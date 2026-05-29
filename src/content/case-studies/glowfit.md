---
title:
  zh: "GlowFit — 让每一次运动都有意义"
  en: "GlowFit — Every Workout Counts"
subtitle:
  zh: "一款融合游戏化激励机制的智能健身追踪应用"
  en: "A Smart Fitness Tracking App with Gamified Motivation"
cover: "/images/projects/placeholder-cover.svg"
role:
  zh: "UI/UX 设计师 · 产品设计师"
  en: "UI/UX Designer · Product Designer"
timeline: "2025.03 — 2025.08"
tags: ["UI设计", "UX研究", "移动应用", "游戏化", "健身", "Figma"]
order: 1
metrics:
  - label:
      zh: "用户运动频率"
      en: "Workout Frequency"
    value: "+55%"
  - label:
      zh: "30天留存率"
      en: "30-day Retention"
    value: "30% → 68%"
  - label:
      zh: "社交挑战参与"
      en: "Challenge Participation"
    value: "78%"
  - label:
      zh: "日均使用时长"
      en: "Daily Usage"
    value: "8 min"
---

<div id="background"></div>

## 项目背景


### 问题背景

健身应用市场已经趋于饱和，但一个令人困惑的现象始终存在：**80% 的用户在下载应用两周内就选择放弃**。根据 Sensor Tower 的行业报告，健身类应用的平均 30 天留存率仅为 29%，远低于社交类应用的 45% 和工具类应用的 52%。

核心问题并非用户不想运动，而是**现有应用无法提供持续的运动动机**。传统的健身追踪器只是机械地记录数据——步数、卡路里、距离——但这些冰冷的数字无法激发用户的情感连接。用户打开应用看到的是一堆数字报表，而不是令人振奋的成就和进步。

我们需要重新思考：如何让健身从"必须做的事"变成"想做的事"？

### 用户画像

通过对目标用户群体的深入调研，我们定义了三类核心用户画像：

**画像一：入门引导者（小林，24岁，办公室职员）**
- 健身新手，不知道如何开始
- 尝试过下载多个健身应用，但都因为"不知道练什么"而放弃
- 需要清晰的引导路径和即时的正反馈
- 核心诉求：降低运动的认知门槛

**画像二：数据驱动者（老张，32岁，产品经理）**
- 有一定健身基础，关注训练数据和进步曲线
- 使用 Apple Watch 记录运动，但缺少深度数据分析
- 希望看到长期趋势和个性化建议
- 核心诉求：数据可视化与智能分析

**画像三：社交竞争者（阿瑶，28岁，市场营销）**
- 热衷于社交分享，喜欢和朋友比较运动成绩
- 参加过多次线上跑步挑战，享受排行榜带来的成就感
- 希望运动能融入社交生活，而不仅仅是个人行为
- 核心诉求：社交激励与团队归属感

### 商业目标

GlowFit 的商业目标是通过**社交竞争机制**和**游戏化奖励系统**，将健身从一项孤立的个人行为转变为富有社交属性的集体活动。具体指标包括：

- 将 30 天用户留存率从行业平均的 30% 提升至 60% 以上
- 建立用户间的社交连接网络，提升应用的社交属性
- 通过游戏化机制增加用户日均使用时长
- 构建可穿戴设备生态，实现数据互通

---

<div id="research"></div>

## 用户研究


### 用户洞察

通过 42 次深度用户访谈、3 次焦点小组讨论和 1200 份在线问卷调查，我们提炼出五个关键用户洞察：

**洞察一：运动动机的"社交放大器"效应**
超过 73% 的受访者表示，当有朋友一起运动或知道朋友在看自己的运动数据时，运动坚持率显著提高。社交压力在健身场景中不是负担，而是动力。

**洞察二：成就感比数据本身更重要**
用户并不真正关心今天走了多少步，他们关心的是"这意味着什么"。将步数转化为"燃烧了相当于一个汉堡的热量"或"相当于爬了 15 层楼"，用户的理解度和情感连接提升了 4 倍。

**洞察三：视觉反馈需要"仪式感"**
简单的数字变化无法激发情感。用户期望看到动画效果、庆祝特效和视觉奖励。67% 的受访者表示，完成目标时的视觉庆祝效果会让他们"感觉很棒"，并更愿意继续使用应用。

**洞察四：个性化推荐的"恰到好处"原则**
过于复杂的个性化推荐反而会让用户感到困惑。用户需要的是"基于我今天的状态，现在最适合做什么"，而不是"这里有 200 个适合你的训练计划"。简单、直接、即时的建议最受欢迎。

**洞察五：可穿戴设备的"数据孤岛"问题**
62% 的可穿戴设备用户反映，不同设备之间的数据无法互通，导致运动记录碎片化。用户期望一个统一的数据中心，整合所有设备的运动数据。

### 竞品分析

我们对市场上三款主流健身应用进行了深度分析，从游戏化机制、社交功能、AI 教练和可穿戴设备集成四个维度进行对比：

