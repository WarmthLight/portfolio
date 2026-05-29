---
title:
  zh: "TripWise — AI 智能旅行规划"
  en: "TripWise — AI-Powered Travel Planning"
subtitle:
  zh: "用 AI 重新定义旅行规划体验，让每一次出发都充满期待"
  en: "Redefining travel planning with AI — making every journey as exciting as the destination"
cover: "/images/projects/placeholder-cover.svg"
role:
  zh: "主导 UI/UX 设计师"
  en: "Lead UI/UX Designer"
timeline: "2025.03 — 2025.09"
tags: ["UI/UX", "移动应用", "AI", "旅行", "Figma"]
order: 1
metrics:
  - label:
      zh: "行程规划时间"
      en: "Planning Time"
    value: "3天 → 30分钟"
  - label:
      zh: "用户留存率"
      en: "Retention"
    value: "+45%"
  - label:
      zh: "旅行完成率"
      en: "Trip Completion"
    value: "92%"
  - label:
      zh: "App评分"
      en: "App Rating"
    value: "4.9/5"
---

<div id="background"></div>

## 项目背景


### 问题定义

旅行是人们最向往的生活体验之一，但旅行前的规划过程却往往令人焦虑和疲惫。一个典型的旅行规划流程需要用户在多个平台之间反复跳转——在小红书查找目的地推荐，在马蜂窝阅读攻略，在 Google Maps 规划路线，在携程比价机票酒店，在天气应用查看出行日期的气候数据。平均而言，规划一次 5-7 天的旅行需要耗费 3-5 天的时间，涉及至少 6 个不同的应用程序。

这种碎片化的规划体验不仅耗时，还常常导致信息遗漏和决策疲劳。许多潜在旅行者因为规划过程过于繁琐而选择放弃旅行，或者在旅行中因为准备不足而留下遗憾。

### 用户画像

**画像一：独行探险者 — 林小然（28岁，自由职业）**

林小然是一位自由插画师，每年有 4-6 次独自旅行的机会。她追求深度体验和小众目的地，但经常陷入"信息过载"的困境。她在 Pinterest 上收藏了上百个旅行灵感，却很难将碎片化的想法转化为可执行的行程。她需要的是一个能理解她的审美偏好、并自动将灵感串联成行程的智能工具。

**画像二：情侣周末玩家 — 张明 & 李婷（30岁，互联网从业者）**

张明和李婷都是互联网公司的产品经理，工作繁忙，只有周末和小长假可以出行。他们最头疼的问题是"去哪玩"——两人的兴趣点不完全一致，需要在有限的时间内找到双方都满意的平衡点。他们希望有一个工具能同时考虑两个人的偏好，快速生成兼顾双方兴趣的短途行程。

**画像三：亲子旅行组织者 — 王海燕（33岁，全职妈妈）**

王海燕是一个 5 岁男孩的妈妈，每次带娃出行都需要考虑大量的限制条件：景点是否适合儿童、餐饮是否有儿童菜单、交通是否方便推婴儿车、行程节奏是否适合孩子的体力。她需要一个能根据家庭成员情况自动调整行程节奏的规划工具。

### 商业目标

让旅行规划变得像旅行本身一样令人享受。通过 AI 技术将碎片化的旅行信息整合为个性化的智能行程，降低规划门槛，提升用户的旅行体验和出行意愿。

---

<div id="research"></div>

## 用户研究


### 用户访谈关键洞察

我们对 30 位目标用户进行了深度访谈，覆盖 25-35 岁的年轻旅行群体，总结出以下五项核心洞察：

**洞察一：规划是最大的出行障碍**

87% 的受访者表示，"规划太麻烦"是他们推迟或取消旅行计划的首要原因。用户平均在规划阶段投入的时间是旅行时间的 3-5 倍。

**洞察二：AI 接受度两极分化**

用户对 AI 生成行程的态度存在明显分化。40% 的用户表示"非常愿意尝试 AI 规划"，但 35% 的用户担心 AI 会遗漏个性化细节。关键在于让用户感到"可控"——AI 建议 + 人工微调的混合模式是最受欢迎的方案。

**洞察三：离线功能是刚需而非锦上添花**

92% 的用户在旅行中遇到过网络不稳定或无网络的情况。当前市场上几乎所有旅行应用都依赖在线功能，这是一个明显的市场空白。

**洞察四：社交分享以"炫耀"为主**

用户最常分享的不是行程本身，而是旅途中的即时体验和精美照片。78% 的用户希望行程记录功能能自动生成适合社交分享的图文内容。

**洞察五：行程灵活性至关重要**

62% 的受访者表示，他们会在旅行中临时调整计划。过于固定的行程反而会带来压力。行程需要具备"弹性"——可以随时调整顺序、替换景点，而不影响整体逻辑。

### 竞品对比分析

| 能力维度 | TripWise | TripIt | Google Trips | Pinterest Travel |
|---------|----------|--------|-------------|-----------------|
| AI 行程生成 | 深度定制 AI | 基础导入 | 有限建议 | 无 |
| 离线模式 | 完整离线 | 部分离线 | 依赖网络 | 不支持 |
| 地图集成 | 深度集成 | 基础展示 | 深度集成 | 无 |
| 社交分享 | 行程+动态 | 分享行程链接 | 无 | 灵感分享 |
| 个性化程度 | 高（学习用户偏好） | 低 | 中 | 高（但无规划能力） |
| 多人协作 | 双人偏好融合 | 行程同步 | 无 | 共享看板 |

### 核心痛点排名

