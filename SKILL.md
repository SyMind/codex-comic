---
name: comic-workflow
description: 根据用户创意制作 3:4 竖版中文手绘教育漫画：编写按页/分镜脚本，建立角色、场景、风格设定，并优先使用 Codex Chrome 插件自动化 ChatGPT 网页生成参考图和最终漫画页，必要时用 Browser 插件备用，把提示词、图片和清单保存到用户指定目录。适用于漫画、分镜、条漫、角色/场景设定图、需要通过 ChatGPT 网页生成图片并下载归档的完整漫画工作流。
---

# 漫画创作

## 核心约束

- 必须有用户指定的输出目录；缺失时先询问。
- 生成或下载图片前，先选择最高效可用的浏览器控制方式：优先 Codex Chrome 插件，其次 Browser 插件。
- 所有图片固定为 3:4 竖版。用户未指定画风时，使用 `references/visual-style.md`。
- 漫画默认面向抖音等手机竖屏发布：按 1080x1440 竖图基准，任何可读文字不得小于 48px；对白/旁白建议 56px 以上；主标题建议 80px 以上。若生成分辨率不同，最小文字高度不得低于画布高度的 3.3%。文字必须少量、强对比，手机全屏观看也能清楚读出；避免密集小字、长段落和细线浅色文字。
- 图片生成必须通过 ChatGPT 网页完成；本地只负责脚本、提示词、文件归档和校验。不要用本地图片生成、网页抓取或 shell 自动化代替 ChatGPT 图片生成。
- 角色参考图、场景参考图和最终漫画页都可以并发生成；每个生成任务使用独立 ChatGPT 新会话，下载和重命名时必须核对内容，避免串图、串页或覆盖文件。
- 最终漫画页必须“每页一张图、每页一个全新 ChatGPT 对话”。页面生成阶段优先并发打开多个新对话，同时推进多页生成、下载和记录。
- 最终漫画页画面内不得出现页码、页脚页码、角标编号、`Page XX`、`第 XX 页` 等页面编号；文件名仍使用 `pages/page-XX.png`。
- 遇到受版权保护的角色或在世艺术家精确风格要求，改写为安全的描述性视觉特征。

## 工具选择

在进入图片生成阶段前执行：

1. 首选 `Chrome` 插件：ChatGPT 通常需要用户登录态，Chrome 能复用用户真实浏览器、cookies、已有标签页和文件上传能力；适合批量开新会话、并发生成、上传参考图和下载文件。
2. 次选 `Browser` 插件：适合不依赖用户 Chrome 登录态的网页自动化，或用户已在 Codex in-app browser 中完成登录的情况。
3. 若 Chrome 和 Browser 都不可用，暂停图片生成阶段，告知用户需要启用 Chrome 或 Browser 插件。
4. 若 Chrome/ChatGPT 需要登录、权限确认、上传文件、下载文件或其他会产生外部影响的 UI 操作，遵守所选工具对应的确认策略。

## 初始化

先创建项目目录：

```bash
python3 <当前技能路径>/scripts/init_comic_project.py "<输出目录>" --title "<漫画标题>"
```

目录约定：

- `script/comic-script.md`：按页/分镜脚本。
- `bible/characters.md`、`bible/scenes.md`、`bible/style.md`：角色、场景、风格设定。
- `prompts/concepts/`、`prompts/pages/`：发送给 ChatGPT 的提示词。
- `references/characters/`、`references/scenes/`：下载后的参考图。
- `pages/`：最终漫画页。
- `logs/generation-log.md`、`manifest.json`：生成记录和项目清单。

## 工作流

1. 写脚本：`script/comic-script.md` 按页组织；每页写故事节拍、分镜布局、镜头、动作、对白/旁白/音效字和连续性备注；每页文字总量要适合手机竖屏阅读，单个文字块不超过 18 个汉字。
2. 写设定：角色写外观/服装/表情/道具/禁忌；场景写空间/道具/光线/氛围/禁忌；风格写 3:4、阅读方向、抖音大字文字策略和画风锚点。
3. 写提示词：使用 `references/prompt-templates.md`；用户未给画风时先读 `references/visual-style.md`。
4. 生成参考图：用选定的浏览器控制方式操作 ChatGPT UI，为每个角色/场景打开独立新会话；可同时推进多个角色和场景生成任务，下载到 `references/` 后按内容核对命名。
5. 生成漫画页：用选定的浏览器控制方式为每一页打开独立的新 ChatGPT 会话，上传相关参考图，提交该页提示词；可同时打开多个新对话并发生成多页，但每个对话只负责一页、只产出一张最终图；下载到 `pages/page-XX.png` 后按页面内容核对命名。
6. 收尾：确认文件齐全、图片可打开、比例接近 3:4、角色/场景连续性正确；更新 `manifest.json` 并向用户说明结果位置。

## 阶段参考

- ChatGPT 浏览器自动化和下载：`references/chatgpt-browser-automation.md`
- 提示词模板：`references/prompt-templates.md`
- 默认画风：`references/visual-style.md`