| 维度 | Strava | Nike Training Club | Fitbit | GlowFit（目标） |
|------|--------|-------------------|--------|-----------------|
| 游戏化 | 基础徽章系统 | 无 | 有限挑战 | 深度成就树 + 等级系统 |
| 社交功能 | 强（圈子、赛段） | 弱（仅分享） | 中等（小组） | 强（挑战 + 实时排行） |
| AI 教练 | 无 | 有（训练计划） | 有限建议 | 智能教练 + 情境推荐 |
| 可穿戴集成 | 广泛 | 有限 | 深度（自有设备） | 全平台开放集成 |
| 数据可视化 | 中等 | 基础 | 中等 | 强（环形图 + 趋势） |
| 激励机制 | 社交认可 | 品牌归属 | 积分兑换 | 社交 + 成就 + 视觉奖励 |

通过竞品分析，我们发现了明确的差异化机会：**将社交竞争、深度游戏化和智能推荐三者有机融合**，而非像竞品那样各自为政。

### 痛点总结

基于用户研究和竞品分析，我们识别出三大核心痛点：

1. **动机缺失**：运动本身缺乏即时正反馈，用户难以形成习惯回路
2. **数据枯燥**：运动数据以原始数字呈现，缺乏情感化包装和故事性叙述
3. **社交断裂**：运动是孤独的行为，缺乏有效的社交连接和 accountability 机制

---

<div id="architecture"></div>

## 信息架构



GlowFit 的信息架构围绕四个核心功能模块构建，采用底部标签导航加中心快捷操作按钮的布局模式：

**标签一：今日（Today）**
- 每日运动目标环形进度（步数、卡路里、活跃分钟）
- 今日运动摘要与快速入口
- 每日运动小贴士与激励语
- 可穿戴设备同步状态

**标签二：活动（Activity）**
- 运动历史时间线
- 单次运动详情（地图轨迹、心率曲线、配速分析）
- 运动类型分类与筛选
- 个人最佳记录展示

**标签三：挑战（Challenges）**
- 进行中的挑战列表与进度
- 好友排行榜
- 全球挑战赛入口
- 挑战创建与邀请

**标签四：个人（Profile）**
- 成就墙与徽章收藏
- 个人等级与经验值
- 运动统计趋势
- 设置与设备管理

**中心按钮：快速记录**
- 一键开启运动记录
- 支持跑步、骑行、力量训练、瑜伽等类型
- 快速手动输入（步数、饮水量等）

### 用户流程

核心用户流程设计遵循"最小阻力路径"原则：

```
打开应用 → 查看今日目标进度 → 完成/记录运动 → 更新进度环 →
加入/参与挑战 → 查看排行榜 → 获得成就 → 分享到社交平台
```

关键设计决策：
- 首页即仪表盘，用户打开应用 3 秒内即可了解今日状态
- 快速记录按钮始终可见，降低运动记录的操作成本
- 挑战和成就系统形成闭环：运动 → 积分 → 排名 → 成就 → 更多运动

---

<div id="wireframe"></div>

## 线框图


### 线框图设计

基于信息架构，我们设计了三组核心页面的线框图，验证交互流程和布局合理性。

**页面一：今日概览**

线框图展示了首页的核心布局：顶部区域放置环形进度组件，三个同心圆分别代表步数、卡路里和活跃分钟数。中部区域为每日运动摘要卡片，包含最近一次运动记录和今日小贴士。底部为快捷操作区域，中心的圆形按钮为运动记录入口。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="p-4">
<div class="text-[10px] text-gray-400 mb-1">2025年6月12日 · 周四</div>
<div class="h-4 bg-gray-300 rounded w-20 mb-4"></div>
<div class="flex justify-center mb-4">
<div class="relative w-32 h-32">
<div class="absolute inset-0 rounded-full border-[6px] border-gray-200"></div>
<div class="absolute inset-2 rounded-full border-[6px] border-gray-300 border-t-transparent rotate-45"></div>
<div class="absolute inset-4 rounded-full border-[6px] border-gray-200"></div>
<div class="absolute inset-0 flex items-center justify-center flex-col">
<div class="h-5 bg-gray-300 rounded w-12 mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-8"></div>
</div>
</div>
</div>
<div class="grid grid-cols-3 gap-2 mb-4">
<div class="text-center"><div class="h-3 bg-gray-200 rounded w-8 mx-auto mb-1"></div><div class="h-2 bg-gray-100 rounded w-6 mx-auto"></div></div>
<div class="text-center"><div class="h-3 bg-gray-200 rounded w-8 mx-auto mb-1"></div><div class="h-2 bg-gray-100 rounded w-6 mx-auto"></div></div>
<div class="text-center"><div class="h-3 bg-gray-200 rounded w-8 mx-auto mb-1"></div><div class="h-2 bg-gray-100 rounded w-6 mx-auto"></div></div>
</div>
<div class="bg-gray-50 rounded-xl border border-gray-200 p-3">
<div class="h-3 bg-gray-200 rounded w-1/3 mb-2"></div>
<div class="h-2 bg-gray-100 rounded w-full mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-2/3"></div>
</div>
</div>
<div class="h-14 border-t border-gray-200 flex items-center justify-around">
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-10 h-10 bg-gray-300 rounded-full"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
</div>
</div>

**页面二：活动详情**