1. **信息碎片化**：用户在 6+ 个应用之间切换，平均需要 3-5 天完成一次旅行规划
2. **个性化缺失**：现有工具无法真正理解用户的旅行风格和偏好，提供的建议千篇一律
3. **离线体验断裂**：旅行中网络不稳定时，规划好的行程无法访问，导航功能失效

---

<div id="architecture"></div>

## 信息架构



TripWise 采用四大核心模块的架构设计：

```
TripWise
├── 探索 (Explore)
│   ├── 目的地推荐
│   ├── 热门路线
│   ├── 灵感画廊
│   └── 社区动态
├── 规划 (Plan)
│   ├── AI 行程生成
│   ├── 行程编辑器
│   ├── 交通规划
│   └── 住宿预订
├── 旅行 (Trip)
│   ├── 实时导航
│   ├── 行程时间线
│   ├── 离线数据
│   └── 旅行记录
└── 我的 (Me)
├── 旅行档案
├── 偏好设置
├── 离线包管理
└── 社交分享
```

### 核心用户流程

**流程一：灵感发现 → AI 生成 → 行程定制**

```
浏览探索页 → 收藏灵感目的地 → 触发 AI 行程生成
→ 设定旅行参数（日期/人数/风格）→ AI 生成初版行程
→ 用户微调细节 → 确认行程 → 下载离线数据
```

**流程二：旅途执行 → 即时调整 → 记录分享**

```
开启旅行模式 → 查看当日行程 → 导航至目的地
→ 完成活动打卡 → 临时调整后续行程 → 自动生成旅行日记
→ 分享至社交平台
```

### 导航结构

底部标签栏采用四个核心入口，确保用户在任何场景下都能快速切换：

- **探索**：罗盘图标，发现目的地和灵感
- **规划**：日历图标，AI 行程生成与编辑
- **旅行**：指南针图标，旅途中的实时助手
- **我的**：个人图标，档案与设置

---

<div id="wireframe"></div>

## 线框图


### 线框图一：目的地探索页

探索页采用沉浸式设计，以大尺寸目的地图片为主视觉。顶部设置搜索栏，支持语音输入和自然语言搜索（如"冬天适合泡温泉的地方"）。搜索栏下方横向滚动展示分类标签：海岛、城市、雪山、美食等。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="p-3 space-y-3">
<div class="h-8 bg-gray-100 rounded-lg flex items-center px-3">
<div class="w-4 h-4 bg-gray-300 rounded mr-2"></div>
<div class="h-2 bg-gray-200 rounded w-1/3"></div>
</div>
<div class="flex gap-2 overflow-hidden">
<div class="h-6 px-3 bg-gray-300 rounded-full flex-shrink-0"></div>
<div class="h-6 px-3 bg-gray-100 rounded-full flex-shrink-0"></div>
<div class="h-6 px-3 bg-gray-100 rounded-full flex-shrink-0"></div>
<div class="h-6 px-3 bg-gray-100 rounded-full flex-shrink-0"></div>
</div>
<div class="h-32 bg-gray-200 rounded-xl relative">
<div class="absolute bottom-2 left-2 right-2 flex justify-between">
<div class="h-4 w-16 bg-white/80 rounded"></div>
<div class="h-4 w-8 bg-white/80 rounded"></div>
</div>
</div>
<div class="grid grid-cols-2 gap-2">
<div class="h-24 bg-gray-100 rounded-lg border border-gray-200"></div>
<div class="h-24 bg-gray-100 rounded-lg border border-gray-200"></div>
</div>
</div>
<div class="h-14 border-t border-gray-200 flex items-center justify-around">
<div class="w-6 h-6 bg-gray-300 rounded"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
</div>
</div>

### 线框图二：行程编辑器

行程编辑器采用纵向时间轴布局，左侧为日期导航条（Day 1、Day 2...），右侧为主编辑区域。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="p-3">
<div class="h-6 bg-gray-100 rounded mb-3"></div>
<div class="flex gap-2 mb-3">
<div class="h-7 w-12 bg-gray-300 rounded-full"></div>
<div class="h-7 w-12 bg-gray-100 rounded-full"></div>
<div class="h-7 w-12 bg-gray-100 rounded-full"></div>
</div>
<div class="relative pl-6 space-y-3">
<div class="absolute left-2 top-0 bottom-0 w-0.5 bg-gray-200"></div>
<div class="relative">
<div class="absolute -left-4 top-2 w-3 h-3 bg-gray-300 rounded-full border-2 border-white"></div>
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2">
<div class="h-2 bg-gray-200 rounded w-1/3 mb-1"></div>
<div class="h-3 bg-gray-300 rounded w-2/3 mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-1/2"></div>
</div>
</div>
<div class="relative">
<div class="absolute -left-4 top-2 w-3 h-3 bg-gray-200 rounded-full border-2 border-white"></div>
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2">
<div class="h-2 bg-gray-200 rounded w-1/4 mb-1"></div>
<div class="h-3 bg-gray-300 rounded w-1/2 mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-2/3"></div>
</div>
</div>
<div class="relative">
<div class="absolute -left-4 top-2 w-3 h-3 bg-gray-200 rounded-full border-2 border-white"></div>
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2">
<div class="h-2 bg-gray-200 rounded w-1/3 mb-1"></div>
<div class="h-3 bg-gray-300 rounded w-3/4 mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-1/2"></div>
</div>
</div>
</div>
<div class="absolute bottom-16 right-4 w-10 h-10 bg-gray-300 rounded-full"></div>
</div>
</div>

### 线框图三：实时旅行视图

