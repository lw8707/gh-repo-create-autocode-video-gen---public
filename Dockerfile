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