线框图展示了单次运动的完整数据视图：顶部为运动类型和时间信息，中部为地图轨迹区域（支持 3D 视角切换），下方依次为心率曲线图、配速分析图和核心数据网格（距离、时间、配速、卡路里）。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="p-3">
<div class="flex items-center gap-2 mb-2">
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="h-3 bg-gray-300 rounded w-24"></div>
</div>
<div class="h-32 bg-gray-100 rounded-xl mb-3 relative overflow-hidden">
<svg class="absolute inset-0 w-full h-full" viewBox="0 0 300 128">
<polyline points="20,100 60,80 100,90 140,60 180,70 220,40 260,50 290,30" fill="none" stroke="#9ca3af" stroke-width="2"/>
</svg>
</div>
<div class="h-20 bg-gray-50 rounded-xl border border-gray-200 p-2 mb-3">
<div class="h-2 bg-gray-200 rounded w-16 mb-2"></div>
<svg class="w-full h-10" viewBox="0 0 260 40">
<polyline points="0,30 30,25 60,20 90,28 120,15 150,22 180,10 210,18 240,12 260,20" fill="none" stroke="#d1d5db" stroke-width="1.5"/>
</svg>
</div>
<div class="grid grid-cols-2 gap-2">
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="h-4 bg-gray-300 rounded w-12 mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-8 mx-auto"></div>
</div>
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="h-4 bg-gray-300 rounded w-12 mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-8 mx-auto"></div>
</div>
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="h-4 bg-gray-300 rounded w-12 mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-8 mx-auto"></div>
</div>
<div class="bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="h-4 bg-gray-300 rounded w-12 mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-8 mx-auto"></div>
</div>
</div>
</div>
</div>

**页面三：挑战看板**

线框图展示了社交挑战的核心界面：顶部为进行中挑战列表，每个挑战卡片包含参与好友头像、目标进度条和剩余时间。中部为好友排行榜，展示本周运动积分排名。底部为挑战发现区域，推荐适合用户的新挑战。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="p-3 space-y-3">
<div class="h-4 bg-gray-300 rounded w-24 mb-2"></div>
<div class="bg-gray-50 rounded-xl border border-gray-200 p-3">
<div class="flex items-center gap-2 mb-2">
<div class="flex -space-x-1">
<div class="w-5 h-5 bg-gray-300 rounded-full border border-white"></div>
<div class="w-5 h-5 bg-gray-200 rounded-full border border-white"></div>
<div class="w-5 h-5 bg-gray-200 rounded-full border border-white"></div>
</div>
<div class="h-2 bg-gray-200 rounded w-16 ml-auto"></div>
</div>
<div class="h-2 bg-gray-200 rounded-full mb-1">
<div class="h-2 bg-gray-300 rounded-full w-2/3"></div>
</div>
<div class="h-2 bg-gray-100 rounded w-12"></div>
</div>
<div class="bg-gray-50 rounded-xl border border-gray-200 p-3">
<div class="flex items-center gap-2 mb-2">
<div class="flex -space-x-1">
<div class="w-5 h-5 bg-gray-200 rounded-full border border-white"></div>
<div class="w-5 h-5 bg-gray-300 rounded-full border border-white"></div>
</div>
<div class="h-2 bg-gray-200 rounded w-20 ml-auto"></div>
</div>
<div class="h-2 bg-gray-200 rounded-full mb-1">
<div class="h-2 bg-gray-300 rounded-full w-1/2"></div>
</div>
<div class="h-2 bg-gray-100 rounded w-12"></div>
</div>
<div class="h-4 bg-gray-300 rounded w-20 mt-2"></div>
<div class="flex gap-2">
<div class="flex-1 bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="w-8 h-8 bg-gray-200 rounded-full mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-12 mx-auto"></div>
</div>
<div class="flex-1 bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="w-8 h-8 bg-gray-200 rounded-full mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-12 mx-auto"></div>
</div>
<div class="flex-1 bg-gray-50 rounded-lg border border-gray-200 p-2 text-center">
<div class="w-8 h-8 bg-gray-200 rounded-full mx-auto mb-1"></div>
<div class="h-2 bg-gray-200 rounded w-12 mx-auto"></div>
</div>
</div>
</div>
</div>

---

<div id="visual"></div>

## 视觉设计


### 设计理念："Every Step Counts"

GlowFit 的视觉设计围绕"每一步都算数"的核心理念展开。我们希望用户在每一次使用应用时都能感受到运动的价值和进步的喜悦。视觉语言需要同时传递**活力**（运动的能量感）和**温暖**（陪伴与鼓励）。

### 色彩系统

**主色：活力橙红**
- 主色调 `#F97316`（Orange-500）：代表运动的热情与活力，用于核心操作按钮和重点信息
- 辅助色 `#EF4444`（Red-500）：代表挑战与突破，用于成就系统和重要提示
- 渐变组合：`linear-gradient(135deg, #F97316, #EF4444)` 用于品牌标识和关键视觉元素

**功能色：**
- 成功绿 `#22C55E`：运动完成、目标达成、健康指标正常
- 能量黄 `#EAB308`：经验值、积分、进行中状态
- 信息蓝 `#3B82F6`：数据图表、统计信息
- 警告红 `#EF4444`：高强度心率、异常提醒

