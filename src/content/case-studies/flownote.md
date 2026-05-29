---
title:
  zh: "FlowNote — AI 驱动的智能笔记应用"
  en: "FlowNote — AI-Powered Intelligent Note-Taking App"
subtitle:
  zh: "让笔记像思维一样流动，让 AI 帮你整理知识脉络"
  en: "Let notes flow like thoughts, let AI organize your knowledge"
cover: "/images/projects/placeholder-cover.svg"
role:
  zh: "UI/UX 设计师"
  en: "UI/UX Designer"
timeline: "2025.03 — 2025.08"
tags: ["UI/UX Design", "Product Design", "AI", "Mobile App", "Prototyping"]
order: 1
metrics:
  - label:
      zh: "用户效率提升"
      en: "User Efficiency"
    value: "+40%"
  - label:
      zh: "笔记整理时间"
      en: "Organization Time"
    value: "-60%"
  - label:
      zh: "用户满意度"
      en: "User Satisfaction"
    value: "4.8/5"
  - label:
      zh: "月活用户"
      en: "MAU"
    value: "50K+"
---

<div id="background"></div>

## 项目背景


### 问题洞察

在信息爆炸的时代，知识工作者面临一个悖论：他们每天产出大量笔记和想法，却花费将近 **30% 的工作时间**在整理和检索这些笔记上，而不是专注于真正有价值的知识创造。传统笔记工具虽然功能完善，但本质上仍停留在"记录"层面，缺乏对内容的深度理解和智能组织能力。

根据我的调研数据，平均每位知识工作者每天创建 3-5 条笔记，但每周只有不到 15% 的历史笔记被有效复用。笔记越积越多，检索成本线性增长，最终沦为"写了却找不到"的数字废墟。

### 目标用户画像

**用户画像一：小林 — 大学研究生**

- 年龄：24 岁，计算机科学专业
- 目标：高效管理课程笔记、论文文献和项目灵感，构建个人知识体系
- 痛点：用 Notion 建了 200+ 页面的笔记库，但翻找一篇特定主题的笔记需要花费 10-15 分钟；手动打标签既繁琐又不一致
- 技术背景：熟悉各类效率工具，但期望更智能的自动整理方案

**用户画像二：陈姐 — 产品经理**

- 年龄：32 岁，互联网公司产品经理
- 目标：快速记录产品想法、用户反馈和会议纪要，随时调取相关信息
- 痛点：每天产生大量碎片化笔记，分散在多个 App 中；回忆"上周三用户访谈提到的那个竞品功能"需要在多个工具间跳转搜索
- 期望：一个能理解上下文关系的笔记系统

**用户画像三：张老师 — 知识博主**

- 年龄：38 岁，教育科技领域从业者
- 目标：管理跨领域的知识素材，构建可复用的知识网络
- 痛点：大量阅读和摘录的笔记缺乏关联，难以发现不同知识领域之间的潜在联系
- 期望：能主动发现知识关联、辅助内容创作的智能工具

### 产品目标

FlowNote 的核心愿景是：**打造一个能和你一起思考的笔记应用**。它不应该只是一个记录工具，而应该是一个知识伙伴——能够理解你写下的内容，自动发现知识之间的关联，并在你需要的时候提供精准的信息检索。

具体业务指标：

- 将笔记整理时间从平均每周 3.2 小时降低至 1.3 小时以内
- 提升笔记的有效复用率从 15% 提升至 60% 以上
- 在上线 6 个月内达到 5 万月活用户，留存率 > 40%

---

<div id="research"></div>

## 用户研究


### 用户访谈核心洞察

我进行了 24 场深度用户访谈（每场 45-60 分钟），覆盖大学生、产品经理、内容创作者、科研人员四类目标用户群。以下是 5 个最关键的发现：

**洞察一：标签系统的使用率与弃用率同样高**

> "我每次新建笔记都会认真打标签，大概坚持了两周，然后就再也不打了。" — P07

所有访谈用户都尝试过手动标签系统，但平均在 2 周后就放弃使用。标签的价值被广泛认可，但手动维护的成本太高。这直接验证了 AI 自动标签的市场需求。

**洞察二：搜索行为呈现"模糊回忆"模式**

> "我不会搜索'竞品分析2024Q1'这种精确关键词，我通常会搜'那个竞品的定价策略'，因为我不记得具体文件名了。" — P12

用户的搜索习惯是以模糊概念为起点，而非精确关键词。现有工具的搜索功能大多基于关键词匹配，无法满足这种语义级别的搜索需求。

**洞察三：笔记之间的关联是隐性的、动态的**

> "我发现三周前记的一条笔记和今天的一条笔记其实讲的是同一个东西，但我在创建它们的时候完全没有意识到。" — P03

知识之间的联系往往在时间推移中才逐渐显现。用户期待工具能主动提示这种跨时间的关联，而非仅仅被动存储。

**洞察四：协作场景被严重忽视**

> "我和团队成员经常需要在同一篇笔记上讨论和补充，但大部分笔记工具的协作功能都很弱。" — P19

知识工作者的笔记往往需要与他人共享和讨论。现有笔记工具在实时协作方面的体验普遍薄弱，这是一个明显的市场空白。

**洞察五：移动端体验决定使用粘性**

> "我有一半的灵感都是在通勤路上产生的，如果移动端不好用，我就会用备忘录先记着，然后...然后就忘了。" — P21

移动端体验不是"锦上添花"，而是决定产品能否融入用户日常节奏的关键。一个在手机上难用的笔记应用，注定无法覆盖完整的使用场景。

### 竞品分析

| 维度 | Notion | Obsidian | Apple Notes | FlowNote (目标) |
|------|--------|----------|-------------|----------------|
| AI 智能标签 | ✗ | ✗ (需插件) | ✗ | ✓ 内置 |
| 知识图谱 | ✗ | ✓ 社区插件 | ✗ | ✓ 原生集成 |
| 语义搜索 | ✗ | ✗ | 部分支持 | ✓ AI 语义搜索 |
| 实时协作 | ✓ | ✗ | ✓ (有限) | ✓ |
| 离线支持 | 有限 | ✓ | ✓ | ✓ |
| 跨平台 | ✓ | ✓ | 仅 Apple | ✓ |
| 定价 | $8/月起 | 免费 (自托管) | 免费 | 免费 + $5/月高级版 |
| 学习曲线 | 中等 | 高 | 低 | 低 |

竞品分析显示，目前市场上没有任何一款产品能同时在 AI 智能、知识图谱和实时协作三个维度提供完整体验。FlowNote 的差异化定位正是"AI 驱动的知识管理"——不只是记录，更是理解和组织。

### 三大核心痛点总结

1. **整理成本过高** — 手动标签和分类系统无法维持，笔记逐渐变成无序堆砌
2. **检索效率低下** — 基于关键词的搜索无法理解用户的模糊意图，信息触达效率低
3. **知识孤岛严重** — 笔记之间的关联完全依赖人脑记忆，无法形成结构化的知识网络

