# ChatGPT Computer Use 工作流

仅在生成或下载图片时阅读。

## 前置

- 使用 Codex 的 Computer Use skill 操作本机 Chrome/ChatGPT UI。
- 开始前确认 Computer Use 可用，并按其确认策略处理登录、上传、下载、权限弹窗和第三方传输。
- 不要用本地图片生成、网页抓取或 shell 自动化代替 ChatGPT UI 生成。

## 生成

1. 用 Computer Use 打开或切换到本机 Chrome，并进入 `https://chatgpt.com/`。
2. 每个角色、场景、漫画页默认新开会话。最终漫画页生成时，优先同时打开多个新的 ChatGPT 会话并发推进；每个会话只处理一页，避免在同一对话连续生成多页。
3. 设定图：提交 `prompts/concepts/` 中对应提示词，必要时只按设定做局部修正。
4. 漫画页：先上传相关参考图，再提交 `prompts/pages/page-XX.md`；提示词必须说明每张附件的用途，并明确画面内不要页码、页脚页码、角标编号或 `Page XX`/`第 XX 页` 字样。
5. 下载前确认结果可用：3:4 竖版、主体正确、无明显连续性错误。否则先在同一会话修正。

## 下载

1. 如控件隐藏，先悬停或聚焦图片。
2. 点击分享图片按钮。若 Computer Use 可以读取控件属性，优先寻找：

```css
button[aria-label="分享此图片"]
```

3. 再点击分享/下载界面中的大型圆形确认按钮；用户提供过的特征为：

```html
<div class="flex items-center justify-center rounded-full composer-submit-button-color h-16 w-16 shadow-lg">...</div>
```

4. 如果文件进入默认下载目录，移动最新图片到项目目录并重命名：
   - 角色：`references/characters/<slug>-reference.png`
   - 场景：`references/scenes/<slug>-reference.png`
   - 页面：`pages/page-XX.png`
5. 在 `logs/generation-log.md` 记录提示词路径、图片路径、对应 ChatGPT 会话和必要备注；并发下载时先核对文件时间和页面内容再重命名，避免串页。