实时旅行视图在旅行进行中使用，采用全屏地图为背景，叠加行程信息面板。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="relative h-[500px] bg-gray-100">
<div class="absolute top-3 left-3 right-3 bg-white/90 rounded-lg p-2 flex items-center justify-between">
<div>
<div class="h-3 bg-gray-300 rounded w-20 mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-16"></div>
</div>
<div class="w-8 h-8 bg-gray-200 rounded-full"></div>
</div>
<div class="absolute top-20 left-1/2 -translate-x-1/2 w-4 h-4 bg-gray-400 rounded-full border-2 border-white shadow"></div>
<div class="absolute top-36 right-8 w-3 h-3 bg-gray-300 rounded-full"></div>
<div class="absolute bottom-0 left-0 right-0 bg-white rounded-t-2xl p-3 space-y-2">
<div class="h-3 bg-gray-200 rounded w-1/3 mb-2"></div>
<div class="h-10 bg-gray-50 rounded-lg border border-gray-200 flex items-center px-3">
<div class="w-3 h-3 bg-gray-300 rounded-full mr-2"></div>
<div class="h-2 bg-gray-200 rounded w-1/2"></div>
</div>
<div class="h-10 bg-gray-50 rounded-lg border border-gray-200 flex items-center px-3">
<div class="w-3 h-3 bg-gray-200 rounded-full mr-2"></div>
<div class="h-2 bg-gray-200 rounded w-2/3"></div>
</div>
</div>
</div>
</div>

---

<div id="visual"></div>

## 视觉设计


### 设计理念："自在漫游，轻松规划"

TripWise 的设计哲学核心是"减负"——减轻旅行规划的认知负担，让用户将更多精力放在期待旅行的美好心情上。

视觉语言追求三个关键词：

- **温暖**：旅行是充满期待和愉悦的体验，界面色彩和图形应该传递这种情感
- **轻盈**：信息密度高但不压抑，通过留白和层次感创造呼吸空间
- **探索**：界面本身就应该激发用户的好奇心和探索欲

### 色彩系统

**主色系：Teal-to-Cyan 渐变**

- 主色调：Teal #0D9488 — 传递信任感和专业度，用于核心操作按钮和关键信息
- 辅助色：Cyan #06B6D4 — 增添活力和年轻感，用于次要操作和装饰元素
- 渐变组合：从 Teal 到 Cyan 的渐变用于进度指示、加载动画和重点突出

**强调色：Coral**

- 活力橙：#F97316 — 用于重要提示、收藏状态和交互反馈，与冷色主色形成互补

**中性色系**

- 背景白：#FAFAFA
- 卡片白：#FFFFFF
- 文字主色：#1E293B
- 文字次要：#64748B
- 分割线：#E2E8F0

### 字体方案

- **标题字体**：思源黑体 (Noto Sans SC) Bold/ExtraBold — 大标题和关键信息，传递现代感和力量感
- **正文字体**：思源黑体 Regular/Medium — 正文内容，确保阅读舒适度
- **英文辅助**：Inter — 数字和英文信息，与思源黑体形成和谐搭配
- **行间距**：标题 1.2，正文 1.6，确保中文排版的舒适性

### 图标风格

采用 2px 线条风格的定制图标，风格统一、辨识度高。关键操作图标（如收藏、分享）使用填充样式以增强可点击感。图标与文字标签搭配使用，降低认知负荷。

---

<div id="high-fidelity"></div>

## 高保真设计


### 屏幕一：目的地探索页

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-11 bg-gradient-to-r from-teal-500 to-cyan-500 flex items-end justify-between px-6 pb-1.5">
<span class="text-white/90 text-[11px] font-medium">9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3a4.237 4.237 0 00-6 0zm-4-4l2 2a7.074 7.074 0 0110 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>

<div class="px-4 pt-3 pb-2">
<div class="flex items-center gap-2 bg-gray-100 rounded-xl px-3 py-2.5">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
<span class="text-gray-400 text-[13px]">搜索目的地、灵感或攻略...</span>
<div class="ml-auto w-6 h-6 bg-teal-500 rounded-full flex items-center justify-center">
<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>
</div>
</div>
</div>

<div class="px-4 pb-3 flex gap-2 overflow-x-auto">
<span class="flex-shrink-0 px-3 py-1 bg-teal-500 text-white text-[11px] font-medium rounded-full">全部</span>
<span class="flex-shrink-0 px-3 py-1 bg-gray-100 text-gray-600 text-[11px] rounded-full">海岛</span>
<span class="flex-shrink-0 px-3 py-1 bg-gray-100 text-gray-600 text-[11px] rounded-full">城市</span>
<span class="flex-shrink-0 px-3 py-1 bg-gray-100 text-gray-600 text-[11px] rounded-full">雪山</span>
<span class="flex-shrink-0 px-3 py-1 bg-gray-100 text-gray-600 text-[11px] rounded-full">美食</span>
<span class="flex-shrink-0 px-3 py-1 bg-gray-100 text-gray-600 text-[11px] rounded-full">温泉</span>
</div>

<div class="px-4 pb-3">
<div class="relative rounded-2xl overflow-hidden h-40">
<div class="absolute inset-0 bg-gradient-to-br from-teal-400 via-cyan-400 to-teal-600"></div>
<div class="absolute inset-0 flex flex-col justify-end p-4">
<div class="flex items-center gap-1.5 mb-1">
<span class="px-1.5 py-0.5 bg-white/20 backdrop-blur-sm rounded text-[9px] text-white">AI推荐</span>
<span class="px-1.5 py-0.5 bg-orange-400/80 backdrop-blur-sm rounded text-[9px] text-white">热度98</span>
</div>
<h3 class="text-white font-bold text-lg leading-tight">日本京都</h3>
<p class="text-white/80 text-[11px] mt-0.5">千年古都，春日樱花季 · 5天4晚</p>
<div class="flex items-center gap-1 mt-1.5">
<div class="w-4 h-4 rounded-full bg-white/30"></div>
<div class="w-4 h-4 rounded-full bg-white/30 -ml-2"></div>
<div class="w-4 h-4 rounded-full bg-white/30 -ml-2"></div>
<span class="text-white/70 text-[9px] ml-1">1.2万人收藏</span>
</div>
</div>
<div class="absolute top-3 right-3 w-8 h-8 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center">
<svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
</div>
</div>
</div>