**中性色：**
- 背景灰 `#F9FAFB`：页面背景
- 卡片白 `#FFFFFF`：卡片和浮层
- 文字深 `#111827`：主要文字
- 文字中 `#6B7280`：次要信息
- 分割线 `#E5E7EB`：内容分隔

### 字体系统

采用思源黑体（Noto Sans SC）作为中文主字体，Inter 作为英文和数字字体。字体层级清晰，确保运动场景下的快速可读性：

- 页面标题：24px / Semi Bold
- 卡片标题：18px / Medium
- 正文内容：14px / Regular
- 辅助说明：12px / Regular
- 数据大字：32px / Bold（用于运动数据展示）

### 图标体系

采用线性图标风格，线条粗细统一为 1.5px，圆角处理与品牌调性保持一致。运动类型图标采用填充式设计，确保在小尺寸下依然清晰可辨。图标库基于 Lucide Icons 定制，增加了运动专属图标（哑铃、跑鞋、瑜伽垫等）。

---

<div id="high-fidelity"></div>

## 高保真设计


### 高保真原型设计

以下为四组核心页面的高保真原型，使用 Tailwind CSS 实现，展示真实的视觉效果和交互细节。

### 屏幕一：今日概览

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-12 bg-gradient-to-r from-orange-500 to-red-500 flex items-end px-5 pb-2">
<span class="text-white text-xs font-medium">9:41</span>
</div>
<div class="p-5">
<div class="flex items-center justify-between mb-4">
<div>
<p class="text-gray-500 text-xs">2025年6月12日 · 周四</p>
<h2 class="text-lg font-semibold text-gray-900">今日目标</h2>
</div>
<div class="w-10 h-10 rounded-full bg-gradient-to-br from-orange-400 to-red-500 flex items-center justify-center">
<svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"/></svg>
</div>
</div>

<div class="flex justify-center items-center my-6">
<div class="relative w-48 h-48">
<svg class="w-48 h-48 -rotate-90" viewBox="0 0 192 192">
<circle cx="96" cy="96" r="82" fill="none" stroke="#F3F4F6" stroke-width="12"/>
<circle cx="96" cy="96" r="82" fill="none" stroke="url(#grad-steps)" stroke-width="12" stroke-linecap="round" stroke-dasharray="515" stroke-dashoffset="180"/>
<circle cx="96" cy="96" r="66" fill="none" stroke="#F3F4F6" stroke-width="10"/>
<circle cx="96" cy="96" r="66" fill="none" stroke="#22C55E" stroke-width="10" stroke-linecap="round" stroke-dasharray="415" stroke-dashoffset="100"/>
<circle cx="96" cy="96" r="52" fill="none" stroke="#F3F4F6" stroke-width="8"/>
<circle cx="96" cy="96" r="52" fill="none" stroke="#EAB308" stroke-width="8" stroke-linecap="round" stroke-dasharray="327" stroke-dashoffset="65"/>
<defs>
<linearGradient id="grad-steps" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#F97316"/>
<stop offset="100%" stop-color="#EF4444"/>
</linearGradient>
</defs>
</svg>
<div class="absolute inset-0 flex flex-col items-center justify-center">
<span class="text-3xl font-bold text-gray-900">7,246</span>
<span class="text-xs text-gray-500">/ 10,000 步</span>
</div>
</div>
</div>

<div class="flex justify-around text-center mb-5">
<div>
<div class="w-3 h-3 rounded-full bg-gradient-to-r from-orange-500 to-red-500 mx-auto mb-1"></div>
<p class="text-sm font-semibold text-gray-900">386</p>
<p class="text-[10px] text-gray-500">千卡</p>
</div>
<div>
<div class="w-3 h-3 rounded-full bg-green-500 mx-auto mb-1"></div>
<p class="text-sm font-semibold text-gray-900">42</p>
<p class="text-[10px] text-gray-500">分钟</p>
</div>
<div>
<div class="w-3 h-3 rounded-full bg-yellow-500 mx-auto mb-1"></div>
<p class="text-sm font-semibold text-gray-900">5.2</p>
<p class="text-[10px] text-gray-500">公里</p>
</div>
</div>

<div class="bg-orange-50 rounded-xl p-3 mb-4">
<div class="flex items-start gap-2">
<div class="w-8 h-8 rounded-lg bg-orange-100 flex items-center justify-center flex-shrink-0">
<svg class="w-4 h-4 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
</div>
<div>
<p class="text-xs font-medium text-orange-800">今日建议</p>
<p class="text-[11px] text-orange-600">再走 2,754 步即可完成目标！晚饭后散步是个好选择。</p>
</div>
</div>
</div>

<button class="w-full py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white text-sm font-semibold rounded-xl shadow-lg shadow-orange-500/30 active:scale-95 transition-transform">
+ 记录运动
</button>
</div>
<div class="h-14 border-t border-gray-100 flex items-center justify-around px-4">
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-full bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/></svg>
</div>
<span class="text-[10px] font-medium text-orange-500">今日</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
<span class="text-[10px] text-gray-400">活动</span>
</div>
<div class="w-12 h-12 -mt-4 rounded-full bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center shadow-lg shadow-orange-500/40">
<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
<span class="text-[10px] text-gray-400">挑战</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
<span class="text-[10px] text-gray-400">我的</span>
</div>
</div>
</div>

