---
title:
  zh: "PixelForge — AI 驱动的游戏资产创作平台"
  en: "PixelForge — AI-Powered Game Asset Creation Platform"
subtitle:
  zh: "为独立开发者打造的智能美术工作流"
  en: "Intelligent Art Workflow for Indie Developers"
cover: "/images/case-studies/pixelforge-cover.svg"
role:
  zh: "UI/UX 设计师 & 产品负责人"
  en: "UI/UX Designer & Product Lead"
timeline: "2025.03 — 2025.09"
tags: ["AI", "游戏开发", "Figma", "React", "Unity", "WebGL"]
order: 5
metrics:
  - label:
      zh: "资产制作效率"
      en: "Asset Creation"
    value: "4x faster"
  - label:
      zh: "美术成本"
      en: "Art Costs"
    value: "-60%"
  - label:
      zh: "用户创作量"
      en: "Monthly Creations"
    value: "300+"
  - label:
      zh: "Unity 插件下载"
      en: "Unity Plugin"
    value: "10K+"
---

<div id="background"></div>

## 项目背景


### 行业痛点

独立游戏开发者的预算分配长期存在结构性失衡。根据 Game Developers Conference 2024 调查数据，独立开发者平均将 60% 的项目预算用于美术资产外包，而核心玩法迭代的投入不到 20%。一张高质量的角色原画外包报价在 ¥2000-5000 之间，一套完整的 tileset（含 50+ tile）需要 ¥3000-8000，而一个 2D 平台游戏的全部美术资产通常需要 ¥20000-50000 的预算。

更严重的是迭代成本。当美术风格需要调整时，每次返工都意味着额外的沟通成本和时间延迟。一款中等体量的 2D 游戏从概念到最终美术资产完成，通常需要 3-6 个月的美术制作周期。对于 Game Jam 参与者来说，48 小时内几乎没有时间打磨美术品质。

### 用户画像

**画像一：独立开发者（Solo Indie Dev）**

28 岁，全职开发者，正在开发一款像素风 Roguelike 游戏。熟悉 Unity 和 C#，但美术能力有限。使用免费素材拼凑原型，风格不统一影响了游戏的可发布性。核心诉求：用最少的美术预算获得可发布的视觉品质，同时保持对资产风格的控制权。

**画像二：小型工作室负责人（Small Studio Lead）**

32 岁，带领 5 人团队开发一款 2D 动作游戏。团队有程序和策划但没有专职美术。外包美术资产的成本和沟通成本严重影响了迭代速度。核心诉求：让程序和策划也能快速生成符合风格的美术资产，减少对外包的依赖。

**画像三：Game Jam 参与者（Game Jam Participant）**

25 岁，业余游戏开发者，热衷于参加 Game Jam。48 小时内需要完成游戏的全部内容，美术通常是最大的短板。核心诉求：在极短时间内生成可用的美术资产，让游戏在视觉上不拖后腿。

### 项目目标

PixelForge 的商业目标是通过 AI 辅助降低游戏美术的创作门槛和成本，让独立开发者能够专注于游戏设计和玩法创新。产品定位为"专业级工具 + AI 增强"，而非纯 AI 生成器——保留手动编辑能力，确保输出的资产符合游戏引擎的技术要求。

---

<div id="research"></div>

## 用户研究


### 用户洞察

**洞察一：风格一致性比单张质量更重要**

通过对 47 位独立开发者的访谈发现，85% 的受访者表示"风格不统一"是使用 AI 生成资产的最大障碍。Midjourney 生成的单张图片质量很高，但批量生成时风格漂移严重，导致游戏内资产视觉混乱。用户需要的是可控的、风格一致的批量生成能力。

**洞察二：游戏引擎的技术规格是硬性约束**

与通用设计工具不同，游戏资产必须满足严格的技术约束：sprite sheet 的帧序列排布、纹理尺寸的 2 的幂次要求、法线贴图的通道格式、LOD 层级的尺寸规范等。任何不满足这些约束的资产都无法直接导入引擎使用。

**洞察三：现有工具链断裂严重**

开发者的工作流程通常横跨 4-6 个工具：用 Midjourney 生成概念图，用 Photoshop 手动修图和调整尺寸，用 Aseprite 制作像素 sprite，用 Blender 建模，最后在 Unity/Unreal 中组装。工具之间缺乏数据流通，每次导出和导入都伴随着格式转换和信息丢失。

**洞察四：迭代速度决定创意上限**

在 Game Jam 和原型验证阶段，开发者需要快速尝试不同的视觉方向。当每次风格调整需要 2-3 天的外包沟通时，开发者倾向于接受"够用就好"的方案，放弃了更优的创意可能性。AI 辅助的即时反馈循环可以将迭代周期从天缩短到分钟。

**洞察五：学习曲线是隐形门槛**

Blender、Photoshop 等专业工具的学习曲线对非美术背景的开发者构成了实质性障碍。62% 的受访者表示"不熟悉专业美术工具的操作"是他们选择外包而非自学的主要原因。工具需要在专业能力和易用性之间找到平衡点。

### 竞品分析

| 维度 | Aseprite | Blender | Midjourney | Unity Asset Store | PixelForge |
|------|----------|---------|------------|-------------------|------------|
| AI 生成 | 无 | 插件支持 | 核心功能 | 无 | 核心功能 |
| 游戏就绪 | 像素专用 | 3D 专用 | 需手动处理 | 即用型 | 资产直接可用 |
| 价格 | $20 买断 | 免费开源 | $10-60/月 | 按资产计费 | $15/月订阅 |
| 工作流整合 | 独立工具 | 独立工具 | 独立工具 | 引擎内 | 引擎插件导出 |
| 学习曲线 | 中等 | 陡峭 | 低 | 低 | 低 |
| 风格控制 | 手动 | 手动 | 提示词 | 无 | 提示词+手动编辑 |
| 批量生成 | 无 | 无 | 有限 | 无 | 支持 |
| 输出格式 | PNG/GIF | FBX/OBJ | PNG | 多格式 | PNG/Sprite/FBX/Atlas |

**竞品定位洞察：** 市场上缺乏一个同时具备 AI 生成能力、游戏资产技术约束处理、和引擎导出整合的工具。现有方案要么擅长 AI 生成但不懂游戏规格（Midjourney），要么是专业工具但无 AI 能力（Aseprite/Blender）。PixelForge 填补的是"AI 生成 + 游戏就绪 + 工作流整合"的交叉地带。

### 痛点优先级矩阵

| 痛点 | 频率 | 严重度 | 技术可行性 | 优先级 |
|------|------|--------|------------|--------|
| 美术资产成本高 | 极高 | 严重 | 高 | P0 |
| 风格不一致 | 高 | 严重 | 中 | P0 |
| 迭代周期长 | 高 | 高 | 高 | P0 |
| 工具链断裂 | 中 | 高 | 中 | P1 |
| 技术规格约束 | 中 | 中 | 高 | P1 |
| 学习曲线陡峭 | 中 | 中 | 高 | P2 |

---

<div id="architecture"></div>

## 信息架构


### 产品架构

PixelForge 采用 Web 应用架构，核心模块划分为五个功能区域：

```
┌─────────────────────────────────────────────────────────┐
│                     菜单栏 & 全局导航                      │
├──────┬──────────────────────────────────┬───────────────┤
│      │                                  │               │
│ 工具栏 │         主画布区域                 │   属性面板    │
│      │       （Workbench / AI Studio）    │  （图层/参数）│
│ 选择  │                                  │               │
│ 画笔  │                                  │               │
│ 橡皮  │                                  │               │
│ 填充  │                                  │               │
│ 取样  │                                  │               │
│      │                                  │               │
├──────┴──────────────────────────────────┴───────────────┤
│              底部面板（资产库 / 导出中心 / 时间轴）           │
└─────────────────────────────────────────────────────────┘
```

**五大功能模块：**

1. **Workbench（工作台）**：核心编辑区域，提供像素画笔、选区、变换、图层管理等专业编辑工具。支持无限画布、多图层混合模式、参考线和网格对齐。

2. **AI Studio（AI 工作室）**：AI 生成和编辑的核心界面。包含提示词输入区、风格预设库、生成参数调节、变体对比和批量生成队列。

3. **Asset Library（资产库）**：统一管理所有生成和导入的资产。支持标签分类、版本管理、风格标记和跨项目复用。

4. **Export Center（导出中心）**：将资产转换为目标引擎的技术规格。内置 Unity Sprite Atlas 生成器、Unreal Material 配置器和通用纹理压缩器。

5. **Project Settings（项目设置）**：管理项目级别的配置，包括目标引擎版本、纹理格式偏好、默认导出路径和 AI 模型选择。

### 核心用户流程

