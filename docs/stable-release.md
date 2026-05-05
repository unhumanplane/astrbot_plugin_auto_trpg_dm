# 稳定版发布说明

这个仓库是面向 AstrBot 插件市场发布的稳定版仓库。稳定版优先贴合 AstrBot 插件审核规范，和开发仓库会有少量实现差异。

## 数据目录

稳定版通过 `StarTools.get_data_dir()` 获取插件数据目录。运行数据默认写入 AstrBot 为插件分配的 `data/plugin_data/<plugin_name>` 目录下，包括：

- `saves/`：跑团存档。
- `save_backups/`：存档备份。
- `audit/`：关键工具调用和诊断记录。
- `maps/`：战棋地图输出。
- `ambient_images/`：游戏配图输出。
- `rulebooks/`：运行时规则书缓存。

## 日志

稳定版不再写入独立的 `logs/auto_trpg_dm.log` 文件，而是统一使用 AstrBot 提供的 `logger`。这样更符合插件市场 reviewer 对日志来源的要求。

需要排查问题时，优先查看：

- AstrBot 控制台或运行日志。
- 插件数据目录下的 `audit/*.jsonl`。
- AstrBot 插件配置里的相关开关和 provider 配置。

开发仓库可以继续保留独立日志文件用于本地排障；稳定版以审核规范和市场分发稳定性为优先。
