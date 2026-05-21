# 漫画工作流 Codex Skill

这个仓库提供一个 Codex skill：`comic-workflow`。它会根据用户创意制作 3:4 竖版中文手绘教育漫画，并把脚本、设定、提示词、生成图片和清单整理到用户指定目录。

## 效果展示

<p>
  <img src="assets/showcase/page-00.jpg" alt="示例漫画页 00" width="160">
  <img src="assets/showcase/page-01.jpg" alt="示例漫画页 01" width="160">
  <img src="assets/showcase/page-02.jpg" alt="示例漫画页 02" width="160">
  <img src="assets/showcase/page-03.jpg" alt="示例漫画页 03" width="160">
  <img src="assets/showcase/page-04.jpg" alt="示例漫画页 04" width="160">
  <img src="assets/showcase/page-05.jpg" alt="示例漫画页 05" width="160">
  <img src="assets/showcase/page-06.jpg" alt="示例漫画页 06" width="160">
</p>

## 安装

告诉你的 agent：

> Install the `comic-workflow` skill from `github.com/<owner>/<repo>`.

或者直接运行安装命令：

```bash
# 项目级安装
npx skills add <owner>/<repo>

# 全局安装
npx skills add <owner>/<repo> -g
```

也可以手动克隆到 Codex skills 目录：

```bash
git clone https://github.com/<owner>/<repo> ~/.codex/skills/comic-workflow
```

安装后，通过 `$comic-workflow` 调用。

## 功能

- 写按页/分镜脚本。
- 建立角色、场景、风格设定。
- 通过 Codex Chrome 插件在 ChatGPT 生成参考图和漫画页。
- 并发打开多个 ChatGPT 新对话生成最终页面，每页一个对话、每页一张图。
- 下载并整理图片、提示词、生成记录和项目清单。

## 隐私说明

- 不要提交生成漫画项目中的私人素材、提示词、下载图片或 `.env` 文件。
- 默认示例输出目录 `output/` 已被 `.gitignore` 忽略。
- 发布到公开 GitHub 前，请检查 Git commit author 信息是否会暴露个人姓名或邮箱。
