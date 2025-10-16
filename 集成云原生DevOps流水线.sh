#!/bin/bash
echo "🚀 集成云原生DevOps流水线..."

# 创建CI/CD配置文件
mkdir -p .gitee workflows

cat > .gitee/pipeline.yml << 'PIPELINE_EOF'
name: AI开发平台流水线
version: '2.0'

stages:
  - name: 代码检查
    steps:
      - name: 安全扫描
        type: docker
        image: security-scanner:latest
        commands:
          - python security_scan.py
        
      - name: 代码质量
        type: docker  
        image: python:3.9
        commands:
          - pip install pylint bandit
          - pylint **/*.py
          - bandit -r .

  - name: 构建测试
    steps:
      - name: 单元测试
        type: docker
        image: python:3.9
        commands:
          - pip install pytest
          - pytest tests/ -v
          
      - name: 集成测试
        type: docker
        image: python:3.9
        commands:
          - python -m unittest discover integration_tests/

  - name: 构建打包
    steps:
      - name: 打包应用
        type: docker
        image: python:3.9
        commands:
          - pip install pyinstaller
          - pyinstaller --onefile main.py
          
      - name: 容器化
        type: docker-build
        dockerfile: Dockerfile
        image: my-ai-platform:latest

  - name: 部署
    steps:
      - name: 开发环境
        type: kubernetes
        cluster: dev
        namespace: ai-platform
        yaml: k8s/dev-deployment.yaml
        
      - name: 生产环境
        type: kubernetes
        cluster: prod
        namespace: ai-platform
        yaml: k8s/prod-deployment.yaml
        when:
          branch: main
PIPELINE_EOF

# 创建Dockerfile
cat > Dockerfile << 'DOCKER_EOF'
FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 复制代码
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# 创建非root用户
RUN useradd -m -u 1000 appuser
USER appuser

EXPOSE 8000

CMD ["python", "main.py"]
DOCKER_EOF

# 创建Kubernetes部署文件
mkdir -p k8s

cat > k8s/prod-deployment.yaml << 'K8S_EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-platform
  namespace: ai-platform
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-platform
  template:
    metadata:
      labels:
        app: ai-platform
    spec:
      containers:
      - name: ai-platform
        image: my-ai-platform:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: ai-platform-service
  namespace: ai-platform
spec:
  selector:
    app: ai-platform
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
K8S_EOF

# 创建本地开发流水线
cat > local_dev_pipeline.sh << 'LOCAL_EOF'
#!/bin/bash
echo "🔧 本地开发流水线启动..."

# 1. 代码质量检查
echo "📋 运行代码检查..."
python -m pylint **/*.py --exit-zero
python -m bandit -r . -f json -o bandit_report.json

# 2. 安全扫描
echo "🛡️ 运行安全扫描..."
python enhanced_security_demo.py

# 3. 测试
echo "🧪 运行测试..."
if [ -d "tests" ]; then
    python -m pytest tests/ -v
else
    echo "⚠️ 未找到测试目录，跳过测试"
fi

# 4. 构建
echo "🏗️ 构建应用..."
if command -v pyinstaller >/dev/null 2>&1; then
    pyinstaller --onefile main.py 2>/dev/null || echo "⚠️ 构建失败，继续..."
else
    echo "⚠️ pyinstaller未安装，跳过构建"
fi

echo "✅ 本地流水线完成"
LOCAL_EOF

chmod +x local_dev_pipeline.sh

echo "✅ 云原生DevOps流水线配置完成"
echo "运行: ./local_dev_pipeline.sh 开始本地开发流水线"
