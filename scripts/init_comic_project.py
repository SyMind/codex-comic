#!/usr/bin/env python3
"""为漫画生成项目创建稳定的目录骨架。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


DIRS = [
    "script",
    "bible",
    "prompts/concepts",
    "prompts/pages",
    "references/characters",
    "references/scenes",
    "pages",
    "downloads",
    "logs",
]


PLACEHOLDERS = {
    "script/comic-script.md": "# 漫画脚本\n\n",
    "bible/characters.md": "# 角色设定\n\n",
    "bible/scenes.md": "# 场景设定\n\n",
    "bible/style.md": (
        "# 风格设定\n\n"
        "- 图片比例：3:4 竖版。\n"
        "- 页面编号：画面内不放页码、页脚页码或角标编号；仅用文件名排序。\n"
        "- 默认画风：中文手绘教育漫画信息图；详见 skill 的 `references/visual-style.md`。\n"
    ),
    "logs/generation-log.md": "# 生成记录\n\n",
}


def create_project(output_dir: Path, title: str) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)

    for relative in DIRS:
        (output_dir / relative).mkdir(parents=True, exist_ok=True)

    for relative, content in PLACEHOLDERS.items():
        path = output_dir / relative
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    manifest_path = output_dir / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {
            "title": title,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": "已初始化",
            "script": "script/comic-script.md",
            "bibles": {
                "characters": "bible/characters.md",
                "scenes": "bible/scenes.md",
                "style": "bible/style.md",
            },
            "references": {
                "characters": [],
                "scenes": [],
            },
            "pages": [],
            "logs": ["logs/generation-log.md"],
        }

    manifest["title"] = title or manifest.get("title") or output_dir.name
    manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="初始化漫画生成项目的输出目录。"
    )
    parser.add_argument("output_dir", help="用于保存漫画输出内容的目录。")
    parser.add_argument(
        "--title",
        default="未命名漫画",
        help="写入 manifest.json 的漫画标题。",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).expanduser().resolve()
    manifest = create_project(output_dir, args.title)

    print(
        json.dumps(
            {"输出目录": str(output_dir), "项目清单": manifest},
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