---

<div id="architecture"></div>

## 信息架构


### 产品信息架构

FlowNote 采用"智能中枢"式的架构设计，以 AI 引擎为核心连接所有功能模块。整体架构分为三层：

**基础层**：用户认证、数据存储、同步服务、离线缓存
**智能层**：AI 标签引擎、语义搜索引擎、知识图谱生成器、内容摘要生成
**交互层**：笔记编辑器、图谱可视化、搜索界面、协作工作区、个人中心

### 核心用户流程

一个典型的使用场景是：用户打开 FlowNote 浏览今天新增的笔记卡片，点击"创建笔记"按钮进入编辑器，开始撰写内容。在编辑过程中，AI 引擎实时分析文本，在侧边栏动态推荐相关标签和关联笔记。编辑完成后，笔记自动归类到知识图谱的相应位置，用户可以在知识图谱中看到这篇新笔记如何与现有知识产生连接。

当用户需要查找之前的笔记时，通过语义搜索输入模糊概念（例如"上周关于用户留存的讨论"），AI 将从语义层面理解搜索意图，返回相关的笔记片段和知识图谱节点，而非简单的关键词匹配结果。

### 导航结构

FlowNote 采用移动端标准的底部标签栏导航，五个核心入口：

| Tab | 图标 | 功能定位 |
|-----|------|---------|
| 首页 (Home) | 网格 | AI 精选的笔记信息流，按主题自动聚合 |
| 创建 (Create) | 加号 | 新建笔记/快速捕获灵感 |
| 图谱 (Graph) | 网络节点 | 可视化知识关系网络 |
| 搜索 (Search) | 放大镜 | AI 语义搜索 + 筛选器 |
| 我的 (Profile) | 个人 | 设置、数据统计、导出 |

这种五入口设计确保了核心功能的可达性——用户在任意界面最多两次点击就能触达任何功能。同时，底部导航的高度固定为 56px，确保拇指操作的舒适性。

---

<div id="wireframe"></div>

## 线框图


### 首页信息流

首页采用卡片瀑布流布局，顶部是一个固定的搜索栏（支持语音输入和快捷搜索），下方是 AI 自动生成的笔记卡片网格。每张卡片包含标题预览、首段摘要、AI 标签胶囊、以及关联笔记数。卡片支持左右滑动快速浏览，长按进入批量管理模式。顶部还设有一个"今日洞察"横幅，展示 AI 发现的跨笔记知识关联。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="p-4 space-y-3">
<div class="h-8 bg-gray-100 rounded-lg"></div>
<div class="flex gap-2">
<div class="h-6 w-12 bg-gray-200 rounded-full"></div>
<div class="h-6 w-12 bg-gray-200 rounded-full"></div>
<div class="h-6 w-12 bg-gray-200 rounded-full"></div>
</div>
<div class="h-16 bg-gray-50 rounded-xl border border-gray-200 p-3">
<div class="h-3 bg-gray-200 rounded w-3/4 mb-2"></div>
<div class="h-2 bg-gray-100 rounded w-full mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-2/3"></div>
</div>
<div class="h-16 bg-gray-50 rounded-xl border border-gray-200 p-3">
<div class="h-3 bg-gray-200 rounded w-1/2 mb-2"></div>
<div class="h-2 bg-gray-100 rounded w-full mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-3/4"></div>
</div>
<div class="h-16 bg-gray-50 rounded-xl border border-gray-200 p-3">
<div class="h-3 bg-gray-200 rounded w-2/3 mb-2"></div>
<div class="h-2 bg-gray-100 rounded w-full mb-1"></div>
<div class="h-2 bg-gray-100 rounded w-1/2"></div>
</div>
</div>
<div class="h-14 border-t border-gray-200 flex items-center justify-around">
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-8 h-8 bg-gray-300 rounded-full"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
<div class="w-6 h-6 bg-gray-200 rounded"></div>
</div>
</div>

### 编辑器界面

编辑器占据全屏空间，顶部是轻量工具栏（标题、加粗、列表、图片插入等），中部是沉浸式文本编辑区域。关键创新在于右侧的 AI 助手面板——可以收起为一个小浮标，展开后显示实时 AI 建议：推荐标签、关联笔记、内容摘要、语法优化。AI 面板支持上下滑动浏览建议列表，点击即可一键应用。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="h-10 bg-gray-50 border-b border-gray-200 flex items-center px-3 gap-2">
<div class="w-5 h-5 bg-gray-200 rounded"></div>
<div class="w-5 h-5 bg-gray-200 rounded"></div>
<div class="w-5 h-5 bg-gray-200 rounded"></div>
<div class="w-5 h-5 bg-gray-200 rounded"></div>
<div class="ml-auto w-5 h-5 bg-gray-300 rounded"></div>
</div>
<div class="flex">
<div class="flex-1 p-4 space-y-2">
<div class="h-4 bg-gray-200 rounded w-1/3"></div>
<div class="h-2 bg-gray-100 rounded w-full"></div>
<div class="h-2 bg-gray-100 rounded w-full"></div>
<div class="h-2 bg-gray-100 rounded w-3/4"></div>
<div class="h-2 bg-gray-100 rounded w-full"></div>
<div class="h-2 bg-gray-100 rounded w-2/3"></div>
</div>
<div class="w-20 bg-gray-50 border-l border-gray-200 p-2 space-y-2">
<div class="h-4 bg-gray-200 rounded w-full"></div>
<div class="h-3 bg-gray-100 rounded w-full"></div>
<div class="h-3 bg-gray-100 rounded w-full"></div>
<div class="h-3 bg-gray-100 rounded w-2/3"></div>
</div>
</div>
</div>

### 知识图谱