```
用户输入需求描述
│
▼
AI Studio 生成资产变体（4-8 个）
│
▼
用户选择满意的变体 → 拖入 Workbench
│
▼
手动精修（调整细节/风格统一/技术规格适配）
│
▼
Asset Library 存档管理
│
▼
Export Center 导出到游戏引擎
```

### 专业工具栏设计

参考 Figma 和 Photoshop 的工具栏模式，左侧工具栏采用双层结构：

- **第一层（图标栏）**：选择、画笔、橡皮、填充、取样、文字、形状、变换
- **第二层（属性栏）**：根据当前工具动态显示相关参数（画笔大小、硬度、透明度、混合模式等）

顶部菜单栏包含：File（项目管理）、Edit（编辑操作）、View（视图控制）、AI（生成与编辑）、Export（导出选项）、Help（文档与快捷键）。

---

<div id="wireframe"></div>

## 线框图


### 线框图一：主工作台

主工作台采用经典的三栏布局。

<div class="my-10 rounded-xl border-2 border-gray-400 overflow-hidden bg-zinc-900">
<div class="h-8 bg-zinc-800 flex items-center px-3 gap-3 border-b border-zinc-700">
<div class="h-3 bg-zinc-600 rounded w-16"></div>
<div class="flex gap-2 ml-4">
<div class="h-3 bg-zinc-700 rounded w-8"></div>
<div class="h-3 bg-zinc-700 rounded w-8"></div>
<div class="h-3 bg-zinc-700 rounded w-8"></div>
<div class="h-3 bg-zinc-700 rounded w-8"></div>
</div>
</div>
<div class="flex h-[420px]">
<div class="w-10 bg-zinc-800 border-r border-zinc-700 flex flex-col items-center py-2 gap-2">
<div class="w-5 h-5 bg-zinc-600 rounded"></div>
<div class="w-5 h-5 bg-zinc-700 rounded"></div>
<div class="w-5 h-5 bg-zinc-700 rounded"></div>
<div class="w-5 h-5 bg-zinc-700 rounded"></div>
<div class="w-5 h-5 bg-zinc-700 rounded"></div>
<div class="w-5 h-5 bg-zinc-700 rounded"></div>
</div>
<div class="w-44 bg-zinc-800 border-r border-zinc-700 p-2 space-y-2">
<div class="h-2 bg-zinc-500 rounded w-16 mb-1"></div>
<div class="h-5 bg-zinc-700 rounded"></div>
<div class="h-5 bg-zinc-700 rounded"></div>
<div class="h-2 bg-zinc-500 rounded w-12 mt-2 mb-1"></div>
<div class="h-5 bg-zinc-700 rounded"></div>
</div>
<div class="flex-1 bg-zinc-950 flex items-center justify-center relative">
<div class="w-32 h-32 bg-zinc-800 border border-zinc-700 rounded" style="background-image: repeating-conic-gradient(#27272a 0% 25%, #18181b 0% 50%); background-size: 8px 8px;"></div>
<div class="absolute top-2 right-2 text-[8px] text-zinc-500">128×128 — 60%</div>
</div>
<div class="w-52 bg-zinc-800 border-l border-zinc-700 p-2 space-y-2">
<div class="h-2 bg-zinc-500 rounded w-12 mb-1"></div>
<div class="h-5 bg-zinc-700 rounded"></div>
<div class="h-5 bg-zinc-700 rounded"></div>
<div class="h-5 bg-zinc-700 rounded"></div>
<div class="h-2 bg-zinc-500 rounded w-12 mt-2 mb-1"></div>
<div class="h-16 bg-zinc-700 rounded"></div>
</div>
</div>
<div class="h-20 bg-zinc-800 border-t border-zinc-700 p-2 flex gap-1">
<div class="w-10 h-10 bg-zinc-700 rounded"></div>
<div class="w-10 h-10 bg-zinc-700 rounded"></div>
<div class="w-10 h-10 bg-zinc-700 rounded"></div>
<div class="w-10 h-10 bg-zinc-700 rounded"></div>
<div class="w-10 h-10 bg-zinc-700 rounded"></div>
</div>
</div>

### 线框图二：AI 生成面板

AI 生成面板采用左右分割布局。

<div class="my-10 rounded-xl border-2 border-gray-400 overflow-hidden bg-zinc-900">
<div class="h-8 bg-zinc-800 flex items-center px-3 gap-3 border-b border-zinc-700">
<div class="h-3 bg-zinc-600 rounded w-16"></div>
<div class="flex gap-2 ml-4">
<div class="h-3 bg-zinc-700 rounded w-12"></div>
<div class="h-3 bg-zinc-700 rounded w-12"></div>
</div>
</div>
<div class="flex h-[420px]">
<div class="w-2/5 bg-zinc-800 border-r border-zinc-700 p-4 space-y-3">
<div class="h-2 bg-zinc-500 rounded w-16 mb-1"></div>
<div class="h-20 bg-zinc-700 rounded-lg p-2">
<div class="h-2 bg-zinc-500 rounded w-full mb-1"></div>
<div class="h-2 bg-zinc-600 rounded w-3/4"></div>
</div>
<div class="h-2 bg-zinc-500 rounded w-20 mb-1"></div>
<div class="grid grid-cols-3 gap-1.5">
<div class="h-12 bg-zinc-700 rounded border border-zinc-600"></div>
<div class="h-12 bg-zinc-700 rounded border border-fuchsia-500"></div>
<div class="h-12 bg-zinc-700 rounded border border-zinc-600"></div>
<div class="h-12 bg-zinc-700 rounded border border-zinc-600"></div>
<div class="h-12 bg-zinc-700 rounded border border-zinc-600"></div>
<div class="h-12 bg-zinc-700 rounded border border-zinc-600"></div>
</div>
<div class="h-8 bg-fuchsia-600 rounded-lg flex items-center justify-center">
<div class="h-2 bg-white/50 rounded w-16"></div>
</div>
</div>
<div class="flex-1 bg-zinc-850 p-4">
<div class="grid grid-cols-3 gap-2 h-full">
<div class="bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="bg-zinc-800 rounded-lg border border-fuchsia-500"></div>
<div class="bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="bg-zinc-800 rounded-lg border border-zinc-700"></div>
</div>
</div>
</div>
</div>

### 线框图三：资产库

资产库采用全屏浏览模式。

<div class="my-10 rounded-xl border-2 border-gray-400 overflow-hidden bg-zinc-900">
<div class="h-8 bg-zinc-800 flex items-center px-3 gap-3 border-b border-zinc-700">
<div class="h-3 bg-zinc-600 rounded w-16"></div>
<div class="h-5 bg-zinc-700 rounded flex-1 max-w-xs ml-4"></div>
</div>
<div class="flex h-[420px]">
<div class="w-44 bg-zinc-800 border-r border-zinc-700 p-2 space-y-1">
<div class="h-5 bg-zinc-700 rounded text-[8px] text-zinc-400 flex items-center px-2">角色</div>
<div class="h-5 bg-zinc-700 rounded text-[8px] text-zinc-400 flex items-center px-2 pl-4">环境</div>
<div class="h-5 bg-zinc-700 rounded text-[8px] text-zinc-400 flex items-center px-2 pl-4">UI</div>
<div class="h-5 bg-zinc-700 rounded text-[8px] text-zinc-400 flex items-center px-2 pl-4">特效</div>
<div class="h-5 bg-zinc-700 rounded text-[8px] text-zinc-400 flex items-center px-2">道具</div>
</div>
<div class="flex-1 p-3">
<div class="grid grid-cols-4 gap-2">
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
<div class="aspect-square bg-zinc-800 rounded-lg border border-zinc-700"></div>
</div>
</div>
</div>
</div>

---

<div id="visual"></div>

## 视觉设计


### 设计理念："Code Meets Canvas"

PixelForge 的视觉设计核心理念是"代码遇见画布"——在专业工具的精密感和创意软件的灵感感之间取得平衡。界面语言借鉴 IDE 的信息密度和清晰层级，同时保留游戏开发工具特有的视觉活力。

设计原则：
- **信息密度优先**：在不牺牲可读性的前提下最大化有效信息展示
- **暗色沉浸**：深色背景减少视觉干扰，让画布内容成为唯一焦点
- **精确的视觉层级**：通过色彩、间距和字体权重建立清晰的信息层级
- **功能可见性**：所有可交互元素都提供即时的视觉反馈

### 色彩系统

**主色 Magenta-Purple 渐变（品牌识别）：**
- Primary: `#D946EF`（品红）— 用于主要操作按钮、选中状态、品牌元素
- Secondary: `#A855F7`（紫色）— 用于辅助元素、渐变过渡、hover 状态
- 渐变方向：135deg，从 Primary 到 Secondary

**画布背景色（Dark Theme）：**
- Canvas Dark: `#18181B`（zinc-900）— 主画布背景
- Panel Dark: `#27272A`（zinc-800）— 面板和工具栏背景
- Border: `#3F3F46`（zinc-700）— 分割线和边框
- Surface: `#09090B`（zinc-950）— 最深层背景