<div class="px-4 pb-2">
<div class="flex justify-between items-center mb-2">
<span class="text-[13px] font-bold text-gray-800">为你推荐</span>
<span class="text-[11px] text-teal-500">查看更多</span>
</div>
<div class="flex gap-2">
<div class="flex-1 rounded-xl overflow-hidden bg-gray-100">
<div class="h-20 bg-gradient-to-br from-amber-300 to-orange-400"></div>
<div class="p-2">
<p class="text-[11px] font-semibold text-gray-800">清迈</p>
<p class="text-[9px] text-gray-500">泰北玫瑰 · 4天</p>
<div class="flex items-center gap-0.5 mt-1">
<svg class="w-2.5 h-2.5 text-amber-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<span class="text-[9px] text-gray-500">4.8</span>
</div>
</div>
</div>
<div class="flex-1 rounded-xl overflow-hidden bg-gray-100">
<div class="h-20 bg-gradient-to-br from-sky-300 to-blue-500"></div>
<div class="p-2">
<p class="text-[11px] font-semibold text-gray-800">冰岛</p>
<p class="text-[9px] text-gray-500">极光之旅 · 7天</p>
<div class="flex items-center gap-0.5 mt-1">
<svg class="w-2.5 h-2.5 text-amber-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<span class="text-[9px] text-gray-500">4.9</span>
</div>
</div>
</div>
<div class="flex-1 rounded-xl overflow-hidden bg-gray-100">
<div class="h-20 bg-gradient-to-br from-emerald-300 to-teal-500"></div>
<div class="p-2">
<p class="text-[11px] font-semibold text-gray-800">巴厘岛</p>
<p class="text-[9px] text-gray-500">海岛度假 · 5天</p>
<div class="flex items-center gap-0.5 mt-1">
<svg class="w-2.5 h-2.5 text-amber-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
<span class="text-[9px] text-gray-500">4.7</span>
</div>
</div>
</div>
</div>
</div>

<div class="h-14 border-t border-gray-100 flex items-center justify-around px-2 mt-2">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-teal-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
<span class="text-[9px] font-medium text-teal-500">探索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
<span class="text-[9px] text-gray-400">规划</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
<span class="text-[9px] text-gray-400">旅行</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
</div>

### 屏幕二：AI 行程编辑器

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-11 bg-gradient-to-r from-teal-500 to-cyan-500 flex items-end justify-between px-6 pb-1.5">
<span class="text-white/90 text-[11px] font-medium">9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3a4.237 4.237 0 00-6 0zm-4-4l2 2a7.074 7.074 0 0110 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>

<div class="px-4 pt-3 pb-2">
<div class="flex items-center justify-between">
<div class="flex items-center gap-2">
<svg class="w-4 h-4 text-teal-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15 19l-7-7 7-7"/></svg>
<div>
<h3 class="text-[14px] font-bold text-gray-800">京都5日游</h3>
<p class="text-[10px] text-gray-400">AI 生成 · 可自由编辑</p>
</div>
</div>
<div class="w-8 h-8 bg-teal-50 rounded-full flex items-center justify-center">
<svg class="w-4 h-4 text-teal-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
</div>
</div>
</div>

<div class="px-4 pb-3 flex gap-1.5">
<span class="flex-shrink-0 px-3 py-1.5 bg-teal-500 text-white text-[11px] font-semibold rounded-lg">Day 1</span>
<span class="flex-shrink-0 px-3 py-1.5 bg-gray-100 text-gray-500 text-[11px] rounded-lg">Day 2</span>
<span class="flex-shrink-0 px-3 py-1.5 bg-gray-100 text-gray-500 text-[11px] rounded-lg">Day 3</span>
<span class="flex-shrink-0 px-3 py-1.5 bg-gray-100 text-gray-500 text-[11px] rounded-lg">Day 4</span>
<span class="flex-shrink-0 px-3 py-1.5 bg-gray-100 text-gray-500 text-[11px] rounded-lg">Day 5</span>
</div>

<div class="px-4 relative">
<div class="absolute left-[23px] top-4 bottom-4 w-0.5 bg-teal-200"></div>

<div class="relative flex gap-3 pb-4">
<div class="relative z-10 w-4 h-4 bg-teal-500 rounded-full mt-1 flex-shrink-0 ring-2 ring-white"></div>
<div class="flex-1 bg-white border border-gray-100 rounded-xl p-3 shadow-sm">
<div class="flex justify-between items-start mb-1">
<span class="text-[10px] text-teal-500 font-semibold">09:00 - 12:00</span>
<div class="w-5 h-5 rounded-full bg-gray-50 flex items-center justify-center">
<svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
</div>
</div>
<h4 class="text-[12px] font-bold text-gray-800">伏见稻荷大社</h4>
<p class="text-[10px] text-gray-500 mt-0.5">千本鸟居 · 建议3小时</p>
<div class="flex items-center gap-1.5 mt-2">
<span class="px-1.5 py-0.5 bg-blue-50 text-blue-600 text-[8px] rounded">JR奈良线</span>
<span class="text-[8px] text-gray-400">约20分钟</span>
</div>
</div>
</div>