知识图谱采用力导向图布局，节点代表笔记，连线代表笔记间的语义关联强度。节点大小反映笔记的重要性（基于引用次数和关联度），颜色代表所属主题分类。底部提供一个半透明的筛选面板，支持按时间范围、主题、标签进行图谱过滤。点击任意节点会弹出笔记预览卡片，双击进入详情。

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">
<div class="h-7 bg-gray-100 flex items-center justify-center">
<div class="w-16 h-1 rounded-full bg-gray-300"></div>
</div>
<div class="relative h-[500px] bg-gray-50 flex items-center justify-center">
<svg class="absolute inset-0 w-full h-full" viewBox="0 0 320 500">
<line x1="100" y1="150" x2="180" y2="200" stroke="#d1d5db" stroke-width="2"/>
<line x1="180" y1="200" x2="240" y2="160" stroke="#d1d5db" stroke-width="2"/>
<line x1="180" y1="200" x2="160" y2="300" stroke="#d1d5db" stroke-width="2"/>
<line x1="160" y1="300" x2="80" y2="350" stroke="#d1d5db" stroke-width="2"/>
<line x1="240" y1="160" x2="280" y2="250" stroke="#d1d5db" stroke-width="1.5"/>
</svg>
<div class="absolute top-[130px] left-[80px] w-10 h-10 bg-gray-300 rounded-full flex items-center justify-center text-[8px] text-gray-600">3</div>
<div class="absolute top-[180px] left-[160px] w-14 h-14 bg-gray-400 rounded-full flex items-center justify-center text-[8px] text-white">5</div>
<div class="absolute top-[140px] left-[220px] w-8 h-8 bg-gray-200 rounded-full flex items-center justify-center text-[8px] text-gray-600">2</div>
<div class="absolute top-[280px] left-[140px] w-12 h-12 bg-gray-350 rounded-full flex items-center justify-center text-[8px] text-gray-600">4</div>
<div class="absolute top-[330px] left-[60px] w-8 h-8 bg-gray-200 rounded-full flex items-center justify-center text-[8px] text-gray-600">1</div>
</div>
<div class="absolute bottom-0 left-0 right-0 bg-white/80 backdrop-blur-sm border-t border-gray-200 p-3 flex gap-2">
<div class="h-6 px-3 bg-gray-200 rounded-full text-[8px] flex items-center text-gray-500">全部</div>
<div class="h-6 px-3 bg-gray-100 rounded-full text-[8px] flex items-center text-gray-400">学习</div>
<div class="h-6 px-3 bg-gray-100 rounded-full text-[8px] flex items-center text-gray-400">工作</div>
</div>
</div>

---

<div id="visual"></div>

## 视觉设计


### 设计哲学："清晰即智能"

FlowNote 的视觉设计围绕"清晰即智能"这一核心理念展开。我们拒绝花哨的装饰性元素，相信真正的智能应该体现在信息的清晰呈现和操作的直觉性上。每一个视觉决策都服务于一个目标：让用户专注于内容本身，而非工具的复杂性。

整体视觉语言追求克制而温暖的科技感——通过精准的留白、层次分明的排版和微妙的渐变，营造一个既有现代科技感又不失人文温度的笔记环境。

### 色彩系统

**主色调 — 蓝紫渐变**

