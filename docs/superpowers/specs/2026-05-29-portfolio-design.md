# 求职作品集设计规格

## 概述

一个多页面静态作品集网站，展示三个求职方向：UI/UX 设计、Unity 游戏开发、AIGC 生成。采用干净现代的视觉风格，中英双语，自行托管视频。

## 目标用户

求职者本人，面向潜在雇主/面试官。

## 站点结构

```
首页 (/)
├── UI/UX 设计 (/uiux)
├── Unity 游戏开发 (/unity)
│   └── 项目详情 (/unity/project-slug)
├── AIGC 生成 (/aigc)
└── 关于我 (/about)
```

中英双语通过 URL 路径区分：`/zh/unity` vs `/en/unity`。

## 技术选型

| 类别 | 选型 | 理由 |
|------|------|------|
| 框架 | Astro | 静态生成性能极好，内置 i18n 路由 |
| 样式 | Tailwind CSS | 干净现代风格，快速开发 |
| 视频 | HTML5 `<video>` 自托管 | 自行控制播放体验 |
| 部署 | Vercel / GitHub Pages | 免费，自动部署 |
| 版本管理 | Git | |

## 视觉设计

### 配色

- 背景：`#FFFFFF`（白）/ `#F8F9FA`（浅灰交替）
- 主文字：`#1A1A1A`
- 辅助文字：`#6B7280`
- 强调色：`#2563EB`（蓝色，按钮、链接、hover 状态）
- 卡片边框：`#E5E7EB`

### 字体

- 中文：系统默认（`system-ui`）
- 英文/代码：`Inter` 或系统 sans-serif

### 组件

- 卡片：圆角 12px，轻微阴影，hover 上浮
- 按钮：圆角 8px，实心蓝 + 文字白
- 视频：16:9 比例容器，圆角 8px，自带播放控件
- 导航栏：顶部固定，Logo 左，导航链接右，语言切换最右

## 页面设计

### 首页 (/)

- 全屏 Hero：名字 + 一句话定位（"游戏开发者 / UI设计师 / AIGC创作者"）
- 向下滚动，三个方向入口卡片（大图 + 标题 + 一句话描述）
- 底部：GitHub 链接

### Unity 页 (/unity)

- 项目卡片网格（2-3 个），每个卡片：封面图 + 标题 + 标签
- 点击进入项目详情页

### 项目详情页 (/unity/project-slug)

- 顶部：视频播放器（16:9）
- 下方：项目标题、文字描述、技术栈标签
- 底部：返回按钮

### UI/UX 页 (/uiux) 和 AIGC 页 (/aigc)

- 空状态提示："更多作品即将上线" / "More projects coming soon"

### 关于我 (/about)

- 头像 + 姓名
- 个人简介（一段话）
- 技能标签（Unity, C#, Figma, Stable Diffusion 等）
- 完整联系方式（邮箱、微信、GitHub）

## 内容数据模型

### 项目 (Project)

```yaml
title: { zh: "项目名", en: "Project Name" }
description: { zh: "描述", en: "Description" }
cover: "/images/projects/xxx-cover.jpg"
video: "/videos/xxx-demo.mp4"
tags: ["Unity", "C#", "3D"]
slug: "project-slug"
```

### 技能标签

扁平列表，中英通用：`["Unity", "C#", "Figma", "Stable Diffusion", "ComfyUI"]`

## 媒体格式要求

- 视频：MP4（H.264），分辨率 1080p，码率适中以控制文件大小
- 封面图：JPG/PNG，宽 1200px，16:9 比例
- 头像：JPG/PNG，正方形，400x400px 以上

## 初始内容

- Unity 方向：2-3 个现有项目（exe 截图/封面 + 视频演示）
- UI/UX 方向：空状态占位
- AIGC 方向：空状态占位
- 用户需提供：项目视频文件、封面截图、头像、个人简介文案、联系方式