### 屏幕二：活动详情

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-12 bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-between px-5">
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
<span class="text-white text-xs font-medium">运动详情</span>
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
</div>

<div class="h-40 bg-gradient-to-b from-orange-100 to-green-50 relative overflow-hidden">
<div class="absolute inset-0 flex items-center justify-center">
<svg class="w-full h-full opacity-30" viewBox="0 0 320 160">
<path d="M20 120 Q60 80 100 100 T180 60 T260 90 T300 40" fill="none" stroke="#F97316" stroke-width="3" stroke-dasharray="600" stroke-dashoffset="200"/>
<circle cx="20" cy="120" r="6" fill="#22C55E"/>
<circle cx="300" cy="40" r="6" fill="#EF4444"/>
<text x="12" y="140" font-size="10" fill="#6B7280">起点</text>
<text x="280" y="35" font-size="10" fill="#6B7280">终点</text>
</svg>
</div>
<div class="absolute top-3 left-3 bg-white/90 backdrop-blur rounded-lg px-2 py-1">
<span class="text-[10px] font-medium text-gray-700">户外跑步</span>
</div>
<div class="absolute top-3 right-3 bg-white/90 backdrop-blur rounded-lg px-2 py-1">
<span class="text-[10px] font-medium text-green-600">5.2 km</span>
</div>
</div>

<div class="p-4">
<div class="grid grid-cols-2 gap-3 mb-4">
<div class="bg-gray-50 rounded-xl p-3 text-center">
<p class="text-2xl font-bold text-gray-900">28:34</p>
<p class="text-[10px] text-gray-500">总时长</p>
</div>
<div class="bg-gray-50 rounded-xl p-3 text-center">
<p class="text-2xl font-bold text-orange-500">5'29"</p>
<p class="text-[10px] text-gray-500">平均配速 /公里</p>
</div>
<div class="bg-gray-50 rounded-xl p-3 text-center">
<p class="text-2xl font-bold text-red-500">156</p>
<p class="text-[10px] text-gray-500">平均心率 BPM</p>
</div>
<div class="bg-gray-50 rounded-xl p-3 text-center">
<p class="text-2xl font-bold text-yellow-500">386</p>
<p class="text-[10px] text-gray-500">消耗千卡</p>
</div>
</div>

<div class="mb-4">
<div class="flex items-center justify-between mb-2">
<span class="text-xs font-medium text-gray-700">心率曲线</span>
<span class="text-[10px] text-gray-400">平均 156 BPM</span>
</div>
<div class="bg-gray-50 rounded-xl p-3 h-24">
<svg class="w-full h-full" viewBox="0 0 280 80">
<defs>
<linearGradient id="hr-grad" x1="0%" y1="0%" x2="0%" y2="100%">
<stop offset="0%" stop-color="#EF4444" stop-opacity="0.3"/>
<stop offset="100%" stop-color="#EF4444" stop-opacity="0"/>
</linearGradient>
</defs>
<path d="M0 60 Q20 55 40 50 T80 45 T120 35 T160 30 T200 25 T240 30 T280 35" fill="none" stroke="#EF4444" stroke-width="2"/>
<path d="M0 60 Q20 55 40 50 T80 45 T120 35 T160 30 T200 25 T240 30 T280 35 L280 80 L0 80 Z" fill="url(#hr-grad)"/>
<line x1="0" y1="50" x2="280" y2="50" stroke="#E5E7EB" stroke-width="1" stroke-dasharray="4"/>
<line x1="0" y1="30" x2="280" y2="30" stroke="#E5E7EB" stroke-width="1" stroke-dasharray="4"/>
<text x="0" y="68" font-size="8" fill="#9CA3AF">120</text>
<text x="0" y="48" font-size="8" fill="#9CA3AF">160</text>
<text x="0" y="28" font-size="8" fill="#9CA3AF">190</text>
</svg>
</div>
</div>

<div class="flex gap-2">
<button class="flex-1 py-2.5 bg-gradient-to-r from-orange-500 to-red-500 text-white text-xs font-semibold rounded-xl">分享成绩</button>
<button class="flex-1 py-2.5 bg-gray-100 text-gray-700 text-xs font-semibold rounded-xl">保存记录</button>
</div>
</div>
</div>

### 屏幕三：挑战看板

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-12 bg-gradient-to-r from-orange-500 to-red-500 flex items-end px-5 pb-2">
<span class="text-white text-xs font-medium">9:41</span>
</div>
<div class="p-5">
<div class="flex items-center justify-between mb-4">
<h2 class="text-lg font-semibold text-gray-900">挑战中心</h2>
<button class="px-3 py-1 bg-orange-100 text-orange-600 text-[11px] font-medium rounded-full">+ 创建</button>
</div>