<div class="relative flex gap-3 pb-4">
<div class="relative z-10 w-4 h-4 bg-cyan-400 rounded-full mt-1 flex-shrink-0 ring-2 ring-white"></div>
<div class="flex-1 bg-white border border-gray-100 rounded-xl p-3 shadow-sm">
<div class="flex justify-between items-start mb-1">
<span class="text-[10px] text-cyan-500 font-semibold">12:30 - 13:30</span>
<div class="w-5 h-5 rounded-full bg-gray-50 flex items-center justify-center">
<svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
</div>
</div>
<h4 class="text-[12px] font-bold text-gray-800">午餐 · 伏见美食</h4>
<p class="text-[10px] text-gray-500 mt-0.5">推荐：稻荷茶寮抹茶甜品</p>
<div class="flex items-center gap-1.5 mt-2">
<span class="px-1.5 py-0.5 bg-orange-50 text-orange-500 text-[8px] rounded">🍜 美食</span>
<span class="text-[8px] text-gray-400">步行5分钟</span>
</div>
</div>
</div>

<div class="relative flex gap-3 pb-3">
<div class="relative z-10 w-4 h-4 bg-white border-2 border-teal-300 rounded-full mt-1 flex-shrink-0 ring-2 ring-white"></div>
<div class="flex-1 bg-white border border-dashed border-teal-200 rounded-xl p-3">
<div class="flex justify-between items-start mb-1">
<span class="text-[10px] text-teal-400 font-semibold">14:00 - 17:00</span>
<div class="w-5 h-5 rounded-full bg-gray-50 flex items-center justify-center">
<svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
</div>
</div>
<h4 class="text-[12px] font-bold text-gray-800">清水寺</h4>
<p class="text-[10px] text-gray-500 mt-0.5">世界遗产 · 建议3小时</p>
<div class="flex items-center gap-1.5 mt-2">
<span class="px-1.5 py-0.5 bg-teal-50 text-teal-500 text-[8px] rounded">🚌 巴士</span>
<span class="text-[8px] text-gray-400">约30分钟</span>
</div>
</div>
</div>
</div>

<div class="px-4 pb-4">
<div class="flex items-center gap-2 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-xl px-4 py-3">
<div class="w-6 h-6 bg-white/20 rounded-full flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
</div>
<span class="text-white text-[12px] font-semibold">AI 智能优化行程</span>
<span class="text-white/70 text-[10px] ml-auto">考虑交通衔接</span>
</div>
</div>

<div class="h-14 border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
<span class="text-[9px] text-gray-400">探索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-teal-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
<span class="text-[9px] font-medium text-teal-500">规划</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
<span class="text-[9px] text-gray-400">旅行</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
</div>

### 屏幕三：旅行详情页

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-11 bg-gradient-to-r from-teal-500 to-cyan-500 flex items-end justify-between px-6 pb-1.5">
<span class="text-white/90 text-[11px] font-medium">9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3a4.237 4.237 0 00-6 0zm-4-4l2 2a7.074 7.074 0 0110 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>

<div class="relative h-44 bg-gradient-to-br from-teal-100 via-cyan-50 to-emerald-100">
<svg class="absolute inset-0 w-full h-full opacity-20" xmlns="http://www.w3.org/2000/svg">
<defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="#0D9488" stroke-width="0.5"/></pattern></defs>
<rect width="100%" height="100%" fill="url(#grid)"/>
</svg>
<svg class="absolute inset-0 w-full h-full" viewBox="0 0 320 176">
<path d="M 40 140 Q 80 100 120 110 T 200 80 T 280 60" fill="none" stroke="#0D9488" stroke-width="2.5" stroke-dasharray="6 3"/>
<circle cx="40" cy="140" r="6" fill="#0D9488"/><text x="40" y="144" text-anchor="middle" fill="white" font-size="7" font-weight="bold">1</text>
<circle cx="120" cy="110" r="6" fill="#06B6D4"/><text x="120" y="114" text-anchor="middle" fill="white" font-size="7" font-weight="bold">2</text>
<circle cx="200" cy="80" r="6" fill="#06B6D4"/><text x="200" y="84" text-anchor="middle" fill="white" font-size="7" font-weight="bold">3</text>
<circle cx="280" cy="60" r="6" fill="#F97316"/><text x="280" y="64" text-anchor="middle" fill="white" font-size="7" font-weight="bold">4</text>
</svg>
<div class="absolute top-2 right-2 bg-white/80 backdrop-blur-sm rounded-lg px-2 py-1.5 flex items-center gap-1.5">
<span class="text-[14px]">🌤</span>
<div>
<span class="text-[10px] font-semibold text-gray-700">22°C</span>
<span class="text-[8px] text-gray-400 block">晴转多云</span>
</div>
</div>
<div class="absolute top-2 left-2 bg-teal-500/90 backdrop-blur-sm rounded-lg px-2.5 py-1">
<span class="text-white text-[10px] font-bold">Day 2 · 清水寺周边</span>
</div>
</div>

<div class="px-4 py-3 border-b border-gray-100">
<div class="flex items-center justify-between">
<div>
<h3 class="text-[13px] font-bold text-gray-800">Day 2 行程</h3>
<p class="text-[10px] text-gray-500 mt-0.5">4个活动 · 步行2.3km</p>
</div>
<div class="flex gap-1">
<span class="px-2 py-0.5 bg-green-50 text-green-600 text-[9px] rounded-full font-medium">已完成 2</span>
<span class="px-2 py-0.5 bg-teal-50 text-teal-600 text-[9px] rounded-full font-medium">剩余 2</span>
</div>
</div>
</div>

