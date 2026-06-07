# ChatGPT 浏览器自动化工作流

仅在生成或下载图片时阅读。

## 前置

- 优先使用 Codex Chrome 插件控制用户本机 Chrome，因为 ChatGPT 通常需要用户登录态、已有 cookies 和文件上传能力。
- 若 Chrome 插件不可用且用户已在 Codex in-app browser 中登录 ChatGPT，可使用 Browser 插件。
- 开始前确认所选浏览器控制方式可用，并按其确认策略处理登录、上传、下载、权限弹窗和第三方传输。
- 不要用本地图片生成、网页抓取或 shell 自动化代替 ChatGPT UI 生成。

## 操作优先级

1. 优先使用 DOM/Playwright 定位、键盘输入、文件选择器和下载事件，减少视觉点击。
2. 找不到稳定选择器时，先截图或读取页面状态确认控件位置，再点击。
3. 并发生成时用多个独立标签页/会话推进任务；每个标签页只绑定一个角色、场景或页面。

## 生成

1. 用所选浏览器控制方式打开或切换到 ChatGPT：优先用户本机 Chrome 的 `https://chatgpt.com/`。
2. 每个角色、场景、漫画页默认新开会话。角色参考图、场景参考图和最终漫画页都可以并发推进；每个会话只处理一个生成任务，避免在同一对话连续生成多个角色、多个场景或多页漫画。
3. 设定图：提交 `prompts/concepts/` 中对应提示词，必要时只按设定做局部修正。
4. 漫画页：先通过文件选择器上传相关参考图，再提交 `prompts/pages/page-XX.md`；提示词必须说明每张附件的用途，并明确画面内不要页码、页脚页码、角标编号或 `Page XX`/`第 XX 页` 字样。
5. 下载前确认结果可用：3:4 竖版、主体正确、无明显连续性错误。否则先在同一会话修正。

## 下载

1. 如控件隐藏，先悬停或聚焦图片。
2. 点击分享图片按钮。使用 Chrome/Browser 自动化时优先用稳定选择器定位；可优先寻找：

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
5. 在 `logs/generation-log.md` 记录提示词路径、图片路径、对应 ChatGPT 会话和必要备注；并发下载时先核对文件时间、标签页任务和页面内容再重命名，避免串图或串页。