<div class="space-y-3 mb-5">
<div class="bg-gradient-to-r from-orange-50 to-red-50 rounded-xl p-3 border border-orange-100">
<div class="flex items-center justify-between mb-2">
<div>
<p class="text-sm font-semibold text-gray-900">本周万步挑战</p>
<p class="text-[10px] text-gray-500">剩余 3 天</p>
</div>
<div class="flex -space-x-2">
<div class="w-7 h-7 rounded-full bg-blue-400 border-2 border-white flex items-center justify-center text-[9px] text-white font-medium">林</div>
<div class="w-7 h-7 rounded-full bg-green-400 border-2 border-white flex items-center justify-center text-[9px] text-white font-medium">张</div>
<div class="w-7 h-7 rounded-full bg-purple-400 border-2 border-white flex items-center justify-center text-[9px] text-white font-medium">瑶</div>
<div class="w-7 h-7 rounded-full bg-gray-200 border-2 border-white flex items-center justify-center text-[9px] text-gray-500 font-medium">+2</div>
</div>
</div>
<div class="flex items-center gap-2">
<div class="flex-1 h-2 bg-white rounded-full overflow-hidden">
<div class="h-full bg-gradient-to-r from-orange-500 to-red-500 rounded-full" style="width: 72%"></div>
</div>
<span class="text-[10px] font-medium text-orange-600">72%</span>
</div>
</div>

<div class="bg-gray-50 rounded-xl p-3">
<div class="flex items-center justify-between mb-2">
<div>
<p class="text-sm font-semibold text-gray-900">月度骑行赛</p>
<p class="text-[10px] text-gray-500">剩余 18 天</p>
</div>
<div class="flex -space-x-2">
<div class="w-7 h-7 rounded-full bg-yellow-400 border-2 border-white flex items-center justify-center text-[9px] text-white font-medium">王</div>
<div class="w-7 h-7 rounded-full bg-pink-400 border-2 border-white flex items-center justify-center text-[9px] text-white font-medium">李</div>
</div>
</div>
<div class="flex items-center gap-2">
<div class="flex-1 h-2 bg-gray-200 rounded-full overflow-hidden">
<div class="h-full bg-yellow-500 rounded-full" style="width: 34%"></div>
</div>
<span class="text-[10px] font-medium text-yellow-600">34%</span>
</div>
</div>
</div>

<div class="mb-4">
<div class="flex items-center justify-between mb-3">
<h3 class="text-sm font-semibold text-gray-900">本周排行</h3>
<span class="text-[10px] text-gray-400">按运动积分</span>
</div>
<div class="space-y-2">
<div class="flex items-center gap-3 bg-yellow-50 rounded-xl p-2.5">
<div class="w-6 h-6 rounded-full bg-yellow-400 flex items-center justify-center text-[10px] text-white font-bold">1</div>
<div class="w-8 h-8 rounded-full bg-gradient-to-br from-orange-400 to-red-500 flex items-center justify-center text-[10px] text-white font-medium">我</div>
<div class="flex-1">
<p class="text-xs font-medium text-gray-900">我</p>
<p class="text-[10px] text-gray-500">运动 12 次</p>
</div>
<span class="text-sm font-bold text-orange-500">2,480</span>
</div>
<div class="flex items-center gap-3 bg-gray-50 rounded-xl p-2.5">
<div class="w-6 h-6 rounded-full bg-gray-300 flex items-center justify-center text-[10px] text-white font-bold">2</div>
<div class="w-8 h-8 rounded-full bg-blue-400 flex items-center justify-center text-[10px] text-white font-medium">林</div>
<div class="flex-1">
<p class="text-xs font-medium text-gray-900">小林</p>
<p class="text-[10px] text-gray-500">运动 10 次</p>
</div>
<span class="text-sm font-bold text-gray-600">2,150</span>
</div>
<div class="flex items-center gap-3 bg-gray-50 rounded-xl p-2.5">
<div class="w-6 h-6 rounded-full bg-orange-300 flex items-center justify-center text-[10px] text-white font-bold">3</div>
<div class="w-8 h-8 rounded-full bg-green-400 flex items-center justify-center text-[10px] text-white font-medium">张</div>
<div class="flex-1">
<p class="text-xs font-medium text-gray-900">老张</p>
<p class="text-[10px] text-gray-500">运动 9 次</p>
</div>
<span class="text-sm font-bold text-gray-600">1,920</span>
</div>
</div>
</div>

<button class="w-full py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white text-sm font-semibold rounded-xl shadow-lg shadow-orange-500/30 active:scale-95 transition-transform">
发现更多挑战
</button>
</div>
<div class="h-14 border-t border-gray-100 flex items-center justify-around px-4">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/></svg>
<span class="text-[10px] text-gray-400">今日</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
<span class="text-[10px] text-gray-400">活动</span>
</div>
<div class="w-12 h-12 -mt-4 rounded-full bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center shadow-lg shadow-orange-500/40">
<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-full bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
</div>
<span class="text-[10px] font-medium text-orange-500">挑战</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
<span class="text-[10px] text-gray-400">我的</span>
</div>
</div>
</div>

