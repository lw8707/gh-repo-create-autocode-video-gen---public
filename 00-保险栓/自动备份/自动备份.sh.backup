#!/bin/bash
echo "执行自动备份..."

cd ~/my-ai-business/我的智能体课程
tar -czf 00-保险栓/自动备份/项目备份.tar.gz --exclude=00-保险栓 --exclude=*.tar.gz .

if [ -d "/sdcard/Huawei/Cloud" ]; then
    cp 00-保险栓/自动备份/项目备份.tar.gz /sdcard/Huawei/Cloud/
    echo "已备份到华为云空间"
else
    cp 00-保险栓/自动备份/项目备份.tar.gz /sdcard/Download/
    echo "已备份到手机存储"
fi

echo "备份完成"