<div class="px-4 py-3 space-y-2.5">
<div class="flex items-center gap-3 p-2.5 bg-gray-50 rounded-xl opacity-70">
<div class="w-7 h-7 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0">
<svg class="w-3.5 h-3.5 text-green-500" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
</div>
<div class="flex-1 min-w-0">
<p class="text-[11px] font-semibold text-gray-500 line-through">伏见稻荷大社</p>
<p class="text-[9px] text-gray-400">09:00-12:00 · 已完成</p>
</div>
</div>

<div class="flex items-center gap-3 p-2.5 bg-gray-50 rounded-xl opacity-70">
<div class="w-7 h-7 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0">
<svg class="w-3.5 h-3.5 text-green-500" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
</div>
<div class="flex-1 min-w-0">
<p class="text-[11px] font-semibold text-gray-500 line-through">午餐 · 伏见美食</p>
<p class="text-[9px] text-gray-400">12:30-13:30 · 已完成</p>
</div>
</div>

<div class="flex items-center gap-3 p-2.5 bg-teal-50 border border-teal-200 rounded-xl">
<div class="w-7 h-7 bg-teal-500 rounded-full flex items-center justify-center flex-shrink-0">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
</div>
<div class="flex-1 min-w-0">
<p class="text-[11px] font-bold text-teal-700">清水寺</p>
<p class="text-[9px] text-teal-600">14:00-17:00 · 进行中</p>
</div>
<svg class="w-4 h-4 text-teal-400 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
</div>

<div class="flex items-center gap-3 p-2.5 bg-white border border-gray-100 rounded-xl">
<div class="w-7 h-7 bg-gray-100 rounded-full flex items-center justify-center flex-shrink-0">
<span class="text-[10px] text-gray-400">4</span>
</div>
<div class="flex-1 min-w-0">
<p class="text-[11px] font-semibold text-gray-700">二年坂散步</p>
<p class="text-[9px] text-gray-500">17:30-18:30 · 即将开始</p>
</div>
<svg class="w-4 h-4 text-gray-300 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
</div>
</div>

<div class="h-14 border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
<span class="text-[9px] text-gray-400">探索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
<span class="text-[9px] text-gray-400">规划</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-teal-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
<span class="text-[9px] font-medium text-teal-500">旅行</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
</div>

### 屏幕四：实时导航模式

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-11 bg-gradient-to-r from-teal-500 to-cyan-500 flex items-end justify-between px-6 pb-1.5">
<span class="text-white/90 text-[11px] font-medium">9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3a4.237 4.237 0 00-6 0zm-4-4l2 2a7.074 7.074 0 0110 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>

<div class="bg-gradient-to-r from-teal-500 to-cyan-500 px-4 py-3">
<div class="flex items-center justify-between">
<div>
<p class="text-white/70 text-[9px] uppercase tracking-wider font-medium">当前位置</p>
<h3 class="text-white text-[15px] font-bold mt-0.5">清水寺</h3>
</div>
<div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
</div>
</div>
<div class="flex items-center gap-3 mt-2">
<div class="flex items-center gap-1">
<svg class="w-3 h-3 text-white/70" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
<span class="text-white/80 text-[10px]">已停留 1h 23m</span>
</div>
<div class="flex items-center gap-1">
<svg class="w-3 h-3 text-white/70" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
<span class="text-white/80 text-[10px]">清水区</span>
</div>
</div>
</div>

<div class="bg-amber-50 border-b border-amber-100 px-4 py-2 flex items-center gap-2">
<div class="w-2 h-2 bg-amber-400 rounded-full animate-pulse"></div>
<span class="text-amber-700 text-[10px] font-medium">离线模式 · 数据已缓存</span>
<div class="ml-auto flex items-center gap-1">
<div class="w-3 h-3 bg-amber-400 rounded-full flex items-center justify-center">
<svg class="w-2 h-2 text-white" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M1 1l22 22M16.72 11.06A10.94 10.94 0 019 8.26m-5.38 1.68A10.94 10.94 0 014.34 12M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/></svg>
</div>
</div>
</div>

<div class="relative h-28 bg-gradient-to-br from-teal-50 to-cyan-50 mx-4 mt-3 rounded-xl overflow-hidden">
<svg class="absolute inset-0 w-full h-full opacity-30" xmlns="http://www.w3.org/2000/svg">
<defs><pattern id="miniGrid" width="12" height="12" patternUnits="userSpaceOnUse"><path d="M 12 0 L 0 0 0 12" fill="none" stroke="#0D9488" stroke-width="0.3"/></pattern></defs>
<rect width="100%" height="100%" fill="url(#miniGrid)"/>
</svg>
<svg class="absolute inset-0 w-full h-full" viewBox="0 0 290 112">
<path d="M 50 90 Q 100 50 150 60 T 240 30" fill="none" stroke="#0D9488" stroke-width="2" stroke-dasharray="4 2"/>
<circle cx="150" cy="60" r="8" fill="#0D9488" opacity="0.2"/><circle cx="150" cy="60" r="4" fill="#0D9488"/>
<circle cx="240" cy="30" r="5" fill="#F97316"/>
</svg>
<div class="absolute bottom-1.5 left-1.5 bg-white/80 backdrop-blur-sm rounded px-1.5 py-0.5">
<span class="text-[8px] text-gray-600 font-medium">到下一站：步行 12 分钟</span>
</div>
</div>

