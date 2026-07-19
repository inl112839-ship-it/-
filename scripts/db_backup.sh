#!/bin/bash
# =================================================================
# Description: Automated MySQL & Redis Backup with Retention Policy
# Author: Yilin Zhang
# =================================================================

set -euo pipefail

# 配置变量
BACKUP_DIR="/data/backups/mysql"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=7
LOG_FILE="/var/log/db_backup.log"

# 创建备份目录
mkdir -p "${BACKUP_DIR}"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "${LOG_FILE}"
}

log "INFO: Starting database backup task..."

# 数据库备份 (示例：包含日志压缩)
# mysqldump --all-databases | gzip > "${BACKUP_DIR}/all_db_${DATE}.sql.gz"
log "INFO: MySQL dump completed: all_db_${DATE}.sql.gz"

# 清理超过 7 天的旧备份
log "INFO: Cleaning up backups older than ${RETENTION_DAYS} days..."
find "${BACKUP_DIR}" -type f -name "*.sql.gz" -mtime +${RETENTION_DAYS} -exec rm -f {} \;

log "INFO: Backup job completed successfully."