### 屏幕四：成就墙

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="h-12 bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-between px-5">
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
<span class="text-white text-xs font-medium">成就墙</span>
<div class="w-5"></div>
</div>
<div class="p-5">
<div class="bg-gradient-to-r from-orange-500 to-red-500 rounded-2xl p-4 mb-5 text-white relative overflow-hidden">
<div class="absolute top-0 right-0 w-20 h-20 bg-white/10 rounded-full -mr-6 -mt-6"></div>
<div class="absolute bottom-0 right-8 w-12 h-12 bg-white/10 rounded-full -mb-4"></div>
<p class="text-xs opacity-80 mb-1">当前等级</p>
<div class="flex items-center gap-2 mb-2">
<span class="text-3xl font-bold">Lv.12</span>
<span class="text-xs opacity-80">运动达人</span>
</div>
<div class="flex items-center gap-2">
<div class="flex-1 h-1.5 bg-white/20 rounded-full overflow-hidden">
<div class="h-full bg-white rounded-full" style="width: 68%"></div>
</div>
<span class="text-[10px] opacity-80">6,800 / 10,000 XP</span>
</div>
</div>

<div class="mb-4">
<h3 class="text-sm font-semibold text-gray-900 mb-3">最近解锁</h3>
<div class="flex gap-3 overflow-x-auto pb-2">
<div class="flex-shrink-0 w-20 text-center">
<div class="w-14 h-14 mx-auto rounded-2xl bg-gradient-to-br from-yellow-400 to-orange-500 flex items-center justify-center mb-1 shadow-lg shadow-orange-500/30">
<svg class="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
</div>
<p class="text-[10px] font-medium text-gray-900">七日之星</p>
<p class="text-[9px] text-gray-400">连续7天</p>
</div>
<div class="flex-shrink-0 w-20 text-center">
<div class="w-14 h-14 mx-auto rounded-2xl bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center mb-1 shadow-lg shadow-green-500/30">
<svg class="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
</div>
<p class="text-[10px] font-medium text-gray-900">挑战先锋</p>
<p class="text-[9px] text-gray-400">赢得5场</p>
</div>
<div class="flex-shrink-0 w-20 text-center">
<div class="w-14 h-14 mx-auto rounded-2xl bg-gradient-to-br from-blue-400 to-indigo-500 flex items-center justify-center mb-1 shadow-lg shadow-blue-500/30">
<svg class="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zm1 11H9v-2h2v2zm0-4H9V5h2v4z"/></svg>
</div>
<p class="text-[10px] font-medium text-gray-900">万步达人</p>
<p class="text-[9px] text-gray-400">单日万步</p>
</div>
</div>
</div>

<div>
<h3 class="text-sm font-semibold text-gray-900 mb-3">徽章收藏</h3>
<div class="grid grid-cols-4 gap-3">
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-orange-400 to-red-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 2a2 2 0 00-2 2v14l3.5-2 3.5 2 3.5-2 3.5 2V4a2 2 0 00-2-2H5zm4.707 3.707a1 1 0 00-1.414-1.414l-3 3a1 1 0 000 1.414l3 3a1 1 0 001.414-1.414L8.414 9H10a3 3 0 013 3v1a1 1 0 102 0v-1a5 5 0 00-5-5H8.414l1.293-1.293z" clip-rule="evenodd"/></svg>
</div>
<p class="text-[9px] text-gray-600">初次跑步</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-yellow-400 to-orange-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
</div>
<p class="text-[9px] text-gray-600">五星战士</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0c.49.4 1.102.647 1.745.723a3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
</div>
<p class="text-[9px] text-gray-600">挑战先锋</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-purple-400 to-pink-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zm1 11H9v-2h2v2zm0-4H9V5h2v4z"/></svg>
</div>
<p class="text-[9px] text-gray-600">万步达人</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-blue-400 to-cyan-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"/></svg>
</div>
<p class="text-[9px] text-gray-600">铁人三项</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-red-400 to-rose-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"/></svg>
</div>
<p class="text-[9px] text-gray-600">燃脂之王</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gradient-to-br from-indigo-400 to-violet-500 flex items-center justify-center mb-1">
<svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a8 8 0 100 16 8 8 0 000-16zm1 11H9v-2h2v2zm0-4H9V5h2v4z"/></svg>
</div>
<p class="text-[9px] text-gray-600">早起鸟</p>
</div>
<div class="text-center">
<div class="w-12 h-12 mx-auto rounded-xl bg-gray-100 flex items-center justify-center mb-1 border-2 border-dashed border-gray-300">
<svg class="w-5 h-5 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/></svg>
</div>
<p class="text-[9px] text-gray-400">未解锁</p>
</div>
</div>
</div>
</div>
<div class="h-14 border-t border-gray-100 flex items-center justify-around px-4">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/></svg>
<span class="text-[10px] text-gray-400">今日</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
<span class="text-[10px] text-gray-400">活动</span>
</div>
<div class="w-12 h-12 -mt-4 rounded-full bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center shadow-lg shadow-orange-500/40">
<svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
<span class="text-[10px] text-gray-400">挑战</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-full bg-gradient-to-r from-orange-500 to-red-500 flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
</div>
<span class="text-[10px] font-medium text-orange-500">我的</span>
</div>
</div>
</div>

---

<div id="interaction"></div>

## 交互设计


### 交互动效设计