**功能色：**
- Accent Cyan: `#06B6D4` — 用于 AI 相关功能标识（AI 按钮、生成进度、AI 标签）
- Success: `#22C55E` — 导出成功、操作完成
- Warning: `#F59E0B` — 参数警告、低质量提示
- Error: `#EF4444` — 错误状态、删除确认

**中性色阶：**
- 文字主色：`#FAFAFA`（zinc-50）
- 文字次要：`#A1A1AA`（zinc-400）
- 文字禁用：`#52525B`（zinc-600）

### 暗色主题设计决策

工具类应用默认采用深色主题，原因有三：第一，深色背景减少了界面元素对画布内容的视觉干扰，让创作者的注意力集中在资产本身；第二，深色主题降低了长时间工作的视觉疲劳，对需要持续数小时工作的游戏开发者至关重要；第三，深色界面与大多数游戏引擎（Unity、Unreal、Godot）的编辑器风格保持一致，降低了用户的认知切换成本。

### 字体系统

**UI 字体：Inter**
- 标题 H1：24px / Semi Bold / -0.02em 字间距
- 标题 H2：18px / Semi Bold / -0.01em 字间距
- 正文：14px / Regular / 1.5 行高
- 小字标签：12px / Medium / 0.01em 字间距
- 工具提示：11px / Regular

**代码/提示词字体：JetBrains Mono**
- 提示词输入框：14px / Regular / 1.6 行高
- 代码片段：13px / Regular
- 快捷键显示：12px / Medium

字体选择的理由：Inter 是专为屏幕阅读优化的无衬线字体，其 x-height 比例和字形设计在小尺寸下仍保持极佳的可读性，非常适合信息密度高的工具界面。JetBrains Mono 的等宽特性和连字支持使其成为代码和提示词输入的理想选择，其独特的字形设计（如 0 和 O 的区分）在技术内容展示中提供了额外的辨识度。

---

<div id="high-fidelity"></div>

## 高保真设计


### 高保真原型一：Workbench 主工作台（桌面端）

<div class="my-8 rounded-xl border border-zinc-700 overflow-hidden shadow-2xl bg-zinc-900">
<div class="h-9 bg-zinc-800 flex items-center px-4 gap-5 border-b border-zinc-700">
<span class="text-fuchsia-400 text-sm font-semibold tracking-tight">PixelForge</span>
<span class="text-zinc-400 text-xs hover:text-zinc-200 cursor-pointer">File</span>
<span class="text-zinc-400 text-xs hover:text-zinc-200 cursor-pointer">Edit</span>
<span class="text-zinc-400 text-xs hover:text-zinc-200 cursor-pointer">View</span>
<span class="text-cyan-400 text-xs font-medium hover:text-cyan-300 cursor-pointer">AI</span>
<span class="text-zinc-400 text-xs hover:text-zinc-200 cursor-pointer">Export</span>
<span class="text-zinc-400 text-xs hover:text-zinc-200 cursor-pointer">Help</span>
<div class="flex-1"></div>
<span class="text-zinc-500 text-[10px]">warrior_idle_v3.pxf — 128×128px — 60%</span>
<div class="flex items-center gap-2 ml-4">
<div class="w-5 h-5 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
</div>
<div class="w-5 h-5 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
</div>
</div>
</div>

<div class="flex h-[420px]">
<div class="w-10 bg-zinc-800 border-r border-zinc-700 flex flex-col items-center py-2 gap-1">
<div class="w-7 h-7 rounded bg-zinc-600 flex items-center justify-center cursor-pointer" title="Move">
<svg class="w-3.5 h-3.5 text-zinc-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-600 flex items-center justify-center cursor-pointer" title="Select">
<svg class="w-3.5 h-3.5 text-zinc-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/></svg>
</div>
<div class="w-7 h-7 rounded bg-fuchsia-600/80 flex items-center justify-center cursor-pointer ring-1 ring-fuchsia-400" title="Brush">
<svg class="w-3.5 h-3.5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600" title="Eraser">
<svg class="w-3.5 h-3.5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600" title="Fill">
<svg class="w-3.5 h-3.5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600" title="Eyedropper">
<svg class="w-3.5 h-3.5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600" title="Text">
<span class="text-zinc-400 text-xs font-bold">T</span>
</div>
<div class="w-7 h-7 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600" title="Shape">
<svg class="w-3.5 h-3.5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h12a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V6z"/></svg>
</div>
<div class="flex-1"></div>
<div class="w-7 h-7 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600 border-t border-zinc-600 pt-1" title="Color">
<div class="w-4 h-4 rounded-sm bg-fuchsia-500 border border-zinc-500"></div>
</div>
</div>

<div class="w-52 bg-zinc-800 border-r border-zinc-700 p-3 flex flex-col gap-3">
<div class="text-zinc-300 text-[11px] font-medium uppercase tracking-wider">Brush Settings</div>
<div class="flex flex-col gap-1.5">
<div class="flex justify-between items-center">
<span class="text-zinc-400 text-xs">Size</span>
<span class="text-zinc-200 text-xs font-mono">4px</span>
</div>
<div class="h-1 bg-zinc-700 rounded-full overflow-hidden">
<div class="h-full w-1/3 bg-gradient-to-r from-fuchsia-500 to-purple-500 rounded-full"></div>
</div>
</div>
<div class="flex flex-col gap-1.5">
<div class="flex justify-between items-center">
<span class="text-zinc-400 text-xs">Hardness</span>
<span class="text-zinc-200 text-xs font-mono">100%</span>
</div>
<div class="h-1 bg-zinc-700 rounded-full overflow-hidden">
<div class="h-full w-full bg-gradient-to-r from-fuchsia-500 to-purple-500 rounded-full"></div>
</div>
</div>
<div class="flex flex-col gap-1.5">
<div class="flex justify-between items-center">
<span class="text-zinc-400 text-xs">Opacity</span>
<span class="text-zinc-200 text-xs font-mono">85%</span>
</div>
<div class="h-1 bg-zinc-700 rounded-full overflow-hidden">
<div class="h-full w-4/5 bg-gradient-to-r from-fuchsia-500 to-purple-500 rounded-full"></div>
</div>
</div>
<div class="h-px bg-zinc-700 my-1"></div>
<div class="text-zinc-300 text-[11px] font-medium uppercase tracking-wider">Pressure</div>
<div class="flex items-center gap-2">
<div class="w-4 h-4 rounded border border-zinc-600 bg-fuchsia-600/30 flex items-center justify-center">
<svg class="w-2.5 h-2.5 text-fuchsia-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
</div>
<span class="text-zinc-400 text-xs">Size pressure</span>
</div>
<div class="flex items-center gap-2">
<div class="w-4 h-4 rounded border border-zinc-600 flex items-center justify-center"></div>
<span class="text-zinc-500 text-xs">Opacity pressure</span>
</div>
<div class="h-px bg-zinc-700 my-1"></div>
<div class="text-zinc-300 text-[11px] font-medium uppercase tracking-wider">Blend Mode</div>
<div class="h-7 bg-zinc-700 rounded flex items-center px-2 justify-between cursor-pointer hover:bg-zinc-600">
<span class="text-zinc-300 text-xs">Normal</span>
<svg class="w-3 h-3 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
</div>
</div>

<div class="flex-1 bg-zinc-950 relative flex items-center justify-center overflow-hidden">
<div class="absolute inset-0 opacity-5" style="background-image: linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px); background-size: 16px 16px;"></div>
<div class="relative border border-zinc-600" style="width: 256px; height: 256px; background-image: linear-gradient(45deg, #1a1a2e 25%, transparent 25%), linear-gradient(-45deg, #1a1a2e 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #1a1a2e 75%), linear-gradient(-45deg, transparent 75%, #1a1a2e 75%); background-size: 32px 32px; background-position: 0 0, 0 16px, 16px -16px, -16px 0px;">
<div class="absolute inset-0 flex items-center justify-center">
<div class="relative">
<div class="w-20 h-28 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-10 h-10 bg-amber-400 rounded-sm"></div>
<div class="absolute top-3 left-5 w-1.5 h-1.5 bg-zinc-900 rounded-full"></div>
<div class="absolute top-3 right-5 w-1.5 h-1.5 bg-zinc-900 rounded-full"></div>
<div class="absolute top-10 left-1/2 -translate-x-1/2 w-8 h-10 bg-fuchsia-500 rounded-sm"></div>
<div class="absolute top-6 right-0 w-1 h-14 bg-zinc-300 rounded-sm transform rotate-12"></div>
<div class="absolute top-5 right-0 w-3 h-1.5 bg-amber-600 rounded-sm transform rotate-12"></div>
<div class="absolute bottom-0 left-3 w-3 h-6 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-3 w-3 h-6 bg-zinc-700 rounded-sm"></div>
</div>
</div>
</div>
<div class="absolute top-16 left-16 w-24 h-20 border border-dashed border-fuchsia-400 opacity-50"></div>
</div>
<div class="absolute bottom-3 right-3 flex items-center gap-2 bg-zinc-800/90 rounded px-2 py-1">
<span class="text-zinc-500 text-[10px] cursor-pointer hover:text-zinc-300">−</span>
<span class="text-zinc-300 text-[10px] font-mono">60%</span>
<span class="text-zinc-500 text-[10px] cursor-pointer hover:text-zinc-300">+</span>
</div>
<div class="absolute bottom-3 left-3 bg-zinc-800/90 rounded px-2 py-1">
<span class="text-zinc-400 text-[10px] font-mono">X: 64 Y: 80</span>
</div>
</div>

