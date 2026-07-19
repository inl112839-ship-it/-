# 🚀 AI-Powered OpsTools & SRE Infrastructure Toolkit

这是一个集成 **运维自动化脚本、监控套件配置与 CI/CD 流水线实践** 的核心代码仓库。
结合 Cursor、Claude Code、GitHub Copilot 等 AI 工具辅助快速构建与开发，旨在提升企业生产环境的高可用性与运维交付效率。

---

## 🛠️ 项目主要功能与技术栈

### 1. 自动化运维与巡检脚本 (`/scripts`)
* **`server_inspector.py`**: 基于 Python 的服务器基础性能（CPU、内存、磁盘 IO、网络连通性）自动化巡检与 Telegram/钉钉告警通知。
* **`db_backup_sync.sh`**: MySQL / Redis 数据库自动化增量备份及异地容灾同步脚本（带日志审计与自动清理）。

### 2. 监控与告警体系 (`/monitoring`)
* **Prometheus + Grafana** 生产级监控配置文件，包含服务器节点（Node Exporter）与数据库（MySQL Exporter）监控 Dashboards 模板。
* 自定义告警规则（Alertmanager），实现生产环境指标异常秒级响应。

### 3. CI/CD 与容器化部署 (`/deploy`)
* **`Jenkinsfile`**: 标准化多环境（Test/Staging/Prod）自动化构建、测试与镜像发布流水线。
* **`docker-compose.yml`**: 高可用基础服务的极速一键部署脚手架。

---

## 💻 AI 工具赋能与实践
在本项目开发过程中，充分借助 AI 编程工具提高代码重构与运维交付效率：
* **Cursor / Claude Code**: 快速生成高健壮性的 Python/Shell 脚本结构及异常处理逻辑。
* **GitHub Copilot**: 辅助编写复杂正则表达式、Shell 命令及 Dockerfile 配置。

---

## 🛡️ 许可证与安全说明
* 本项目仅用于个人技术展示与自动化工具模版积累。
* **敏感信息声明**：所有配置与代码均已剔除生产环境 IP、账号密码及加密密钥，符合数据安全与合规审计标准。