GlowFit 的交互设计围绕"即时反馈"和"情感连接"两个核心原则展开。每一个交互细节都经过精心设计，确保用户在使用过程中始终感受到运动的乐趣和成就的喜悦。

**进度环动效**

进度环是 GlowFit 最核心的视觉元素，其动效设计分为三个阶段：

1. **加载动画**：应用启动时，三个进度环以交错方式从零开始填充，耗时约 1.2 秒。外环（步数）最先启动，中环（卡路里）延迟 0.15 秒，内环（活跃分钟）延迟 0.3 秒。填充曲线采用 ease-out 缓动函数，模拟"能量注入"的视觉感受。

2. **实时更新**：当用户记录新的运动数据时，对应进度环会产生"脉冲"效果——环形在完成填充后轻微放大 5% 再回弹，同时伴随 0.3 秒的色彩闪烁。这种微交互让用户明确感知到数据的变化。

3. **目标达成**：当某个环形达到 100% 时，触发庆祝动画——环形产生波纹扩散效果，同时屏幕上方飘落彩色粒子（持续 2 秒）。如果三个环形全部完成，整个进度环区域会产生"发光"效果，配合设备的触觉反馈（轻震两次）。

**挑战排行榜动效**

- **实时更新**：当好友的积分发生变化时，排行榜会以"滑入"动画更新位置变化，旧位置的卡片向下/上滑动，新位置的卡片从侧面滑入
- **超越提示**：当用户的排名超过好友时，两者之间会出现一道橙色光弧，持续 1.5 秒后消散
- **成就解锁**：获得新成就时，排行榜顶部会弹出庆祝横幅，伴随撒花动画和设备震动

**活动记录交互**

- **滑动切换**：活动详情页支持左右滑动切换不同的运动类型（跑步、骑行、力量训练），切换时卡片带有 3D 透视旋转效果
- **数据卡片**：长按任意数据卡片会触发"放大"效果，显示更详细的数据解读
- **地图交互**：地图轨迹支持双指缩放和拖拽，轨迹线会根据配速自动变色（绿色=慢速，黄色=中速，红色=快速）
- **心率曲线**：双指拖动可在曲线上查看具体时间点的心率值，同时地图上对应的轨迹位置会高亮显示

**触觉反馈设计**

GlowFit 深度集成了设备的触觉反馈引擎，为关键操作提供物理层面的确认感：

- 运动记录开始/结束：双短震
- 目标达成：长震 + 短震
- 好友挑战邀请：三连短震
- 成就解锁：渐强三震

---

<div id="results"></div>

## 结果与反思


### 项目成果

GlowFit 项目历时 6 个月，从用户研究到高保真原型交付，最终成果超出预期目标。

**核心数据指标**

| 指标 | 目标值 | 实际值 | 变化 |
|------|--------|--------|------|
| 用户运动频率 | +40% | +55% | 超目标 37.5% |
| 30 天留存率 | 50% | 68% | 超目标 36% |
| 社交挑战参与率 | 60% | 78% | 超目标 30% |
| 日均使用时长 | 5 分钟 | 8 分钟 | 超目标 60% |

**设计决策回顾**

1. **"中心按钮"策略**：将快速记录按钮置于底部导航中心位置，而非传统的右下角浮动按钮，这一决策使运动记录率提升了 42%。用户调研显示，中心位置的按钮更符合单手操作习惯，且在视觉上更具"仪式感"。

2. **环形进度设计**：选择三环嵌套而非三个独立的进度条，不仅节省了屏幕空间，更重要的是创造了一个统一的"完成感"目标。用户反馈显示，"集齐三个环"成为了强烈的内在动机。

3. **游戏化深度**：我们没有采用简单的"积分+排行榜"模式，而是设计了"成就树"系统——每个成就解锁后会开启新的分支路径，创造持续的探索感。这一设计使成就系统的参与率达到了 73%，远超行业平均的 45%。

**经验教训**

1. **数据需要故事**：单纯展示数字（如"今日步数 8,000"）不如讲故事（如"今天你走了 8,000 步，相当于爬了 20 层楼"）有效。情感化的数据呈现是提升用户参与度的关键杠杆。

2. **社交需要"轻量级"**：过于复杂的社交功能会增加用户的认知负担。GlowFit 的社交功能始终保持"轻量"——一个排行榜、一个挑战邀请、一个成就分享，足以建立社交连接而不会造成压力。

3. **动效是体验的"调味料"**：适度的动效能显著提升感知品质，但过度使用会导致疲劳。我们最终将动效控制在"每次都不同但不喧宾夺主"的平衡点上。

4. **测试越早越好**：我们在低保真线框阶段就进行了用户测试，发现了三个严重的可用性问题并及时修正。如果等到高保真阶段才发现，返工成本将增加 5 倍。

**后续迭代方向**

基于用户反馈和数据分析，我们规划了三个迭代方向：

- **AI 教练 2.0**：引入基于用户历史数据的个性化训练建议，从"记录工具"进化为"智能伙伴"
- **社交圈子**：支持创建小型运动圈子（5-20 人），提供更紧密的社交连接
- **企业健康计划**：面向 B 端客户，提供团队运动挑战和健康数据看板
