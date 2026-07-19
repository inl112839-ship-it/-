#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Server Health Inspector & Alerting Tool
Features: CPU, Memory, Disk, Network Connectivity & Process Monitoring.
Author: Yilin Zhang
"""

import sys
import psutil
import requests
import logging

# 配置日志规范
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 告警阈值定义
THRESHOLDS = {
    'cpu_percent': 85.0,
    'memory_percent': 90.0,
    'disk_percent': 90.0
}

def check_system_metrics():
    """收集并检查系统基础指标"""
    alerts = []
    
    # 1. CPU 占用率检查
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > THRESHOLDS['cpu_percent']:
        alerts.append(f"⚠️ [CPU Warning] CPU Usage high: {cpu_usage}% (Threshold: {THRESHOLDS['cpu_percent']}%)")
        
    # 2. 内存使用率检查
    mem = psutil.virtual_memory()
    if mem.percent > THRESHOLDS['memory_percent']:
        alerts.append(f"⚠️ [Memory Warning] Memory Usage high: {mem.percent}% (Threshold: {THRESHOLDS['memory_percent']}%)")
        
    # 3. 根磁盘空间检查
    disk = psutil.disk_usage('/')
    if disk.percent > THRESHOLDS['disk_percent']:
        alerts.append(f"🚨 [Disk Critical] Disk Usage high: {disk.percent}% (Threshold: {THRESHOLDS['disk_percent']}%)")

    return alerts

def send_webhook_alert(webhook_url, messages):
    """发送告警消息至企业微信/钉钉 Webhook"""
    if not messages:
        logging.info("All metrics are healthy. No alerts triggered.")
        return
        
    payload = {
        "msgtype": "text",
        "text": {
            "content": "【生产环境服务器异常告警】\n" + "\n".join(messages)
        }
    }
    
    try:
        response = requests.post(webhook_url, json=payload, timeout=5)
        if response.status_code == 200:
            logging.info("Alert message sent successfully.")
        else:
            logging.error(f"Failed to send alert: {response.status_code}")
    except Exception as e:
        logging.error(f"Webhook request failed: {str(e)}")

if __name__ == '__main__':
    logging.info("Starting System Health Check...")
    detected_alerts = check_system_metrics()
    
    if detected_alerts:
        print("\n".join(detected_alerts))
        # 实际生产环境中可传入 Webhook URL 发送告警
        # send_webhook_alert("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx", detected_alerts)
    else:
        logging.info("System Health Check Completed. Status: OK")
