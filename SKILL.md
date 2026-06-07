---
name: comic-workflow
description: 根据用户创意制作 3:4 竖版中文手绘教育漫画：编写按页/分镜脚本，建立角色、场景、风格设定，并使用 Codex 的 Computer Use skill 操作本机 Chrome/ChatGPT UI 生成参考图和最终漫画页，把提示词、图片和清单保存到用户指定目录。适用于漫画、分镜、条漫、角色/场景设定图、需要通过 ChatGPT 网页生成图片并下载归档的完整漫画工作流。
---

# 漫画创作

## 核心约束

- 必须有用户指定的输出目录；缺失时先询问。
- 生成或下载图片前，必须确认本次 Codex 会话可用 Computer Use 能力；若不可用，先告知用户需要安装/启用 Codex Computer Use 插件或技能，暂停图片生成阶段。
- 所有图片固定为 3:4 竖版。用户未指定画风时，使用 `references/visual-style.md`。
- 图片生成必须通过 Computer Use 操作本机 Chrome/ChatGPT 网页 UI；本地只负责脚本、提示词、文件归档和校验。
- 最终漫画页必须“每页一张图、每页一个全新 ChatGPT 对话”。页面生成阶段优先并发打开多个新对话，同时推进多页生成、下载和记录。
- 最终漫画页画面内不得出现页码、页脚页码、角标编号、`Page XX`、`第 XX 页` 等页面编号；文件名仍使用 `pages/page-XX.png`。
- 遇到受版权保护的角色或在世艺术家精确风格要求，改写为安全的描述性视觉特征。

## 前置检测

在进入图片生成阶段前执行：

1. 检查当前可用 skills 中是否有 `computer-use` 或 `computer-use:computer-use`。
2. 若可用，阅读其确认策略，只在需要操作本机 UI 时调用 Computer Use。
3. 若不可用，不要尝试用 shell、网页抓取或本地图片生成绕过；请用户安装/启用 Codex Computer Use，然后继续。
4. 若 Chrome/ChatGPT 需要登录、权限确认、上传文件、下载文件或其他会产生外部影响的 UI 操作，遵守 Computer Use 的确认策略。

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

1. 写脚本：`script/comic-script.md` 按页组织；每页写故事节拍、分镜布局、镜头、动作、对白/旁白/音效字和连续性备注。
2. 写设定：角色写外观/服装/表情/道具/禁忌；场景写空间/道具/光线/氛围/禁忌；风格写 3:4、阅读方向、文字策略和画风锚点。
3. 写提示词：使用 `references/prompt-templates.md`；用户未给画风时先读 `references/visual-style.md`。
4. 生成参考图：通过 Computer Use 操作 Chrome/ChatGPT UI，按角色/场景逐个新开会话，下载到 `references/`。
5. 生成漫画页：通过 Computer Use 为每一页打开独立的新 ChatGPT 会话，上传相关参考图，提交该页提示词；可同时打开多个新对话并发生成多页，但每个对话只负责一页、只产出一张最终图；下载到 `pages/page-XX.png`。
6. 收尾：确认文件齐全、图片可打开、比例接近 3:4、角色/场景连续性正确；更新 `manifest.json` 并向用户说明结果位置。

## 阶段参考

- Computer Use 浏览器操作和下载：`references/chatgpt-chrome-workflow.md`
- 提示词模板：`references/prompt-templates.md`
- 默认画风：`references/visual-style.md`