FlowNote 的品牌色采用从 Indigo (#6366F1) 到 Violet (#8B5CF6) 的渐变，象征着思维的流动性和知识的多维连接。蓝紫色在色彩心理学中代表智慧、创造力和深度思考，与产品的知识管理定位高度契合。渐变方向从左上到右下，暗示从输入到输出、从碎片到体系的思维演进。

**辅助色 — 琥珀金**

Accent 色采用琥珀金 (#F59E0B)，用于高亮 AI 推荐、重要操作按钮和知识关联提示。暖色调的金与冷色调的蓝紫形成互补对比，在视觉上自然引导用户关注 AI 的主动建议。

**中性色系统**

- 正文：#1F2937（深灰，确保长文本阅读舒适性）
- 二级文本：#6B7280（中灰，用于辅助信息和元数据）
- 占位符：#9CA3AF（浅灰，用于空状态和未填写字段）
- 背景：#F9FAFB（接近白色的极浅灰，减少屏幕眩光）
- 卡片背景：#FFFFFF（纯白，确保内容的视觉纯净度）
- 边框：#E5E7EB（细线边框，轻量分割而不干扰阅读）

**语义色**

- 成功/完成：#10B981（绿松石，用于笔记完成同步状态）
- 警告/待处理：#F59E0B（琥珀金，用于 AI 建议和待办提醒）
- 错误/删除：#EF4444（红色，用于删除操作和错误提示）
- 信息/提示：#3B82F6（蓝色，用于系统提示和帮助信息）

### 字体系统

**主字体 — Inter**

Inter 是一款专为屏幕阅读优化的无衬线字体，其 x-height 设计和开放的字形确保了小尺寸下的优秀可读性。在 FlowNote 中，Inter 承担了所有 UI 文字、正文内容和导航标签的渲染。字重使用 400（正文）、500（标签和按钮）、600（标题）、700（大标题）。

**等宽字体 — JetBrains Mono**

用于代码片段、API 文档引用和笔记中的技术标记。JetBrains Mono 的连字设计和清晰的字符区分度使其成为代码块的最佳选择。字号设置为 14px，行高 1.6。

### 间距与圆角系统

采用 4px 基础网格系统：

- xs: 4px（图标与文字间距）
- sm: 8px（紧凑组件内间距）
- md: 16px（标准组件内间距）
- lg: 24px（卡片内间距）
- xl: 32px（区块间距）
- 2xl: 48px（页面级间距）

圆角：按钮 8px、卡片 12px、模态框 16px、头像和图标 50%。统一的圆角系统确保视觉一致性。

---

<div id="high-fidelity"></div>

## 高保真设计


### 屏幕一：首页 — AI 精选信息流

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="bg-gray-900 h-7 flex items-center justify-center relative">
<div class="w-20 h-5 bg-black rounded-full"></div>
<div class="absolute left-5 w-1.5 h-1.5 rounded-full bg-green-400"></div>
</div>
<div class="bg-gradient-to-r from-indigo-500 to-violet-500 px-5 pt-3 pb-2">
<div class="flex justify-between items-center text-white/80 text-[10px] font-medium mb-3">
<span>9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3c-1.65-1.66-4.34-1.66-6 0zm-4-4l2 2c2.76-2.76 7.24-2.76 10 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>
<div class="relative mb-3">
<div class="w-full h-9 bg-white/20 backdrop-blur-sm rounded-xl flex items-center px-3 gap-2">
<svg class="w-4 h-4 text-white/70" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
<span class="text-white/60 text-xs">搜索你的笔记...</span>
<div class="ml-auto flex items-center gap-1.5">
<div class="w-5 h-5 rounded-full bg-white/20 flex items-center justify-center">
<svg class="w-3 h-3 text-white/70" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 18.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM12 13a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM12 7.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"/></svg>
</div>
</div>
</div>
</div>
<div class="flex gap-2 mb-1">
<span class="px-3 py-1 bg-white text-indigo-600 rounded-full text-[10px] font-semibold shadow-sm">全部</span>
<span class="px-3 py-1 bg-white/15 text-white rounded-full text-[10px] font-medium">学习</span>
<span class="px-3 py-1 bg-white/15 text-white rounded-full text-[10px] font-medium">工作</span>
<span class="px-3 py-1 bg-white/15 text-white rounded-full text-[10px] font-medium">灵感</span>
</div>
</div>
<div class="p-4 bg-gray-50" style="height: 380px; overflow-y: auto;">
<div class="mb-4 p-3 rounded-xl bg-gradient-to-r from-indigo-500/10 to-violet-500/10 border border-indigo-200">
<div class="flex items-center gap-2 mb-1.5">
<div class="w-5 h-5 rounded-full bg-gradient-to-br from-indigo-500 to-violet-500 flex items-center justify-center">
<span class="text-white text-[8px]">AI</span>
</div>
<span class="text-[10px] font-semibold text-indigo-700">今日洞察</span>
</div>
<p class="text-[10px] text-gray-600 leading-relaxed">你有 3 篇关于"用户增长"的笔记产生了新的关联，其中包含上周提到的竞品定价策略。</p>
</div>

<div class="mb-3 p-3.5 bg-white rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-start justify-between mb-2">
<div class="w-7 h-7 rounded-lg bg-gradient-to-br from-indigo-500 to-violet-500 flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
</div>
<div class="flex items-center gap-1">
<div class="w-1.5 h-1.5 rounded-full bg-green-400"></div>
<span class="text-[9px] text-gray-400">2 小时前</span>
</div>
</div>
<h3 class="text-xs font-semibold text-gray-800 mb-1">2025 产品增长策略规划</h3>
<p class="text-[10px] text-gray-500 leading-relaxed mb-2.5 line-clamp-2">基于上季度数据分析，用户留存率从 35% 提升至 42%，但新用户激活率仍有较大提升空间...</p>
<div class="flex items-center gap-1.5 flex-wrap">
<span class="px-2 py-0.5 bg-indigo-50 text-indigo-600 rounded-full text-[9px] font-medium">增长策略</span>
<span class="px-2 py-0.5 bg-violet-50 text-violet-600 rounded-full text-[9px] font-medium">数据分析</span>
<span class="px-2 py-0.5 bg-amber-50 text-amber-600 rounded-full text-[9px] font-medium flex items-center gap-0.5">
<svg class="w-2.5 h-2.5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
AI 推荐
</span>
</div>
</div>

<div class="mb-3 p-3.5 bg-white rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-start justify-between mb-2">
<div class="w-7 h-7 rounded-lg bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
</div>
<div class="flex items-center gap-1">
<div class="w-1.5 h-1.5 rounded-full bg-amber-400"></div>
<span class="text-[9px] text-gray-400">昨天</span>
</div>
</div>
<h3 class="text-xs font-semibold text-gray-800 mb-1">竞品定价模型分析 — Linear vs Notion</h3>
<p class="text-[10px] text-gray-500 leading-relaxed mb-2.5 line-clamp-2">两家 SaaS 产品采取了完全不同的定价策略：Linear 坚持简洁的团队定价，Notion 则采用分层定价...</p>
<div class="flex items-center gap-1.5 flex-wrap">
<span class="px-2 py-0.5 bg-amber-50 text-amber-600 rounded-full text-[9px] font-medium">竞品分析</span>
<span class="px-2 py-0.5 bg-blue-50 text-blue-600 rounded-full text-[9px] font-medium">SaaS</span>
<span class="px-2 py-0.5 bg-gray-100 text-gray-500 rounded-full text-[9px] font-medium">关联 5 篇</span>
</div>
</div>

<div class="mb-3 p-3.5 bg-white rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
<div class="flex items-start justify-between mb-2">
<div class="w-7 h-7 rounded-lg bg-gradient-to-br from-emerald-400 to-teal-500 flex items-center justify-center">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
</div>
<span class="text-[9px] text-gray-400">3 天前</span>
</div>
<h3 class="text-xs font-semibold text-gray-800 mb-1">《思考，快与慢》读书笔记</h3>
<p class="text-[10px] text-gray-500 leading-relaxed mb-2.5 line-clamp-2">丹尼尔·卡尼曼将人类的思维模式分为系统1和系统2。系统1是快速的、自动化的直觉判断...</p>
<div class="flex items-center gap-1.5 flex-wrap">
<span class="px-2 py-0.5 bg-emerald-50 text-emerald-600 rounded-full text-[9px] font-medium">读书笔记</span>
<span class="px-2 py-0.5 bg-purple-50 text-purple-600 rounded-full text-[9px] font-medium">认知科学</span>
</div>
</div>
</div>
<div class="h-14 bg-white border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg bg-indigo-500/10 flex items-center justify-center">
<svg class="w-4 h-4 text-indigo-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
</div>
<span class="text-[9px] font-semibold text-indigo-500">首页</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/></svg>
</div>
<span class="text-[9px] text-gray-400">图谱</span>
</div>
<div class="flex flex-col items-center gap-0.5 -mt-3">
<div class="w-11 h-11 rounded-full bg-gradient-to-r from-indigo-500 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
</div>
<span class="text-[9px] text-gray-400">创建</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
</div>
<span class="text-[9px] text-gray-400">搜索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
</div>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
<div class="h-1 bg-white"></div>
</div>

首页信息流展示了 AI 自动分类的笔记卡片，顶部的今日洞察横幅主动推送知识关联，底部中央的创建按钮通过渐变色和阴影效果突出核心操作。

---

### 屏幕二：编辑器 — 沉浸式写作 + AI 助手

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="bg-gray-900 h-7 flex items-center justify-center relative">
<div class="w-20 h-5 bg-black rounded-full"></div>
<div class="absolute left-5 w-1.5 h-1.5 rounded-full bg-green-400"></div>
</div>
<div class="bg-white border-b border-gray-100 px-4 py-2 flex items-center justify-between">
<div class="flex items-center gap-3">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15 19l-7-7 7-7"/></svg>
<span class="text-[10px] text-gray-400">已自动保存</span>
</div>
<div class="flex items-center gap-2">
<div class="w-6 h-6 rounded-full bg-indigo-500/10 flex items-center justify-center">
<svg class="w-3 h-3 text-indigo-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
</div>
<div class="w-6 h-6 rounded-full bg-gray-100 flex items-center justify-center">
<svg class="w-3 h-3 text-gray-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"/></svg>
</div>
</div>
</div>
<div class="flex" style="height: 340px;">
<div class="flex-1 p-4">
<div class="text-[9px] text-gray-400 mb-1">编辑中</div>
<div class="text-sm font-bold text-gray-800 mb-3 leading-tight">2025 产品增长策略规划</div>
<div class="flex items-center gap-1 mb-3 pb-2 border-b border-gray-100">
<div class="w-6 h-6 rounded flex items-center justify-center bg-gray-50"><span class="text-[10px] font-bold text-gray-600">B</span></div>
<div class="w-6 h-6 rounded flex items-center justify-center"><span class="text-[10px] text-gray-400" style="font-style: italic;">I</span></div>
<div class="w-6 h-6 rounded flex items-center justify-center"><span class="text-[10px] text-gray-400" style="text-decoration: underline;">U</span></div>
<div class="w-px h-4 bg-gray-200 mx-0.5"></div>
<div class="w-6 h-6 rounded flex items-center justify-center"><svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16m-7 6h7"/></svg></div>
<div class="w-6 h-6 rounded flex items-center justify-center"><svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg></div>
<div class="w-6 h-6 rounded flex items-center justify-center"><svg class="w-3 h-3 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/></svg></div>
</div>
<div class="text-[11px] text-gray-700 leading-[1.7] space-y-2">
<p>基于上季度数据分析，用户留存率从 35% 提升至 42%，但新用户激活率仍有较大提升空间。</p>
<p class="text-gray-400">|</p>
<p>主要增长策略方向：</p>
<p class="pl-3 border-l-2 border-indigo-400">1. 优化 Onboarding 流程，降低首日使用门槛</p>
<p class="pl-3 border-l-2 border-indigo-400">2. 引入 AI 智能推荐，提升内容发现效率</p>
<p class="pl-3 border-l-2 border-indigo-400">3. 建立用户成长体系，激励深度使用...</p>
</div>
</div>
<div class="w-[110px] border-l border-gray-100 bg-indigo-50/50 p-2.5">
<div class="flex items-center gap-1.5 mb-2.5">
<div class="w-4 h-4 rounded-full bg-gradient-to-br from-indigo-500 to-violet-500 flex items-center justify-center">
<span class="text-white text-[6px] font-bold">AI</span>
</div>
<span class="text-[9px] font-semibold text-indigo-700">AI 助手</span>
</div>
<div class="mb-3">
<p class="text-[8px] text-gray-500 font-medium mb-1.5 uppercase tracking-wide">推荐标签</p>
<div class="flex flex-wrap gap-1">
<span class="px-1.5 py-0.5 bg-white border border-indigo-200 rounded text-[8px] text-indigo-600">增长策略</span>
<span class="px-1.5 py-0.5 bg-white border border-indigo-200 rounded text-[8px] text-indigo-600">数据分析</span>
<span class="px-1.5 py-0.5 bg-white border border-gray-200 rounded text-[8px] text-gray-500">+ 更多</span>
</div>
</div>
<div class="mb-3">
<p class="text-[8px] text-gray-500 font-medium mb-1.5 uppercase tracking-wide">相关笔记</p>
<div class="space-y-1.5">
<div class="p-1.5 bg-white rounded-lg border border-gray-100">
<p class="text-[8px] font-medium text-gray-700 line-clamp-1">竞品定价模型分析</p>
<p class="text-[7px] text-gray-400">相似度 87%</p>
</div>
<div class="p-1.5 bg-white rounded-lg border border-gray-100">
<p class="text-[8px] font-medium text-gray-700 line-clamp-1">用户增长漏斗优化</p>
<p class="text-[7px] text-gray-400">相似度 72%</p>
</div>
</div>
</div>
<div>
<p class="text-[8px] text-gray-500 font-medium mb-1.5 uppercase tracking-wide">AI 摘要</p>
<div class="p-1.5 bg-white rounded-lg border border-gray-100">
<p class="text-[8px] text-gray-600 leading-relaxed">本篇聚焦用户增长与留存策略，建议补充 A/B 测试计划和预期 ROI 分析。</p>
</div>
</div>
</div>
</div>
<div class="h-10 bg-white border-t border-gray-100 flex items-center justify-between px-4">
<div class="flex items-center gap-3">
<svg class="w-3.5 h-3.5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"/></svg>
<svg class="w-3.5 h-3.5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
<svg class="w-3.5 h-3.5 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>
</div>
<div class="flex items-center gap-2">
<span class="text-[9px] text-gray-400">1,247 字</span>
<div class="w-5 h-5 rounded-full bg-gradient-to-r from-indigo-500 to-violet-500 flex items-center justify-center">
<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 10l7-7m0 0l7 7m-7-7v18"/></svg>
</div>
</div>
</div>
<div class="h-1 bg-white"></div>
</div>

编辑器界面采用左编辑区 + 右 AI 助手的双栏布局。AI 助手面板可收起为浮标，展开后实时提供标签推荐、相关笔记联想和内容摘要。这种设计确保 AI 的存在感既不打扰写作流，又能在需要时迅速介入。

---

### 屏幕三：知识图谱 — 可视化知识网络

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="bg-gray-900 h-7 flex items-center justify-center relative">
<div class="w-20 h-5 bg-black rounded-full"></div>
<div class="absolute left-5 w-1.5 h-1.5 rounded-full bg-green-400"></div>
</div>
<div class="bg-white border-b border-gray-100 px-4 py-2.5 flex items-center justify-between">
<h2 class="text-xs font-bold text-gray-800">知识图谱</h2>
<div class="flex items-center gap-2">
<div class="px-2 py-0.5 bg-indigo-50 text-indigo-600 rounded-full text-[9px] font-medium">全部笔记</div>
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/></svg>
</div>
</div>
<div class="relative bg-gradient-to-b from-indigo-50/30 to-white" style="height: 350px;">
<svg class="absolute inset-0 w-full h-full" viewBox="0 0 320 350">
<line x1="160" y1="140" x2="90" y2="80" stroke="#C7D2FE" stroke-width="1.5" opacity="0.7"/>
<line x1="160" y1="140" x2="240" y2="95" stroke="#C7D2FE" stroke-width="1.5" opacity="0.7"/>
<line x1="160" y1="140" x2="120" y2="220" stroke="#DDD6FE" stroke-width="1.5" opacity="0.6"/>
<line x1="160" y1="140" x2="210" y2="210" stroke="#DDD6FE" stroke-width="1.5" opacity="0.6"/>
<line x1="90" y1="80" x2="45" y2="150" stroke="#E0E7FF" stroke-width="1" opacity="0.5"/>
<line x1="240" y1="95" x2="280" y2="160" stroke="#E0E7FF" stroke-width="1" opacity="0.5"/>
<line x1="120" y1="220" x2="60" y2="270" stroke="#E0E7FF" stroke-width="1" opacity="0.5"/>
<line x1="210" y1="210" x2="270" y2="275" stroke="#E0E7FF" stroke-width="1" opacity="0.5"/>
<line x1="90" y1="80" x2="240" y2="95" stroke="#C7D2FE" stroke-width="1" opacity="0.4" stroke-dasharray="4 3"/>
</svg>

<div class="absolute left-1/2 top-[35%] -translate-x-1/2 -translate-y-1/2">
<div class="w-14 h-14 rounded-full bg-gradient-to-br from-indigo-500 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30 border-2 border-white z-10 relative">
<div class="text-center">
<svg class="w-4 h-4 text-white mx-auto mb-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
<span class="text-white text-[7px] font-bold">核心</span>
</div>
</div>
<p class="text-[8px] text-center text-gray-700 font-semibold mt-1 whitespace-nowrap">增长策略</p>
</div>

<div class="absolute left-[15%] top-[15%]">
<div class="w-10 h-10 rounded-full bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center shadow-md border-2 border-white">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"/></svg>
</div>
<p class="text-[7px] text-center text-gray-600 mt-0.5 whitespace-nowrap">竞品分析</p>
</div>

<div class="absolute right-[12%] top-[18%]">
<div class="w-10 h-10 rounded-full bg-gradient-to-br from-emerald-400 to-teal-500 flex items-center justify-center shadow-md border-2 border-white">
<svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
</div>
<p class="text-[7px] text-center text-gray-600 mt-0.5 whitespace-nowrap">读书笔记</p>
</div>

<div class="absolute left-[18%] top-[55%]">
<div class="w-9 h-9 rounded-full bg-gradient-to-br from-blue-400 to-indigo-500 flex items-center justify-center shadow-md border-2 border-white">
<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
</div>
<p class="text-[7px] text-center text-gray-600 mt-0.5 whitespace-nowrap">用户调研</p>
</div>

<div class="absolute right-[15%] top-[52%]">
<div class="w-9 h-9 rounded-full bg-gradient-to-br from-pink-400 to-rose-500 flex items-center justify-center shadow-md border-2 border-white">
<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
</div>
<p class="text-[7px] text-center text-gray-600 mt-0.5 whitespace-nowrap">产品设计</p>
</div>

<div class="absolute left-[3%] top-[38%]">
<div class="w-7 h-7 rounded-full bg-gradient-to-br from-gray-300 to-gray-400 flex items-center justify-center shadow-sm border border-white">
<span class="text-white text-[7px]">AI</span>
</div>
<p class="text-[6px] text-center text-gray-400 mt-0.5 whitespace-nowrap">AI 标签</p>
</div>

<div class="absolute right-[3%] top-[38%]">
<div class="w-7 h-7 rounded-full bg-gradient-to-br from-gray-300 to-gray-400 flex items-center justify-center shadow-sm border border-white">
<span class="text-white text-[7px]">+</span>
</div>
<p class="text-[6px] text-center text-gray-400 mt-0.5 whitespace-nowrap">协作</p>
</div>

<div class="absolute left-[12%] top-[75%]">
<div class="w-6 h-6 rounded-full bg-gradient-to-br from-gray-200 to-gray-300 flex items-center justify-center border border-white">
</div>
</div>
<div class="absolute right-[15%] top-[78%]">
<div class="w-6 h-6 rounded-full bg-gradient-to-br from-gray-200 to-gray-300 flex items-center justify-center border border-white">
</div>
</div>
</div>

<div class="absolute bottom-14 left-0 right-0">
<div class="mx-3 p-2.5 bg-white/90 backdrop-blur-md rounded-xl border border-gray-200 shadow-lg">
<div class="flex items-center gap-1.5 mb-2">
<div class="w-1.5 h-1.5 rounded-full bg-gray-300"></div>
<span class="text-[8px] text-gray-400 font-medium">筛选条件</span>
</div>
<div class="flex gap-1.5">
<span class="px-2 py-0.5 bg-indigo-500 text-white rounded-full text-[8px] font-medium">全部</span>
<span class="px-2 py-0.5 bg-gray-100 text-gray-500 rounded-full text-[8px]">本月</span>
<span class="px-2 py-0.5 bg-gray-100 text-gray-500 rounded-full text-[8px]">增长</span>
<span class="px-2 py-0.5 bg-gray-100 text-gray-500 rounded-full text-[8px]">设计</span>
</div>
</div>
</div>

<div class="h-14 bg-white border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
</div>
<span class="text-[9px] text-gray-400">首页</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg bg-indigo-500/10 flex items-center justify-center">
<svg class="w-4 h-4 text-indigo-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"/></svg>
</div>
<span class="text-[9px] font-semibold text-indigo-500">图谱</span>
</div>
<div class="flex flex-col items-center gap-0.5 -mt-3">
<div class="w-11 h-11 rounded-full bg-gradient-to-r from-indigo-500 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
</div>
<span class="text-[9px] text-gray-400">创建</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
</div>
<span class="text-[9px] text-gray-400">搜索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
</div>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
<div class="h-1 bg-white"></div>
</div>

知识图谱采用力导向布局，中心节点为当前选中的核心笔记，周围节点代表相关联的知识主题。节点颜色映射不同分类，连线粗细反映语义关联强度，虚线表示弱关联。底部半透明筛选面板支持按时间和主题过滤图谱范围。

---

### 屏幕四：AI 搜索 — 语义级信息检索

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-900 overflow-hidden shadow-2xl bg-white">
<div class="bg-gray-900 h-7 flex items-center justify-center relative">
<div class="w-20 h-5 bg-black rounded-full"></div>
<div class="absolute left-5 w-1.5 h-1.5 rounded-full bg-green-400"></div>
</div>
<div class="bg-gradient-to-r from-indigo-500 to-violet-500 px-4 pt-3 pb-4">
<div class="flex items-center gap-2 mb-3">
<div class="flex-1 h-9 bg-white rounded-xl flex items-center px-3 gap-2 shadow-sm">
<svg class="w-3.5 h-3.5 text-indigo-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
<span class="text-xs text-gray-700">竞品定价策略</span>
<svg class="w-3.5 h-3.5 text-gray-300 ml-auto" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12"/></svg>
</div>
<div class="w-9 h-9 bg-white/20 backdrop-blur rounded-xl flex items-center justify-center">
<svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"/></svg>
</div>
</div>
<div class="flex gap-1.5">
<span class="px-2 py-0.5 bg-white text-indigo-600 rounded-full text-[9px] font-semibold">全部</span>
<span class="px-2 py-0.5 bg-white/15 text-white rounded-full text-[9px]">笔记</span>
<span class="px-2 py-0.5 bg-white/15 text-white rounded-full text-[9px]">标签</span>
<span class="px-2 py-0.5 bg-white/15 text-white rounded-full text-[9px]">最近 7 天</span>
</div>
</div>

<div class="p-4 bg-gray-50" style="height: 320px; overflow-y: auto;">
<div class="mb-3 p-2.5 rounded-lg bg-indigo-50 border border-indigo-100">
<div class="flex items-center gap-1.5 mb-1">
<div class="w-4 h-4 rounded-full bg-gradient-to-br from-indigo-500 to-violet-500 flex items-center justify-center">
<span class="text-white text-[6px] font-bold">AI</span>
</div>
<span class="text-[9px] font-semibold text-indigo-700">AI 理解了你的搜索意图</span>
</div>
<p class="text-[9px] text-indigo-600/70 leading-relaxed">正在为你搜索与"竞品定价"语义相关的笔记内容、标签和知识图谱节点...</p>
</div>

<div class="mb-2.5 p-3 bg-white rounded-xl border border-gray-100 shadow-sm">
<div class="flex items-center gap-1.5 mb-1.5">
<div class="w-5 h-5 rounded bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center">
<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
</div>
<span class="text-[10px] font-semibold text-gray-800">竞品定价模型分析 — Linear vs Notion</span>
</div>
<p class="text-[9px] text-gray-500 leading-relaxed mb-2 line-clamp-2">两家 SaaS 产品采取了完全不同的定价策略。Linear 坚持简洁的团队定价，月费 <strong class="text-indigo-600">$8/人</strong>，而 Notion 采用分层定价...</p>
<div class="flex items-center justify-between">
<div class="flex items-center gap-1">
<span class="px-1.5 py-0.5 bg-amber-50 text-amber-600 rounded text-[8px]">竞品分析</span>
<span class="px-1.5 py-0.5 bg-blue-50 text-blue-600 rounded text-[8px]">SaaS</span>
</div>
<span class="text-[8px] text-green-600 font-medium">相似度 92%</span>
</div>
</div>

<div class="mb-2.5 p-3 bg-white rounded-xl border border-gray-100 shadow-sm">
<div class="flex items-center gap-1.5 mb-1.5">
<div class="w-5 h-5 rounded bg-gradient-to-br from-indigo-400 to-violet-500 flex items-center justify-center">
<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
</div>
<span class="text-[10px] font-semibold text-gray-800">定价心理学与用户感知价值</span>
</div>
<p class="text-[9px] text-gray-500 leading-relaxed mb-2 line-clamp-2">锚定效应在 SaaS 定价中扮演关键角色。当用户先看到企业版 <strong class="text-indigo-600">$20/月</strong> 的价格后，专业版 $8/月就会显得极具性价比...</p>
<div class="flex items-center justify-between">
<div class="flex items-center gap-1">
<span class="px-1.5 py-0.5 bg-purple-50 text-purple-600 rounded text-[8px]">定价策略</span>
<span class="px-1.5 py-0.5 bg-pink-50 text-pink-600 rounded text-[8px]">心理学</span>
</div>
<span class="text-[8px] text-green-600 font-medium">相似度 85%</span>
</div>
</div>

<div class="mb-2.5 p-3 bg-white rounded-xl border border-gray-100 shadow-sm">
<div class="flex items-center gap-1.5 mb-1.5">
<div class="w-5 h-5 rounded bg-gradient-to-br from-emerald-400 to-teal-500 flex items-center justify-center">
<svg class="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"/></svg>
</div>
<span class="text-[10px] font-semibold text-gray-800">Freemium 模式转化率研究</span>
</div>
<p class="text-[9px] text-gray-500 leading-relaxed mb-2 line-clamp-2">通过分析 50+ SaaS 产品的定价数据，Freemium 模式的平均转化率为 <strong class="text-indigo-600">2-5%</strong>，但配合使用量限制可提升至 8%...</p>
<div class="flex items-center justify-between">
<div class="flex items-center gap-1">
<span class="px-1.5 py-0.5 bg-emerald-50 text-emerald-600 rounded text-[8px]">数据研究</span>
<span class="px-1.5 py-0.5 bg-orange-50 text-orange-600 rounded text-[8px]">转化率</span>
</div>
<span class="text-[8px] text-green-600 font-medium">相似度 78%</span>
</div>
</div>

<div class="mt-4">
<p class="text-[9px] text-gray-400 font-medium mb-2">最近搜索</p>
<div class="space-y-1.5">
<div class="flex items-center gap-2">
<svg class="w-3 h-3 text-gray-300" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
<span class="text-[9px] text-gray-500">用户增长漏斗</span>
</div>
<div class="flex items-center gap-2">
<svg class="w-3 h-3 text-gray-300" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
<span class="text-[9px] text-gray-500">AI 自动标签实现方案</span>
</div>
<div class="flex items-center gap-2">
<svg class="w-3 h-3 text-gray-300" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
<span class="text-[9px] text-gray-500">知识图谱可视化方案</span>
</div>
</div>
</div>
</div>

<div class="h-14 bg-white border-t border-gray-100 flex items-center justify-around px-2">
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
</div>
<span class="text-[9px] text-gray-400">首页</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2z"/></svg>
</div>
<span class="text-[9px] text-gray-400">图谱</span>
</div>
<div class="flex flex-col items-center gap-0.5 -mt-3">
<div class="w-11 h-11 rounded-full bg-gradient-to-r from-indigo-500 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
<svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M12 4v16m8-8H4"/></svg>
</div>
<span class="text-[9px] text-gray-400">创建</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg bg-indigo-500/10 flex items-center justify-center">
<svg class="w-4 h-4 text-indigo-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
</div>
<span class="text-[9px] font-semibold text-indigo-500">搜索</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-6 h-6 rounded-lg flex items-center justify-center">
<svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
</div>
<span class="text-[9px] text-gray-400">我的</span>
</div>
</div>
<div class="h-1 bg-white"></div>
</div>

AI 搜索界面展示了语义级检索的能力：顶部搜索栏支持语音输入，AI 理解提示条表明系统正在从语义层面分析搜索意图。搜索结果按相关度排序，关键词在摘要中以品牌色高亮，每个结果附带标签和相似度评分。底部保留最近搜索记录，支持快速重复检索。

---

<div id="interaction"></div>

## 交互设计


### 微交互设计

FlowNote 的交互设计追求"流畅而有回应感"，每一个操作都获得即时的视觉反馈，让用户感知到应用的"活性"。

**卡片悬浮提升（Card Hover Lift）**

首页笔记卡片在触摸/悬停时，通过 `transform: translateY(-2px)` 和增强阴影实现微提升效果。提升过程持续 200ms，使用 `cubic-bezier(0.4, 0, 0.2, 1)` 缓动函数，模拟物理世界中卡片被拿起的微妙动态。同时卡片边框颜色从 `gray-100` 渐变到 `indigo-200`，暗示可交互状态。

**AI 建议滑入（AI Suggestion Slide-in）**

AI 助手面板的展开采用从右侧滑入的动画，持续 300ms。面板内容采用渐进式加载——先显示框架，再逐项填充 AI 推荐内容（标签、关联笔记、摘要），每项间隔 100ms 依次出现。这种"思考-呈现"的节奏模拟了 AI 正在分析和推荐的过程，增强了用户对 AI 能力的感知。

**知识图谱节点脉冲（Graph Node Pulse）**

当知识图谱检测到新的知识关联时，相关节点会触发脉冲动画——节点外围出现一圈扩散的光晕，从节点中心向外扩散并逐渐消失，持续 1.5 秒。这个动画在视觉上暗示"发现了新连接"，引导用户关注新产生的知识关联。

**搜索结果高亮（Search Result Highlight）**

语义搜索返回结果时，每个结果卡片以卡片依次滑入的方式呈现（`translateY(10px) -> translateY(0)`，延迟递增 50ms）。搜索关键词在摘要中以 `background-color: #FEF3C7` 的方式高亮，高亮色从 0% 不透明度渐变到 100%，持续 400ms。

### 手势支持

**左滑归档（Swipe to Archive）**

在首页笔记卡片上左滑，卡片渐变为灰色并显示归档图标，滑动距离超过卡片宽度 30% 时触发归档操作，卡片通过缩小+淡出的组合动画移出列表。如果在 2 秒内没有进一步操作，可以通过右滑取消归档。这个手势设计借鉴了邮件应用的成熟交互范式，降低了用户的学习成本。

**双指缩放图谱（Pinch to Zoom Graph）**

知识图谱支持双指缩放，缩放范围从 0.5x 到 3x。在缩放过程中，节点标签的字号会根据缩放级别动态调整——放大时显示更多细节（笔记标题、标签），缩小时只保留节点核心图标和主题分类色。缩放边界有弹性回弹效果，超出范围后松手会回弹到边界值。

**下拉刷新（Pull to Refresh）**

首页和搜索结果支持下拉刷新。下拉时顶部出现品牌渐变色的刷新指示器，指示器由三个依次亮起的圆点组成，模拟 AI 正在"思考"的状态。刷新完成后，新内容通过交叉淡入的方式替换旧内容，避免页面闪烁。

**长按批量操作（Long Press for Batch Mode）**

在首页笔记卡片上长按 500ms 进入批量选择模式。进入时所有卡片轻微震动（通过 Haptic Feedback API），选中卡片出现蓝色边框和对勾标记。批量模式下底部出现操作栏（移动、删除、分享、标签），提供高效的批量管理能力。

### 页面过渡

**列表到详情的共享元素过渡（Shared Element Transition）**

点击首页笔记卡片进入编辑器时，卡片的标题、内容摘要和标签通过共享元素过渡"飞入"编辑器的对应位置。过渡动画持续 400ms，使用 `cubic-bezier(0.2, 0, 0, 1)` 缓动曲线，模拟笔记从列表"展开"为全屏的过程。编辑器的其他元素（工具栏、AI 面板）则通过淡入方式出现。

**图谱节点展开（Graph Node Expand）**

在知识图谱中点击节点时，节点从当前位置扩展为全屏卡片，连线和周围节点淡出。卡片内容展示笔记摘要和快速操作按钮。这种过渡避免了突兀的页面跳转，保持了空间关系的连续性。

**标签页切换（Tab Bar Transition）**

底部标签栏切换时，新页面从底部 10px 处滑入并淡入，旧页面同时向上滑出并淡出。切换过程中底部标签栏保持不动，提供稳定的导航锚点。图谱页面的切换略有不同——图谱以缩放动画从图标位置展开为全屏，强调图谱作为核心功能的特殊地位。

---

<div id="results"></div>

## 结果与反思


### 关键数据成果

FlowNote 在 2025 年 8 月正式上线后，6 个月内达成了以下核心指标：

**效率提升**

- 用户笔记整理时间平均减少 60%（从每周 3.2 小时降至 1.3 小时）
- 笔记有效复用率从 15% 提升至 52%（目标 60%，持续优化中）
- 用户日常操作步骤减少 40%（AI 自动标签替代了手动分类）

**用户增长**

- 月活用户（MAU）达到 52,000+，超出 50K 目标
- 7 日留存率 47%，30 日留存率 38%（行业平均水平为 25%）
- App Store 评分 4.8/5，Google Play 评分 4.7/5
- 用户 NPS（净推荐值）达到 62，属于"优秀"区间

**功能使用**

- AI 自动标签功能使用率达 89%，成为最高频使用的 AI 功能
- 知识图谱页面日均访问 3.2 次/用户
- 语义搜索功能上线后，传统关键词搜索使用量下降 67%

### 有效的设计决策

**AI 作为"建议者"而非"决策者"**

在设计 AI 功能时，我们始终坚持 AI 提供建议而非直接执行。标签推荐是"推荐"而非"自动应用"，知识关联是"提示"而非"强制连接"。这种设计策略既保留了用户的控制感，又通过"一键采纳"降低了操作成本。用户调研显示，92% 的用户更信任"AI 推荐 + 我确认"的模式。

**双栏编辑器的平衡**

AI 助手侧栏的设计经过了 5 轮迭代。最初采用全屏 AI 面板，但用户反馈"太打扰"；后来尝试底部抽屉式，但"不够直觉"。最终确定的侧栏方案在"可发现性"和"不打扰"之间找到了平衡点——侧栏默认收起为小浮标，需要时一键展开，展开状态占据屏幕 35% 宽度，不会压缩编辑区的核心空间。

**知识图谱的渐进式复杂度**

知识图谱默认展示最近 30 天的笔记关联，避免新用户被复杂的全量图谱吓到。随着用户使用时长增加，图谱自动扩展时间范围。同时提供"简单/详细"两种视图模式，让不同技术水平的用户都能找到舒适的使用方式。

### 可改进之处

**协作功能的深度不足**

实时协作功能虽然上线，但仅支持基础的共同编辑和评论，缺乏版本历史对比、权限分级和协作空间等深度功能。在用户调研中，协作深度不足是排名第二的改进诉求。未来版本计划引入 Google Docs 级别的协作体验。

**离线场景的 AI 体验**

目前 AI 功能依赖云端推理，离线状态下只能使用基础的标签匹配和搜索。虽然离线数据同步做得很好，但 AI 体验的断层仍然影响了移动端在弱网环境下的使用体验。计划在未来引入端侧小模型，实现基础 AI 功能的离线支持。

**桌面端适配**

初始设计和开发以移动端优先，桌面端的适配仅提供了基本的响应式布局。桌面端用户反馈中，"希望有更充分利用大屏幕的布局"是最高频的诉求。计划引入多栏布局、浮动面板等桌面端特有的交互模式。

### 设计反思与教训

**教训一：AI 功能的"可见性"设计比功能本身更重要**

最初我们花费大量精力优化 AI 的准确率（从 85% 提升到 93%），但用户满意度的提升远不如预期。后来发现，问题不在于 AI 不够准，而在于用户感知不到 AI 在工作。增加 AI 状态指示器（如"AI 正在分析"的加载动画、"AI 发现了新关联"的推送提示）后，用户对 AI 功能的感知度提升了 40%，即使准确率没有变化。这让我深刻理解：在 AI 产品中，"让用户看到 AI 在思考"和"让 AI 真正在思考"同样重要。

**教训二：竞品分析的价值不在于模仿，而在于发现差异**

在项目初期，我花了大量时间分析 Notion 和 Obsidian 的功能设计，试图"取其精华"。但最终真正帮助产品脱颖而出的，恰恰是那些竞品都没有做好的领域——AI 驱动的自动化和知识关联可视化。最好的竞品分析不是回答"别人怎么做的"，而是回答"别人没做好的地方在哪里"。

**教训三：迭代速度比完美设计更重要**

FlowNote 的设计稿经历了 47 个版本，前 20 个版本几乎每次都推翻重来。真正让设计成熟的是后半段的快速小迭代——每周 2-3 次用户测试，每次只调整 1-2 个关键交互点。与其追求一步到位的完美方案，不如建立快速验证的迭代机制，让真实用户反馈驱动设计演进。