<div class="w-56 bg-zinc-800 border-l border-zinc-700 flex flex-col">
<div class="px-3 py-2 border-b border-zinc-700 flex items-center justify-between">
<span class="text-zinc-300 text-xs font-medium">Layers</span>
<div class="flex gap-1">
<div class="w-5 h-5 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
</div>
</div>
</div>
<div class="flex-1 overflow-y-auto p-2 flex flex-col gap-1">
<div class="flex items-center gap-2 px-2 py-1.5 rounded bg-zinc-700/50 cursor-pointer">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
<div class="w-6 h-6 rounded-sm bg-zinc-600 border border-zinc-500 flex-shrink-0"></div>
<span class="text-zinc-200 text-xs truncate">Sword</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded bg-fuchsia-600/20 ring-1 ring-fuchsia-500/40 cursor-pointer">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
<div class="w-6 h-6 rounded-sm bg-fuchsia-500 border border-zinc-500 flex-shrink-0"></div>
<span class="text-zinc-100 text-xs truncate">Body</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded bg-zinc-700/50 cursor-pointer">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
<div class="w-6 h-6 rounded-sm bg-amber-400 border border-zinc-500 flex-shrink-0"></div>
<span class="text-zinc-200 text-xs truncate">Head</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded bg-zinc-700/50 cursor-pointer">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
<div class="w-6 h-6 rounded-sm bg-zinc-600 border border-zinc-500 flex-shrink-0"></div>
<span class="text-zinc-200 text-xs truncate">Legs</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded bg-zinc-700/50 cursor-pointer">
<svg class="w-3 h-3 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/></svg></div>
<div class="w-6 h-6 rounded-sm bg-zinc-500 border border-zinc-500 flex-shrink-0 opacity-40"></div>
<span class="text-zinc-400 text-xs truncate line-through">Shadow</span>
</div>
</div>
<div class="border-t border-zinc-700">
<div class="flex">
<div class="flex-1 py-1.5 text-center text-[10px] text-zinc-400 cursor-pointer hover:text-zinc-200 border-b-2 border-fuchsia-500">Layers</div>
<div class="flex-1 py-1.5 text-center text-[10px] text-zinc-500 cursor-pointer hover:text-zinc-200 border-b-2 border-transparent">Colors</div>
<div class="flex-1 py-1.5 text-center text-[10px] text-zinc-500 cursor-pointer hover:text-zinc-200 border-b-2 border-transparent">History</div>
</div>
</div>
</div>
</div>

  <div class="h-20 bg-zinc-800 border-t border-zinc-700 flex items-center px-3 gap-2">
    <span class="text-zinc-500 text-[10px] uppercase tracking-wider mr-2">Recent</span>
    <div class="w-14 h-14 rounded bg-zinc-700 border border-zinc-600 flex items-center justify-center cursor-pointer hover:border-fuchsia-500 transition-colors">
      <div class="w-6 h-8 bg-fuchsia-600/60 rounded-sm"></div>
    </div>
    <div class="w-14 h-14 rounded bg-zinc-700 border border-zinc-600 flex items-center justify-center cursor-pointer hover:border-fuchsia-500 transition-colors">
      <div class="w-6 h-6 bg-cyan-600/60 rounded-sm"></div>
    </div>
    <div class="w-14 h-14 rounded bg-zinc-700 border border-zinc-600 flex items-center justify-center cursor-pointer hover:border-fuchsia-500 transition-colors">
      <div class="w-8 h-4 bg-green-600/60 rounded-sm"></div>
    </div>
    <div class="w-14 h-14 rounded bg-zinc-700 border border-zinc-600 flex items-center justify-center cursor-pointer hover:border-fuchsia-500 transition-colors">
      <div class="w-5 h-5 bg-amber-500/60 rounded-full"></div>
    </div>
    <div class="w-14 h-14 rounded bg-zinc-700 border border-zinc-600 flex items-center justify-center cursor-pointer hover:border-fuchsia-500 transition-colors">
      <div class="w-4 h-8 bg-red-500/60 rounded-sm"></div>
    </div>
    <div class="flex-1"></div>
    <div class="px-3 py-1.5 rounded bg-zinc-700 text-zinc-400 text-[10px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">+ Import</div>
  </div>
</div>

**Workbench 设计说明：** 采用三栏布局模式，左侧工具栏 + 属性面板提供完整的画笔控制。中央画布支持像素级精确编辑，checkerboard 背景清晰标识透明区域。右侧面板管理图层结构和历史记录。底部资产快速访问条支持拖拽到画布。整体暗色主题确保画布内容的视觉优先级。

### 高保真原型二：AI Generation Panel（桌面端）

<div class="my-8 rounded-xl border border-zinc-700 overflow-hidden shadow-2xl bg-zinc-900">
<div class="h-9 bg-zinc-800 flex items-center px-4 gap-5 border-b border-zinc-700">
<span class="text-fuchsia-400 text-sm font-semibold tracking-tight">PixelForge</span>
<span class="text-zinc-400 text-xs">File</span>
<span class="text-zinc-400 text-xs">Edit</span>
<span class="text-zinc-400 text-xs">View</span>
<span class="text-cyan-400 text-xs font-medium bg-cyan-400/10 px-2 py-0.5 rounded">AI</span>
<span class="text-zinc-400 text-xs">Export</span>
<div class="flex-1"></div>
<div class="flex items-center gap-1.5 bg-cyan-500/10 px-2 py-1 rounded">
<div class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></div>
<span class="text-cyan-400 text-[10px]">AI Engine Active</span>
</div>
</div>