<div class="mx-4 mt-3 bg-white border border-gray-100 rounded-xl p-3 shadow-sm">
<div class="flex items-center justify-between mb-1.5">
<span class="text-[9px] font-semibold text-orange-500 uppercase tracking-wider">下一站</span>
<span class="text-[9px] text-gray-400">17:30 开始</span>
</div>
<div class="flex items-center gap-2.5">
<div class="w-10 h-10 bg-gradient-to-br from-orange-200 to-amber-300 rounded-lg flex-shrink-0"></div>
<div class="flex-1">
<h4 class="text-[12px] font-bold text-gray-800">二年坂散步</h4>
<p class="text-[9px] text-gray-500 mt-0.5">京都最有韵味的老街</p>
<div class="flex items-center gap-2 mt-1">
<span class="text-[8px] text-gray-400">📍 步行 12分钟</span>
<span class="text-[8px] text-gray-400">⏱ 约1小时</span>
</div>
</div>
<svg class="w-4 h-4 text-gray-300 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
</div>
</div>

<div class="px-4 py-3">
<div class="flex gap-2">
<div class="flex-1 bg-green-50 rounded-xl py-2.5 flex flex-col items-center gap-1">
<svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
<span class="text-[10px] font-medium text-green-600">已到达</span>
</div>
<div class="flex-1 bg-orange-50 rounded-xl py-2.5 flex flex-col items-center gap-1">
<svg class="w-4 h-4 text-orange-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 010 8h-1M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4V8z"/></svg>
<span class="text-[10px] font-medium text-orange-600">去用餐</span>
</div>
<div class="flex-1 bg-gray-50 rounded-xl py-2.5 flex flex-col items-center gap-1">
<svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01M5.07 19H18.93a2 2 0 001.737-3.002L13.737 4a2 2 0 00-3.474 0L3.333 15.998A2 2 0 005.07 19z"/></svg>
<span class="text-[10px] font-medium text-gray-600">需要帮助</span>
</div>
</div>
</div>

<div class="h-14 border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
<span class="text-[9px] text-gray-400">探索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
<span class="text-[9px] text-gray-400">规划</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-teal-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
<span class="text-[9px] font-medium text-teal-500">旅行</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
</div>

### 屏幕五：社交分享动态卡

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-11 bg-gradient-to-r from-teal-500 to-cyan-500 flex items-end justify-between px-6 pb-1.5">
<span class="text-white/90 text-[11px] font-medium">9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3a4.237 4.237 0 00-6 0zm-4-4l2 2a7.074 7.074 0 0110 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3.5 h-3.5 text-white/90" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>

<div class="px-4 pt-3 pb-2 flex items-center justify-between">
<h3 class="text-[14px] font-bold text-gray-800">社区动态</h3>
<div class="flex items-center gap-1">
<div class="w-6 h-6 bg-teal-100 rounded-full flex items-center justify-center">
<svg class="w-3 h-3 text-teal-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
</div>
</div>
</div>

<div class="px-4 pb-3 flex gap-3">
<div class="flex flex-col items-center gap-1">
<div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 p-0.5">
<div class="w-full h-full rounded-full bg-white p-0.5">
<div class="w-full h-full rounded-full bg-gradient-to-br from-teal-300 to-cyan-300"></div>
</div>
</div>
<span class="text-[8px] text-gray-500">我的旅程</span>
</div>
<div class="flex flex-col items-center gap-1">
<div class="w-12 h-12 rounded-full bg-gradient-to-br from-rose-400 to-orange-400 p-0.5">
<div class="w-full h-full rounded-full bg-white p-0.5">
<div class="w-full h-full rounded-full bg-gradient-to-br from-rose-300 to-orange-300"></div>
</div>
</div>
<span class="text-[8px] text-gray-500">小鱼</span>
</div>
<div class="flex flex-col items-center gap-1">
<div class="w-12 h-12 rounded-full bg-gradient-to-br from-violet-400 to-pink-400 p-0.5">
<div class="w-full h-full rounded-full bg-white p-0.5">
<div class="w-full h-full rounded-full bg-gradient-to-br from-violet-300 to-pink-300"></div>
</div>
</div>
<span class="text-[8px] text-gray-500">阿杰</span>
</div>
<div class="flex flex-col items-center gap-1">
<div class="w-12 h-12 rounded-full bg-gradient-to-br from-amber-400 to-yellow-400 p-0.5">
<div class="w-full h-full rounded-full bg-white p-0.5">
<div class="w-full h-full rounded-full bg-gradient-to-br from-amber-300 to-yellow-300"></div>
</div>
</div>
<span class="text-[8px] text-gray-500">旅行家</span>
</div>
</div>

<div class="px-4 pb-3">
<div class="bg-white border border-gray-100 rounded-2xl overflow-hidden shadow-sm">
<div class="flex items-center gap-2.5 p-3 pb-2">
<div class="w-8 h-8 rounded-full bg-gradient-to-br from-rose-400 to-orange-400"></div>
<div class="flex-1">
<p class="text-[11px] font-bold text-gray-800">小鱼的旅行日记</p>
<p class="text-[9px] text-gray-400">2小时前 · 京都</p>
</div>
<div class="flex items-center gap-1">
<span class="px-1.5 py-0.5 bg-teal-50 text-teal-500 text-[8px] rounded-full">AI生成</span>
</div>
</div>
<div class="grid grid-cols-2 gap-0.5 px-0.5">
<div class="h-24 bg-gradient-to-br from-teal-300 to-cyan-400"></div>
<div class="h-24 bg-gradient-to-br from-orange-300 to-rose-400"></div>
<div class="h-20 bg-gradient-to-br from-amber-200 to-orange-300"></div>
<div class="h-20 bg-gradient-to-br from-emerald-200 to-teal-300"></div>
</div>
<div class="p-3">
<p class="text-[10px] text-gray-600 leading-relaxed">Day 2 的京都之旅完美收官！从千本鸟居到清水寺，每一步都像走在画里。AI 帮我规划的路线刚好避开了人流高峰，下午在清水寺看到了超美的日落...</p>
<div class="flex items-center gap-4 mt-2.5">
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-rose-400" fill="currentColor" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
<span class="text-[10px] text-gray-500">328</span>
</div>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
<span class="text-[10px] text-gray-500">56</span>
</div>
<div class="flex items-center gap-1">
<svg class="w-3.5 h-3.5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
<span class="text-[10px] text-gray-500">分享</span>
</div>
</div>
</div>
</div>
</div>