<div class="flex h-[420px]">
<div class="w-[38%] bg-zinc-800 border-r border-zinc-700 p-4 flex flex-col gap-4 overflow-y-auto">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-zinc-300 text-xs font-medium uppercase tracking-wider">Prompt</span>
<span class="text-zinc-500 text-[10px]">Tab to autocomplete</span>
</div>
<div class="bg-zinc-900 rounded-lg border border-zinc-600 p-3 focus-within:border-cyan-500/50 transition-colors">
<div class="flex flex-wrap gap-1 mb-2">
<span class="px-1.5 py-0.5 rounded bg-fuchsia-500/20 text-fuchsia-300 text-[10px]">pixel art</span>
<span class="px-1.5 py-0.5 rounded bg-fuchsia-500/20 text-fuchsia-300 text-[10px]">warrior</span>
<span class="px-1.5 py-0.5 rounded bg-fuchsia-500/20 text-fuchsia-300 text-[10px]">idle animation</span>
</div>
<div class="text-zinc-300 text-xs leading-relaxed font-mono">
A pixel art warrior character with <span class="text-cyan-400">purple armor</span> and <span class="text-cyan-400">glowing sword</span>, 4-frame idle animation, <span class="text-zinc-500">fantasy RPG style, 128x128</span>
</div>
</div>
<div class="flex gap-2 mt-2">
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[10px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">+ Style Tag</div>
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[10px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">+ Size Tag</div>
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[10px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">+ Animation</div>
</div>
</div>

<div>
<span class="text-zinc-300 text-xs font-medium uppercase tracking-wider">Style Presets</span>
<div class="grid grid-cols-3 gap-2 mt-2">
<div class="aspect-square rounded-lg bg-zinc-700 border-2 border-fuchsia-500 flex flex-col items-center justify-center gap-1 cursor-pointer">
<div class="w-6 h-6 rounded bg-fuchsia-500/30"></div>
<span class="text-zinc-200 text-[9px]">Pixel</span>
</div>
<div class="aspect-square rounded-lg bg-zinc-700 border border-zinc-600 flex flex-col items-center justify-center gap-1 cursor-pointer hover:border-zinc-500">
<div class="w-6 h-6 rounded bg-cyan-500/30"></div>
<span class="text-zinc-400 text-[9px]">Hand-drawn</span>
</div>
<div class="aspect-square rounded-lg bg-zinc-700 border border-zinc-600 flex flex-col items-center justify-center gap-1 cursor-pointer hover:border-zinc-500">
<div class="w-6 h-6 rounded bg-amber-500/30"></div>
<span class="text-zinc-400 text-[9px]">Low-poly</span>
</div>
<div class="aspect-square rounded-lg bg-zinc-700 border border-zinc-600 flex flex-col items-center justify-center gap-1 cursor-pointer hover:border-zinc-500">
<div class="w-6 h-6 rounded bg-green-500/30"></div>
<span class="text-zinc-400 text-[9px]">Voxel</span>
</div>
<div class="aspect-square rounded-lg bg-zinc-700 border border-zinc-600 flex flex-col items-center justify-center gap-1 cursor-pointer hover:border-zinc-500">
<div class="w-6 h-6 rounded bg-red-500/30"></div>
<span class="text-zinc-400 text-[9px]">Anime</span>
</div>
<div class="aspect-square rounded-lg bg-zinc-700 border border-zinc-600 flex flex-col items-center justify-center gap-1 cursor-pointer hover:border-zinc-500">
<div class="w-6 h-6 rounded bg-purple-500/30"></div>
<span class="text-zinc-400 text-[9px]">Realistic</span>
</div>
</div>
</div>

<div>
<span class="text-zinc-300 text-xs font-medium uppercase tracking-wider">Settings</span>
<div class="mt-2 flex flex-col gap-2.5">
<div class="flex flex-col gap-1">
<div class="flex justify-between">
<span class="text-zinc-400 text-[11px]">Variants</span>
<span class="text-zinc-200 text-[11px] font-mono">6</span>
</div>
<div class="h-1 bg-zinc-700 rounded-full">
<div class="h-full w-3/5 bg-gradient-to-r from-cyan-500 to-cyan-400 rounded-full"></div>
</div>
</div>
<div class="flex flex-col gap-1">
<div class="flex justify-between">
<span class="text-zinc-400 text-[11px]">Guidance Scale</span>
<span class="text-zinc-200 text-[11px] font-mono">7.5</span>
</div>
<div class="h-1 bg-zinc-700 rounded-full">
<div class="h-full w-[70%] bg-gradient-to-r from-cyan-500 to-cyan-400 rounded-full"></div>
</div>
</div>
<div class="flex flex-col gap-1">
<div class="flex justify-between">
<span class="text-zinc-400 text-[11px]">Steps</span>
<span class="text-zinc-200 text-[11px] font-mono">30</span>
</div>
<div class="h-1 bg-zinc-700 rounded-full">
<div class="h-full w-1/2 bg-gradient-to-r from-cyan-500 to-cyan-400 rounded-full"></div>
</div>
</div>
<div class="flex justify-between items-center">
<span class="text-zinc-400 text-[11px]">Seed</span>
<div class="px-2 py-0.5 rounded bg-zinc-700 text-zinc-300 text-[10px] font-mono">42857</div>
</div>
<div class="flex justify-between items-center">
<span class="text-zinc-400 text-[11px]">Match project style</span>
<div class="w-7 h-4 rounded-full bg-cyan-500/80 cursor-pointer relative">
<div class="w-3 h-3 rounded-full bg-white absolute right-0.5 top-0.5"></div>
</div>
</div>
</div>
</div>

<button class="w-full py-2.5 rounded-lg bg-gradient-to-r from-fuchsia-600 to-purple-600 text-white text-sm font-medium hover:from-fuchsia-500 hover:to-purple-500 transition-all shadow-lg shadow-fuchsia-600/20">
Generate 6 Variants
</button>
<div class="text-center text-zinc-500 text-[10px]">Estimated: ~12 seconds</div>
</div>

<div class="flex-1 p-4 flex flex-col gap-3">
<div class="flex items-center justify-between">
<div class="flex items-center gap-2">
<span class="text-zinc-300 text-xs font-medium">Results</span>
<span class="px-1.5 py-0.5 rounded-full bg-zinc-700 text-zinc-400 text-[10px]">6 variants</span>
</div>
<div class="flex gap-1">
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[10px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">Regenerate All</div>
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[10px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">Save to Library</div>
</div>
</div>

<div class="grid grid-cols-3 gap-3 flex-1">
<div class="rounded-lg bg-zinc-700/50 border-2 border-fuchsia-500 p-2 cursor-pointer flex flex-col gap-1.5 relative">
<div class="absolute -top-1.5 -right-1.5 w-5 h-5 rounded-full bg-fuchsia-500 flex items-center justify-center">
<svg class="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
</div>
<div class="aspect-square rounded bg-zinc-800 flex items-center justify-center">
<div class="w-12 h-16 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-amber-400 rounded-sm"></div>
<div class="absolute top-6 left-1/2 -translate-x-1/2 w-5 h-7 bg-fuchsia-500 rounded-sm"></div>
<div class="absolute top-3 right-0 w-0.5 h-8 bg-zinc-300 rounded-sm transform rotate-12"></div>
<div class="absolute bottom-0 left-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="text-center text-zinc-200 text-[10px]">Variant A</div>
</div>

<div class="rounded-lg bg-zinc-700/30 border border-zinc-600 p-2 cursor-pointer flex flex-col gap-1.5 hover:border-zinc-500">
<div class="aspect-square rounded bg-zinc-800 flex items-center justify-center">
<div class="w-12 h-16 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-amber-400 rounded-sm"></div>
<div class="absolute top-6 left-1/2 -translate-x-1/2 w-5 h-7 bg-purple-600 rounded-sm"></div>
<div class="absolute top-4 left-0 w-0.5 h-8 bg-zinc-300 rounded-sm transform -rotate-12"></div>
<div class="absolute bottom-0 left-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="text-center text-zinc-400 text-[10px]">Variant B</div>
</div>

<div class="rounded-lg bg-zinc-700/30 border border-zinc-600 p-2 cursor-pointer flex flex-col gap-1.5 hover:border-zinc-500">
<div class="aspect-square rounded bg-zinc-800 flex items-center justify-center">
<div class="w-12 h-16 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-amber-300 rounded-sm"></div>
<div class="absolute top-6 left-1/2 -translate-x-1/2 w-5 h-7 bg-fuchsia-400 rounded-sm"></div>
<div class="absolute top-3 right-0 w-0.5 h-9 bg-cyan-300 rounded-sm transform rotate-6"></div>
<div class="absolute bottom-0 left-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="text-center text-zinc-400 text-[10px]">Variant C</div>
</div>

<div class="rounded-lg bg-zinc-700/30 border border-zinc-600 p-2 cursor-pointer flex flex-col gap-1.5 hover:border-zinc-500">
<div class="aspect-square rounded bg-zinc-800 flex items-center justify-center">
<div class="w-12 h-16 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-amber-500 rounded-sm"></div>
<div class="absolute top-6 left-1/2 -translate-x-1/2 w-5 h-7 bg-fuchsia-600 rounded-sm"></div>
<div class="absolute bottom-0 left-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="text-center text-zinc-400 text-[10px]">Variant D</div>
</div>

<div class="rounded-lg bg-zinc-700/30 border border-zinc-600 p-2 cursor-pointer flex flex-col gap-1.5 hover:border-zinc-500">
<div class="aspect-square rounded bg-zinc-800 flex items-center justify-center">
<div class="w-12 h-16 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-amber-400 rounded-sm"></div>
<div class="absolute top-6 left-1/2 -translate-x-1/2 w-5 h-7 bg-purple-500 rounded-sm"></div>
<div class="absolute top-4 right-0 w-0.5 h-7 bg-zinc-300 rounded-sm transform rotate-15"></div>
<div class="absolute bottom-0 left-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="text-center text-zinc-400 text-[10px]">Variant E</div>
</div>

<div class="rounded-lg bg-zinc-700/30 border border-zinc-600 p-2 cursor-pointer flex flex-col gap-1.5 hover:border-zinc-500">
<div class="aspect-square rounded bg-zinc-800 flex items-center justify-center">
<div class="w-12 h-16 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-amber-400 rounded-sm"></div>
<div class="absolute top-6 left-1/2 -translate-x-1/2 w-5 h-7 bg-fuchsia-500 rounded-sm"></div>
<div class="absolute bottom-0 left-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-2 h-4 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="text-center text-zinc-400 text-[10px]">Variant F</div>
</div>
</div>

<div class="flex items-center gap-3 pt-2 border-t border-zinc-700">
<button class="px-4 py-1.5 rounded-lg bg-fuchsia-600 text-white text-xs font-medium hover:bg-fuchsia-500 transition-colors">Edit Selected</button>
<button class="px-4 py-1.5 rounded-lg bg-zinc-700 text-zinc-300 text-xs hover:bg-zinc-600 transition-colors">Add to Canvas</button>
<button class="px-4 py-1.5 rounded-lg bg-zinc-700 text-zinc-300 text-xs hover:bg-zinc-600 transition-colors">Save to Library</button>
<div class="flex-1"></div>
<div class="flex items-center gap-1 text-zinc-500 text-[10px]">
<span>Style similarity:</span>
<div class="w-16 h-1 bg-zinc-700 rounded-full">
<div class="h-full w-[88%] bg-green-500 rounded-full"></div>
</div>
<span class="text-green-400">88%</span>
</div>
</div>
</div>
</div>
</div>

**AI Generation Panel 设计说明：** 左侧输入区将提示词分为标签和描述两层，支持自动补全。风格预设采用 6 宫格快速选择，降低提示词编写的门槛。参数滑块提供细粒度控制。右侧结果区以 2x3 网格展示 6 个变体，选中状态以品红色边框标识。底部操作栏支持将选中结果直接发送到画布或资产库。风格相似度指示器帮助用户评估生成结果与项目风格的一致性。

### 高保真原型三：Asset Library（桌面端）

<div class="my-8 rounded-xl border border-zinc-700 overflow-hidden shadow-2xl bg-zinc-900">
<div class="h-9 bg-zinc-800 flex items-center px-4 gap-5 border-b border-zinc-700">
<span class="text-fuchsia-400 text-sm font-semibold tracking-tight">PixelForge</span>
<span class="text-zinc-400 text-xs">File</span>
<span class="text-zinc-400 text-xs">Edit</span>
<span class="text-zinc-400 text-xs">View</span>
<span class="text-cyan-400 text-xs">AI</span>
<span class="text-zinc-400 text-xs">Export</span>
<div class="flex-1"></div>
<span class="text-zinc-500 text-[10px]">247 assets in project</span>
</div>

<div class="flex h-[420px]">
<div class="w-48 bg-zinc-800 border-r border-zinc-700 p-3 flex flex-col gap-1">
<div class="text-zinc-400 text-[10px] uppercase tracking-wider mb-1">Categories</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded bg-zinc-700 cursor-pointer">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
<span class="text-zinc-200 text-xs">All Assets</span>
<span class="ml-auto text-zinc-500 text-[10px]">247</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer hover:bg-zinc-700/50">
<span class="text-zinc-500 text-xs">📁</span>
<span class="text-zinc-400 text-xs">Characters</span>
<span class="ml-auto text-zinc-500 text-[10px]">58</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer hover:bg-zinc-700/50">
<span class="text-zinc-500 text-xs">📁</span>
<span class="text-zinc-400 text-xs">Environments</span>
<span class="ml-auto text-zinc-500 text-[10px]">82</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer hover:bg-zinc-700/50">
<span class="text-zinc-500 text-xs">📁</span>
<span class="text-zinc-400 text-xs">UI Elements</span>
<span class="ml-auto text-zinc-500 text-[10px]">45</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer hover:bg-zinc-700/50">
<span class="text-zinc-500 text-xs">📁</span>
<span class="text-zinc-400 text-xs">Props</span>
<span class="ml-auto text-zinc-500 text-[10px]">34</span>
</div>
<div class="flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer hover:bg-zinc-700/50">
<span class="text-zinc-500 text-xs">📁</span>
<span class="text-zinc-400 text-xs">VFX</span>
<span class="ml-auto text-zinc-500 text-[10px]">28</span>
</div>
<div class="h-px bg-zinc-700 my-2"></div>
<div class="text-zinc-400 text-[10px] uppercase tracking-wider mb-1">Tags</div>
<div class="flex flex-wrap gap-1">
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">warrior</span>
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">idle</span>
<span class="px-1.5 py-0.5 rounded bg-fuchsia-500/20 text-fuchsia-300 text-[9px]">AI-generated</span>
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">sword</span>
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">dungeon</span>
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">grass</span>
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">stone</span>
<span class="px-1.5 py-0.5 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600 hover:text-zinc-200">chest</span>
</div>
</div>

<div class="flex-1 flex flex-col">
<div class="px-4 py-2.5 border-b border-zinc-700 flex items-center gap-3">
<div class="flex-1 flex items-center gap-2 bg-zinc-800 rounded-lg px-3 py-1.5 border border-zinc-700 focus-within:border-fuchsia-500/50">
<svg class="w-3.5 h-3.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
<span class="text-zinc-500 text-xs">Search assets... (⌘K)</span>
</div>
<div class="flex items-center gap-2">
<div class="h-6 px-2 rounded bg-zinc-800 border border-zinc-700 flex items-center gap-1 cursor-pointer hover:border-zinc-500">
<span class="text-zinc-400 text-[10px]">Type</span>
<svg class="w-2.5 h-2.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
</div>
<div class="h-6 px-2 rounded bg-zinc-800 border border-zinc-700 flex items-center gap-1 cursor-pointer hover:border-zinc-500">
<span class="text-zinc-400 text-[10px]">Size</span>
<svg class="w-2.5 h-2.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
</div>
<div class="h-6 px-2 rounded bg-zinc-800 border border-zinc-700 flex items-center gap-1 cursor-pointer hover:border-zinc-500">
<span class="text-zinc-400 text-[10px]">Date</span>
<svg class="w-2.5 h-2.5 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
</div>
<div class="w-6 h-6 rounded bg-zinc-800 border border-zinc-700 flex items-center justify-center cursor-pointer hover:border-zinc-500">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
</div>
<div class="w-6 h-6 rounded bg-zinc-800 border border-zinc-700 flex items-center justify-center cursor-pointer hover:border-zinc-500">
<svg class="w-3 h-3 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg>
</div>
</div>
</div>

<div class="flex-1 p-4 overflow-y-auto">
<div class="grid grid-cols-5 gap-3">
<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group relative hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square bg-zinc-800 flex items-center justify-center p-3" style="background-color: #1a1a2e;">
<div class="w-10 h-14 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-5 h-5 bg-amber-400 rounded-sm"></div>
<div class="absolute top-5 left-1/2 -translate-x-1/2 w-4 h-6 bg-fuchsia-500 rounded-sm"></div>
<div class="absolute bottom-0 left-1 w-1.5 h-3 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-1.5 h-3 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">warrior_idle.png</div>
<div class="text-zinc-500 text-[9px]">128x128 · 2.3KB</div>
</div>
<div class="absolute inset-0 bg-zinc-900/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
<div class="w-7 h-7 rounded bg-zinc-800/90 flex items-center justify-center cursor-pointer hover:bg-zinc-700">
<svg class="w-3.5 h-3.5 text-zinc-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-800/90 flex items-center justify-center cursor-pointer hover:bg-zinc-700">
<svg class="w-3.5 h-3.5 text-zinc-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"/></svg>
</div>
<div class="w-7 h-7 rounded bg-zinc-800/90 flex items-center justify-center cursor-pointer hover:bg-zinc-700">
<svg class="w-3.5 h-3.5 text-zinc-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"/></svg>
</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #1a2332;">
<div class="w-14 h-10 bg-green-700/60 rounded-sm relative">
<div class="absolute top-1 left-1 w-2 h-2 bg-green-500 rounded-sm"></div>
<div class="absolute top-3 left-4 w-3 h-3 bg-green-600 rounded-sm"></div>
<div class="absolute bottom-1 right-2 w-2 h-1 bg-green-800 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">grass_tile.png</div>
<div class="text-zinc-500 text-[9px]">32x32 · 0.8KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #1e1a2e;">
<div class="w-10 h-10 bg-amber-600/60 rounded relative">
<div class="absolute top-2 left-1/2 -translate-x-1/2 w-4 h-0.5 bg-amber-800 rounded"></div>
<div class="absolute bottom-2 left-1/2 -translate-x-1/2 w-2 h-2 bg-amber-800 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">treasure_chest.png</div>
<div class="text-zinc-500 text-[9px]">64x64 · 1.5KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #2e1a1a;">
<div class="w-8 h-12 bg-red-500/60 rounded-sm relative">
<div class="absolute top-1 left-1/2 -translate-x-1/2 w-3 h-3 bg-red-400/80 rounded-full"></div>
<div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-4 h-1 bg-red-700 rounded"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">fire_effect.png</div>
<div class="text-zinc-500 text-[9px]">64x64 · 1.2KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #1a2e2e;">
<div class="w-12 h-4 bg-cyan-600/60 rounded-sm relative">
<div class="absolute inset-y-0 left-0 w-3 bg-cyan-400/80 rounded-l-sm"></div>
<div class="absolute top-0.5 right-1 w-1 h-1 bg-cyan-300 rounded-full"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">health_bar.png</div>
<div class="text-zinc-500 text-[9px]">128x32 · 0.9KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #2e2e1a;">
<div class="w-10 h-10 bg-stone-500/60 rounded-sm relative">
<div class="absolute top-0 left-0 w-full h-2 bg-stone-600/80 rounded-t-sm"></div>
<div class="absolute bottom-0 left-0 w-2 h-4 bg-stone-400/60 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">stone_wall.png</div>
<div class="text-zinc-500 text-[9px]">64x64 · 1.1KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #1a1a2e;">
<div class="w-6 h-12 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-4 h-4 bg-amber-400 rounded-sm"></div>
<div class="absolute top-4 left-1/2 -translate-x-1/2 w-4 h-5 bg-purple-600 rounded-sm"></div>
<div class="absolute bottom-0 left-0 w-2 h-3 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-0 w-2 h-3 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">mage_idle.png</div>
<div class="text-zinc-500 text-[9px]">128x128 · 2.8KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #1a2e1a;">
<div class="w-12 h-8 bg-green-800/60 rounded-sm relative">
<div class="absolute top-1 left-1 w-3 h-3 bg-green-600/80 rounded-sm"></div>
<div class="absolute top-1 right-1 w-2 h-4 bg-green-600/60 rounded-sm"></div>
<div class="absolute bottom-1 left-3 w-6 h-2 bg-green-700/80 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">tree_tileset.png</div>
<div class="text-zinc-500 text-[9px]">128x128 · 3.2KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #2e1a2e;">
<div class="w-10 h-10 bg-purple-500/40 rounded-full flex items-center justify-center">
<div class="w-4 h-4 bg-purple-300/60 rounded-full"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">magic_orb.png</div>
<div class="text-zinc-500 text-[9px]">64x64 · 1.4KB</div>
</div>
</div>

<div class="rounded-lg bg-zinc-800 border border-zinc-700 overflow-hidden cursor-pointer group hover:border-fuchsia-500/50 transition-all">
<div class="aspect-square flex items-center justify-center p-3" style="background-color: #1a1a2e;">
<div class="w-10 h-14 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-5 h-5 bg-amber-400 rounded-sm"></div>
<div class="absolute top-5 left-1/2 -translate-x-1/2 w-4 h-6 bg-emerald-600 rounded-sm"></div>
<div class="absolute bottom-0 left-1 w-1.5 h-3 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-1 w-1.5 h-3 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="px-2 py-1.5">
<div class="text-zinc-200 text-[10px] truncate">ranger_idle.png</div>
<div class="text-zinc-500 text-[9px]">128x128 · 2.1KB</div>
</div>
</div>
</div>
</div>

<div class="px-4 py-1.5 border-t border-zinc-700 flex items-center justify-between">
<span class="text-zinc-500 text-[10px]">Showing 10 of 247 assets</span>
<div class="flex items-center gap-3">
<span class="text-zinc-500 text-[10px]">Total: 24.6 MB</span>
<div class="flex gap-1">
<div class="w-5 h-5 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600">
<svg class="w-2.5 h-2.5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
</div>
<span class="text-zinc-400 text-[10px] px-1">1 / 25</span>
<div class="w-5 h-5 rounded bg-zinc-700 flex items-center justify-center cursor-pointer hover:bg-zinc-600">
<svg class="w-2.5 h-2.5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

**Asset Library 设计说明：** 左侧分类导航提供树形结构和标签筛选，支持按项目、类型、风格多维度浏览。顶部搜索栏支持快捷键唤起，筛选器行提供类型、尺寸、日期的快速过滤。资产网格根据内容类型自适应缩略图展示，hover 时显示编辑、导出、删除等快捷操作。底部状态栏显示资产统计和分页信息。

### 高保真原型四：Mobile Companion（移动端）

<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-zinc-700 overflow-hidden shadow-2xl bg-zinc-900">
<div class="h-7 bg-zinc-800 flex items-center justify-between px-4 border-b border-zinc-700">
<span class="text-zinc-400 text-[10px] font-medium">9:41</span>
<div class="flex items-center gap-1">
<svg class="w-3 h-3 text-zinc-400" fill="currentColor" viewBox="0 0 24 24"><path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3c-1.65-1.66-4.34-1.66-6 0zm-4-4l2 2c2.76-2.76 7.24-2.76 10 0l2-2C15.14 9.14 8.87 9.14 5 13z"/></svg>
<svg class="w-3 h-3 text-zinc-400" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
</div>
</div>

<div class="h-11 bg-zinc-800 flex items-center px-3 border-b border-zinc-700 gap-3">
<svg class="w-5 h-5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
<span class="text-zinc-200 text-sm font-medium flex-1">Asset Library</span>
<svg class="w-5 h-5 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
<div class="w-5 h-5 rounded-full bg-gradient-to-r from-fuchsia-500 to-purple-500 flex items-center justify-center">
<span class="text-white text-[8px] font-bold">K</span>
</div>
</div>

<div class="flex border-b border-zinc-700">
<div class="flex-1 py-2 text-center text-[11px] text-zinc-400 cursor-pointer">Browse</div>
<div class="flex-1 py-2 text-center text-[11px] text-zinc-200 font-medium border-b-2 border-fuchsia-500 cursor-pointer">AI Generate</div>
<div class="flex-1 py-2 text-center text-[11px] text-zinc-400 cursor-pointer">Approvals</div>
</div>

<div class="p-3 flex flex-col gap-3">
<div>
<div class="flex items-center justify-between mb-2">
<span class="text-zinc-300 text-xs font-medium">Recent Generations</span>
<span class="text-fuchsia-400 text-[10px]">See All</span>
</div>
<div class="flex gap-2 overflow-x-auto pb-1">
<div class="w-20 h-20 flex-shrink-0 rounded-lg bg-zinc-800 border border-fuchsia-500/50 flex items-center justify-center">
<div class="w-8 h-10 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-4 h-4 bg-amber-400 rounded-sm"></div>
<div class="absolute top-4 left-1/2 -translate-x-1/2 w-3 h-5 bg-fuchsia-500 rounded-sm"></div>
<div class="absolute bottom-0 left-0.5 w-1.5 h-2 bg-zinc-700 rounded-sm"></div>
<div class="absolute bottom-0 right-0.5 w-1.5 h-2 bg-zinc-700 rounded-sm"></div>
</div>
</div>
<div class="w-20 h-20 flex-shrink-0 rounded-lg bg-zinc-800 border border-zinc-700 flex items-center justify-center">
<div class="w-10 h-6 bg-green-700/60 rounded-sm"></div>
</div>
<div class="w-20 h-20 flex-shrink-0 rounded-lg bg-zinc-800 border border-zinc-700 flex items-center justify-center">
<div class="w-8 h-8 bg-amber-600/60 rounded"></div>
</div>
<div class="w-20 h-20 flex-shrink-0 rounded-lg bg-zinc-800 border border-zinc-700 flex items-center justify-center">
<div class="w-6 h-10 bg-red-500/60 rounded-sm"></div>
</div>
</div>
</div>

<div class="bg-zinc-800 rounded-lg p-3">
<div class="flex items-center gap-2 mb-2">
<div class="w-1.5 h-1.5 rounded-full bg-amber-400"></div>
<span class="text-zinc-300 text-xs font-medium">Pending Approval</span>
<span class="ml-auto px-1.5 py-0.5 rounded-full bg-amber-400/20 text-amber-300 text-[9px]">3 items</span>
</div>
<div class="space-y-2">
<div class="flex items-center gap-2.5 p-2 rounded bg-zinc-700/50 cursor-pointer">
<div class="w-10 h-10 rounded bg-zinc-700 flex items-center justify-center flex-shrink-0">
<div class="w-5 h-7 relative">
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-3 h-3 bg-amber-400 rounded-sm"></div>
<div class="absolute top-3 left-1/2 -translate-x-1/2 w-3 h-4 bg-fuchsia-500 rounded-sm"></div>
</div>
</div>
<div class="flex-1 min-w-0">
<div class="text-zinc-200 text-[11px] truncate">warrior_attack_01.png</div>
<div class="text-zinc-500 text-[9px]">Generated by AI · 3 hours ago</div>
</div>
<div class="flex gap-1">
<div class="w-6 h-6 rounded-full bg-green-500/20 flex items-center justify-center">
<svg class="w-3 h-3 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
</div>
<div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center">
<svg class="w-3 h-3 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
</div>
</div>
</div>
<div class="flex items-center gap-2.5 p-2 rounded bg-zinc-700/50 cursor-pointer">
<div class="w-10 h-10 rounded bg-zinc-700 flex items-center justify-center flex-shrink-0">
<div class="w-8 h-5 bg-green-700/60 rounded-sm"></div>
</div>
<div class="flex-1 min-w-0">
<div class="text-zinc-200 text-[11px] truncate">grass_tile_v2.png</div>
<div class="text-zinc-500 text-[9px]">Generated by AI · 5 hours ago</div>
</div>
<div class="flex gap-1">
<div class="w-6 h-6 rounded-full bg-green-500/20 flex items-center justify-center">
<svg class="w-3 h-3 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
</div>
<div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center">
<svg class="w-3 h-3 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
</div>
</div>
</div>
<div class="flex items-center gap-2.5 p-2 rounded bg-zinc-700/50 cursor-pointer">
<div class="w-10 h-10 rounded bg-zinc-700 flex items-center justify-center flex-shrink-0">
<div class="w-6 h-6 bg-purple-500/40 rounded-full"></div>
</div>
<div class="flex-1 min-w-0">
<div class="text-zinc-200 text-[11px] truncate">magic_orb_v3.png</div>
<div class="text-zinc-500 text-[9px]">Generated by AI · Yesterday</div>
</div>
<div class="flex gap-1">
<div class="w-6 h-6 rounded-full bg-green-500/20 flex items-center justify-center">
<svg class="w-3 h-3 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
</div>
<div class="w-6 h-6 rounded-full bg-red-500/20 flex items-center justify-center">
<svg class="w-3 h-3 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
</div>
</div>
</div>
</div>
</div>

<div class="bg-zinc-800 rounded-lg p-3">
<span class="text-zinc-400 text-[10px] uppercase tracking-wider">Quick Generate</span>
<div class="mt-2 flex items-center gap-2 bg-zinc-900 rounded-lg px-3 py-2 border border-zinc-700">
<svg class="w-4 h-4 text-cyan-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
<span class="text-zinc-500 text-xs">Describe an asset...</span>
</div>
<div class="mt-2 flex gap-1.5">
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600">+ Character</div>
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600">+ Tile</div>
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600">+ UI</div>
<div class="px-2 py-1 rounded bg-zinc-700 text-zinc-400 text-[9px] cursor-pointer hover:bg-zinc-600">+ VFX</div>
</div>
</div>
</div>

<div class="h-12 bg-zinc-800 border-t border-zinc-700 flex items-center justify-around px-4">
<div class="flex flex-col items-center gap-0.5">
<svg class="w-4 h-4 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
<span class="text-zinc-500 text-[8px]">Home</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-4 h-4 text-fuchsia-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
<span class="text-fuchsia-400 text-[8px] font-medium">Library</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-8 h-8 rounded-full bg-gradient-to-r from-fuchsia-500 to-purple-500 flex items-center justify-center -mt-2 shadow-lg shadow-fuchsia-500/30">
<svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
</div>
<span class="text-zinc-400 text-[8px]">Create</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<svg class="w-4 h-4 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
<span class="text-zinc-500 text-[8px]">Alerts</span>
</div>
<div class="flex flex-col items-center gap-0.5">
<div class="w-5 h-5 rounded-full bg-gradient-to-r from-fuchsia-500 to-purple-500"></div>
<span class="text-zinc-500 text-[8px]">Profile</span>
</div>
</div>
</div>

**Mobile Companion 设计说明：** 移动端采用简化布局，专注于资产浏览和 AI 生成审批两个核心场景。顶部标签栏在 Browse、AI Generate、Approvals 之间切换。近期生成结果以横向滚动卡片展示，待审批列表支持一键通过或拒绝。底部快捷生成入口提供轻量级的移动端 AI 创作体验。底部导航栏包含 Home、Library、Create（突出显示）、Alerts、Profile 五个入口。移动端定位为桌面端的伴侣应用，用于碎片化时间的资产管理和审批。

---

<div id="interaction"></div>

## 交互设计


### 画布交互

**缩放与平移：** 画布支持鼠标滚轮缩放（0.1x-32x）和中键拖拽平移。触控板用户支持双指缩放和滑动平移。缩放过程中自动对齐到像素网格（在 4x 以上缩放时显示像素网格线），确保像素级编辑的精确性。双击缩放适配到内容大小，Ctrl+0 重置为 100%。

**画笔压力感应：** 支持 Wacom 和 iPad 压力感应画笔。压力值映射到两个维度：笔触大小和透明度。在画笔属性面板中可以独立控制两个维度的压力响应曲线。同时支持倾斜感应（用于斜角笔刷效果）和速度感应（快速笔触自动减细）。

**快捷键体系：** 参考 Photoshop 的快捷键布局，同时为游戏开发常用操作增加了专属快捷键。B 画笔、E 橡皮、G 填充、I 取样、V 移动、M 选区、Space 拖拽画布、[ / ] 调整画笔大小。Ctrl+Z / Ctrl+Shift+Z 支持多步撤销重做。

### AI 交互

**提示词自动补全：** 输入时实时提供风格标签、资产类型、技术规格的补全建议。基于项目历史生成的资产和风格偏好，提供个性化的提示词推荐。例如，输入"warrior"时自动推荐"warrior idle"、"warrior attack"、"warrior run"等动画类型。

**风格迁移：** 从资产库中选择参考图片作为风格种子，AI 生成时自动匹配目标资产的色调、笔触风格和细节层级。支持多图混合风格（加权平均）和风格强度调节。

**批量生成：** 一键生成同一资产的多个变体（最多 12 个），支持设置变体约束条件（固定配色、固定尺寸、固定动画帧数等）。生成队列支持后台运行，用户可以继续编辑其他资产。生成完成后推送通知并自动添加到待审批列表。

### 资产管理交互

**拖拽到画布：** 从资产库直接拖拽资产到画布，自动创建新图层。拖拽过程中显示资产的缩略预览和尺寸信息。放置时支持对齐到像素网格和参考线。

**右键上下文菜单：** 右键点击资产提供快速操作菜单：编辑、复制、导出、重命名、删除、查看版本历史、在文件夹中显示、添加到收藏。

**键盘快捷操作：** 资产库支持方向键导航、Enter 打开、Delete 删除、Ctrl+C/V 复制粘贴、Ctrl+F 搜索聚焦。多选支持 Shift+Click 范围选择和 Ctrl+Click 逐个选择。

---

<div id="results"></div>

## 结果与反思


### 项目成果数据

经过 7 个月的设计和开发迭代，PixelForge 于 2025 年 9 月正式发布 Beta 版本，上线首月获得了超出预期的市场反馈：

- **资产制作效率提升 4 倍：** 对比传统外包流程，使用 PixelForge 的独立开发者从概念到可用资产的平均时间从 3 天缩短到 7 小时
- **美术成本降低 60%：** 用户平均每月在美术外包上的支出从 ¥3000 降至 ¥1200，部分轻度使用者完全消除了外包需求
- **月均创作量 300+：** 平台每月生成超过 300 个可发布级别的游戏资产，其中约 40% 被直接用于游戏项目
- **Unity 插件下载量 10K+：** Unity 插件上架两个月内获得 10000+ 次下载，用户评分 4.6/5.0

### 核心设计决策回顾

**决策一：保留手动编辑能力而非纯 AI 生成。** 这一决策最初受到质疑——为什么不做一个更简单的纯生成器？事实证明，手动编辑能力是专业用户选择 PixelForge 而非 Midjourney 的关键原因。游戏开发者需要精确控制每个像素，纯 AI 生成无法满足这种精度要求。

**决策二：默认暗色主题。** 用户测试表明，暗色主题下用户的工作时间平均延长了 40%，视觉疲劳反馈降低了 65%。深色界面与 Unity/Unreal 编辑器的视觉一致性也降低了工具切换的认知成本。

**决策三：Mobile Companion 的定位。** 移动端不提供完整的编辑功能，而是专注于浏览和审批。这个决策基于用户调研——90% 的编辑工作在桌面端完成，移动端的使用场景主要是碎片化时间的资产管理和团队协作审批。

### 设计挑战与解决方案

**挑战一：风格一致性。** AI 生成的资产风格漂移是最大的技术挑战。解决方案是引入"项目风格锚点"机制——用户锁定项目级别的风格参数（色调、笔触、细节层级），后续所有生成自动继承这些约束。

**挑战二：信息密度与可发现性的平衡。** 工具类应用需要在有限空间内暴露大量功能，但过多的 UI 元素会导致认知过载。解决方案是分层暴露——常用功能直接可见，高级功能通过展开面板和右键菜单提供，AI 辅助功能集中到独立的 AI Studio 标签页。

**挑战三：移动端的输入限制。** 移动端缺乏精确的鼠标输入，不适合像素级编辑。解决方案是重新定义移动端的使用场景——从"创作工具"转变为"审批和管理工具"，让移动端服务于桌面端的工作流而非独立运作。

### 与 Unity 开发经验的结合

这个项目是我 Unity 开发背景和 UI/UX 设计能力的深度融合。在设计 PixelForge 的导出流程时，Unity 的 SpriteAtlas、TextureImporter 和 Animator 系统的技术细节直接影响了工具的导出逻辑设计。在设计 Asset Library 的分类结构时，借鉴了 Unity Project 窗口的文件组织模式。在设计快捷键体系时，参考了 Unity 编辑器的快捷键布局，让用户在两个工具之间切换时保持肌肉记忆的一致性。

更重要的是，Unity 开发让我深刻理解了"工具如何服务于创作"——好的工具应该让开发者忘记工具本身的存在，专注于创意表达。这个理念贯穿了 PixelForge 的每一个设计决策。