<div class="h-14 border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/></svg>
<span class="text-[9px] text-gray-400">探索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
<span class="text-[9px] text-gray-400">规划</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
<span class="text-[9px] text-gray-400">旅行</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-5 h-5 text-teal-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<span class="text-[9px] font-medium text-teal-500">我的</span>
</div>
</div>
</div>

---

<div id="interaction"></div>

## 交互设计


### 地图交互

**双指缩放 (Pinch Zoom)**：地图支持 0.5x-4x 的缩放范围。缩放过程中，目的地标记会根据缩放层级动态显示或隐藏——远景模式仅显示城市级标记，放大后逐步显示景点、餐厅、酒店等细节标记。缩放动画采用弹性曲线，手感自然流畅。

**标记点击 (Marker Tap)**：点击地图标记时，标记会执行"弹跳"动画，同时底部滑出目的地信息卡片。卡片包含封面图、名称、评分、距离和"查看详情"按钮。再次点击其他区域或上滑卡片即可关闭。

**路线动画 (Route Animation)**：当用户查看完整行程时，路线会以动画形式从起点绘制至终点，模拟旅行路径。路线颜色随时间变化——已完成部分为实心 Teal，未完成部分为虚线 Cyan。点击路线上的任意节点可跳转至对应活动详情。

**当前位置追踪**：在旅行模式下，用户位置以脉冲圆点实时显示。当用户偏离规划路线超过 100 米时，系统自动触发重新规划提示。

### 行程编辑交互

**拖拽排序 (Drag to Reorder)**：长按活动卡片 0.5 秒后进入拖拽模式。被拖拽的卡片会放大并产生阴影效果，其他卡片自动让位。松手时，卡片以弹性动画落位，系统自动重新计算交通时间和推荐顺序。

**滑动删除 (Swipe to Delete)**：活动卡片支持左右滑动操作。左滑露出红色删除按钮，右滑露出绿色替换按钮。滑动超过卡片宽度的 40% 时自动触发操作，带有触觉反馈。

**长按编辑 (Long Press to Edit)**：长按活动卡片 1 秒后，卡片进入编辑模式。时间、地点、备注等字段变为可编辑状态，同时底部弹出操作面板，支持替换活动、调整时长、添加备注等操作。

### 页面转场动画

**卡片展开 (Card Expand)**：从列表页进入详情页时，列表卡片作为过渡元素展开为详情页的头部区域。动画时长 350ms，使用 `cubic-bezier(0.4, 0, 0.2, 1)` 缓动曲线。

**地图飞入 (Map Fly-to)**：从详情页返回地图时，视角从当前位置平滑飞行至目标位置。飞行路径采用弧线设计，持续时间根据距离动态调整（500ms-2000ms）。

**视差滚动 (Parallax Scrolling)**：行程列表页面在滚动时，背景地图以 0.3x 速度产生视差效果。顶部搜索区域在滚动超过 100px 后收缩为固定顶部栏，提供快速搜索入口。

---

<div id="results"></div>

## 结果与反思


### 核心数据指标

- **行程规划时间**：从传统的 3-5 天缩短至 30 分钟，效率提升 98%
- **用户留存率**：次月留存率 68%，较同类产品提升 45%
- **旅行完成率**：用户规划的行程中 92% 最终被执行，远超行业平均的 60%
- **App Store 评分**：上线 3 个月稳定在 4.9/5 分，差评率低于 1%

### 设计成果

1. **AI 与人工的平衡点**：成功找到"AI 建议 + 用户微调"的最佳交互模式，用户满意度达 94%。关键在于给予用户足够的控制感，同时让 AI 真正解决信息碎片化的问题。

2. **离线体验的突破**：TripWise 是首款提供完整离线体验的旅行规划应用。通过智能预缓存策略，用户在无网络环境下仍可访问完整行程、地图和导航功能，这一特性获得了多家科技媒体的好评。

3. **社交分享的差异化**：AI 自动生成的旅行日记功能成为用户最喜爱的特性之一，日均生成 12 万篇图文内容，社交平台分享转化率 34%。

### 经验教训

1. **AI 的可解释性至关重要**：早期版本中，AI 推荐理由不够透明，导致用户信任度低。后续版本增加了"为什么推荐这个"的解释卡片，用户对 AI 建议的采纳率提升了 62%。

2. **离线优先的设计思维**：将离线功能作为核心特性而非附属功能来设计，从根本上改变了信息架构和技术选型。这一决策虽然增加了开发成本，但最终成为产品的核心竞争力。

3. **情感化设计的价值**：在功能性之外，TripWise 注重旅行的情感体验——倒计时提醒、旅行日记自动生成、里程碑成就系统等情感化设计，显著提升了用户粘性和口碑传播。
