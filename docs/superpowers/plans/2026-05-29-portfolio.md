# 求职作品集实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 构建一个 Astro 多页面静态作品集网站，展示 UI/UX、Unity、AIGC 三个方向，中英双语，干净现代风格。

**架构：** Astro 框架 + Tailwind CSS 样式，静态生成。通过 URL 路径区分中英文（`/zh/` vs `/en/`）。项目数据存放在 `src/content/projects/` 目录，使用 Astro Content Collections 管理。

**技术栈：** Astro 5.x, Tailwind CSS 4.x, TypeScript

---

## 文件结构

```
d:\Portfolio\
├── astro.config.mjs              # Astro 配置（i18n、集成）
├── package.json                   # 依赖管理
├── tsconfig.json                  # TypeScript 配置
├── public/
│   └── favicon.svg                # 网站图标
├── src/
│   ├── layouts/
│   │   └── Base.astro             # 基础 HTML 布局（head、导航、footer）
│   ├── components/
│   │   ├── Navbar.astro           # 顶部导航栏（固定、语言切换）
│   │   ├── Footer.astro           # 页脚（GitHub 链接）
│   │   ├── ProjectCard.astro      # 项目卡片组件
│   │   └── LanguageSwitcher.astro # 中/EN 语言切换按钮
│   ├── pages/
│   │   ├── zh/
│   │   │   ├── index.astro        # 中文首页
│   │   │   ├── uiux.astro         # 中文 UI/UX 页
│   │   │   ├── unity.astro        # 中文 Unity 页
│   │   │   ├── aigc.astro         # 中文 AIGC 页
│   │   │   ├── about.astro        # 中文关于我
│   │   │   └── unity/
│   │   │       └── [slug].astro   # 中文项目详情（动态路由）
│   │   └── en/
│   │       ├── index.astro        # 英文首页
│   │       ├── uiux.astro         # 英文 UI/UX 页
│   │       ├── unity.astro        # 英文 Unity 页
│   │       ├── aigc.astro         # 英文 AIGC 页
│   │       ├── about.astro        # 英文关于我
│   │       └── unity/
│   │           └── [slug].astro   # 英文项目详情（动态路由）
│   ├── content/
│   │   └── config.ts              # Content Collection 定义
│   ├── data/
│   │   ├── site.ts                # 站点元数据（名字、定位、社交链接）
│   │   └── i18n.ts                # UI 翻译字符串
│   └── styles/
│       └── global.css             # Tailwind 入口 + 全局样式
└── docs/
    └── superpowers/
        ├── specs/
        │   └── 2026-05-29-portfolio-design.md
        └── plans/
            └── 2026-05-29-portfolio.md
```

---

### 任务 1：初始化 Astro 项目

**文件：**
- 创建：`package.json`
- 创建：`astro.config.mjs`
- 创建：`tsconfig.json`
- 创建：`src/styles/global.css`
- 创建：`public/favicon.svg`

- [ ] **步骤 1：创建 package.json**

```json
{
  "name": "portfolio",
  "type": "module",
  "version": "1.0.0",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  }
}
```

- [ ] **步骤 2：安装依赖**

运行：`cd d:/Portfolio && npm install astro@latest @astrojs/tailwind@latest tailwindcss@latest`

- [ ] **步骤 3：创建 astro.config.mjs**

```js
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
  },
});
```

- [ ] **步骤 4：创建 tsconfig.json**

```json
{
  "extends": "astro/tsconfigs/strict"
}
```

- [ ] **步骤 5：创建 src/styles/global.css**

```css
@import "tailwindcss";

@theme {
  --color-primary: #2563EB;
  --color-primary-hover: #1D4ED8;
  --color-bg: #FFFFFF;
  --color-bg-alt: #F8F9FA;
  --color-text: #1A1A1A;
  --color-text-muted: #6B7280;
  --color-border: #E5E7EB;
  --font-sans: "Inter", system-ui, -apple-system, sans-serif;
}

body {
  font-family: var(--font-sans);
  color: var(--color-text);
  background: var(--color-bg);
}
```

- [ ] **步骤 6：创建 public/favicon.svg**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="6" fill="#2563EB"/>
  <text x="16" y="22" text-anchor="middle" fill="white" font-size="18" font-family="sans-serif" font-weight="bold">P</text>
</svg>
```

- [ ] **步骤 7：验证构建**

运行：`cd d:/Portfolio && npm run build`
预期：构建成功，无报错

- [ ] **步骤 8：Commit**

```bash
git add package.json astro.config.mjs tsconfig.json src/styles/global.css public/favicon.svg
git commit -m "feat: initialize Astro project with Tailwind CSS"
```

---

### 任务 2：创建站点数据和 i18n 翻译

**文件：**
- 创建：`src/data/site.ts`
- 创建：`src/data/i18n.ts`

- [ ] **步骤 1：创建 src/data/site.ts**

```ts
export const site = {
  name: { zh: '你的名字', en: 'Your Name' },
  tagline: {
    zh: '游戏开发者 / UI设计师 / AIGC创作者',
    en: 'Game Developer / UI Designer / AIGC Creator',
  },
  github: 'https://github.com/yourusername',
  email: 'your@email.com',
  wechat: 'your_wechat',
};
```

- [ ] **步骤 2：创建 src/data/i18n.ts**

```ts
export const ui = {
  zh: {
    nav: {
      home: '首页',
      uiux: 'UI/UX 设计',
      unity: 'Unity 开发',
      aigc: 'AIGC 生成',
      about: '关于我',
    },
    home: {
      viewProject: '查看项目',
      moreSoon: '更多作品即将上线',
    },
    unity: {
      empty: '暂无项目',
    },
    project: {
      back: '返回列表',
      techStack: '技术栈',
    },
    about: {
      skills: '技能',
      contact: '联系方式',
    },
    empty: {
      title: '更多作品即将上线',
      subtitle: '敬请期待',
    },
    langSwitch: 'EN',
  },
  en: {
    nav: {
      home: 'Home',
      uiux: 'UI/UX Design',
      unity: 'Unity Dev',
      aigc: 'AIGC',
      about: 'About',
    },
    home: {
      viewProject: 'View Project',
      moreSoon: 'More projects coming soon',
    },
    unity: {
      empty: 'No projects yet',
    },
    project: {
      back: 'Back to list',
      techStack: 'Tech Stack',
    },
    about: {
      skills: 'Skills',
      contact: 'Contact',
    },
    empty: {
      title: 'More projects coming soon',
      subtitle: 'Stay tuned',
    },
    langSwitch: '中文',
  },
} as const;

export type Locale = keyof typeof ui;
```

- [ ] **步骤 3：Commit**

```bash
git add src/data/site.ts src/data/i18n.ts
git commit -m "feat: add site metadata and i18n translations"
```

---

### 任务 3：创建基础布局和导航组件

**文件：**
- 创建：`src/layouts/Base.astro`
- 创建：`src/components/Navbar.astro`
- 创建：`src/components/Footer.astro`
- 创建：`src/components/LanguageSwitcher.astro`

- [ ] **步骤 1：创建 src/components/LanguageSwitcher.astro**

```astro
---
const { lang, currentPath } = Astro.props;
const otherLang = lang === 'zh' ? 'en' : 'zh';
const otherLabel = lang === 'zh' ? 'EN' : '中文';
const newPath = currentPath.replace(`/${lang}/`, `/${otherLang}/`);
---

<a href={newPath} class="text-sm text-[var(--color-text-muted)] hover:text-[var(--color-primary)] transition-colors">
  {otherLabel}
</a>
```

- [ ] **步骤 2：创建 src/components/Navbar.astro**

```astro
---
import { site } from '../data/site';
import { ui } from '../data/i18n';
import LanguageSwitcher from './LanguageSwitcher.astro';

const { lang } = Astro.props;
const t = ui[lang];
const currentPath = Astro.url.pathname;

const navLinks = [
  { href: `/${lang}/unity`, label: t.nav.unity },
  { href: `/${lang}/uiux`, label: t.nav.uiux },
  { href: `/${lang}/aigc`, label: t.nav.aigc },
  { href: `/${lang}/about`, label: t.nav.about },
];
---

<nav class="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-md border-b border-[var(--color-border)]">
  <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
    <a href={`/${lang}/`} class="text-lg font-semibold text-[var(--color-text)]">
      {site.name[lang]}
    </a>
    <div class="flex items-center gap-6">
      {navLinks.map(link => (
        <a
          href={link.href}
          class={`text-sm transition-colors ${
            currentPath.startsWith(link.href)
              ? 'text-[var(--color-primary)] font-medium'
              : 'text-[var(--color-text-muted)] hover:text-[var(--color-text)]'
          }`}
        >
          {link.label}
        </a>
      ))}
      <LanguageSwitcher lang={lang} currentPath={currentPath} />
    </div>
  </div>
</nav>
```

- [ ] **步骤 3：创建 src/components/Footer.astro**

```astro
---
import { site } from '../data/site';

const { lang } = Astro.props;
---

<footer class="border-t border-[var(--color-border)] py-8 mt-16">
  <div class="max-w-6xl mx-auto px-6 flex items-center justify-between text-sm text-[var(--color-text-muted)]">
    <span>&copy; {new Date().getFullYear()} {site.name[lang]}</span>
    <a href={site.github} target="_blank" rel="noopener" class="hover:text-[var(--color-primary)] transition-colors">
      GitHub
    </a>
  </div>
</footer>
```

- [ ] **步骤 4：创建 src/layouts/Base.astro**

```astro
---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css';

const { lang, title } = Astro.props;
---

<!DOCTYPE html>
<html lang={lang}>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <title>{title}</title>
</head>
<body class="min-h-screen flex flex-col">
  <Navbar lang={lang} />
  <main class="flex-1 pt-16">
    <slot />
  </main>
  <Footer lang={lang} />
</body>
</html>
```

- [ ] **步骤 5：Commit**

```bash
git add src/layouts/Base.astro src/components/Navbar.astro src/components/Footer.astro src/components/LanguageSwitcher.astro
git commit -m "feat: add base layout, navbar, footer, and language switcher"
```

---

### 任务 4：创建首页

**文件：**
- 创建：`src/pages/zh/index.astro`
- 创建：`src/pages/en/index.astro`

- [ ] **步骤 1：创建 src/pages/zh/index.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { site } from '../../data/site';
import { ui } from '../../data/i18n';

const lang = 'zh';
const t = ui[lang];

const directions = [
  { href: '/zh/unity', title: 'Unity 游戏开发', desc: '互动体验与游戏创作', icon: '🎮' },
  { href: '/zh/uiux', title: 'UI/UX 设计', desc: '用户界面与体验设计', icon: '🎨' },
  { href: '/zh/aigc', title: 'AIGC 生成', desc: 'AI 驱动的创意内容', icon: '🤖' },
];
---

<Base lang={lang} title={site.name[lang]}>
  <!-- Hero -->
  <section class="min-h-[80vh] flex flex-col items-center justify-center text-center px-6">
    <h1 class="text-5xl font-bold mb-4">{site.name[lang]}</h1>
    <p class="text-xl text-[var(--color-text-muted)]">{site.tagline[lang]}</p>
  </section>

  <!-- 方向入口 -->
  <section class="max-w-6xl mx-auto px-6 pb-16">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      {directions.map(d => (
        <a href={d.href} class="group block p-8 rounded-xl border border-[var(--color-border)] hover:border-[var(--color-primary)] hover:shadow-lg transition-all">
          <div class="text-4xl mb-4">{d.icon}</div>
          <h2 class="text-xl font-semibold mb-2 group-hover:text-[var(--color-primary)] transition-colors">{d.title}</h2>
          <p class="text-[var(--color-text-muted)]">{d.desc}</p>
        </a>
      ))}
    </div>
  </section>
</Base>
```

- [ ] **步骤 2：创建 src/pages/en/index.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { site } from '../../data/site';
import { ui } from '../../data/i18n';

const lang = 'en';
const t = ui[lang];

const directions = [
  { href: '/en/unity', title: 'Unity Game Dev', desc: 'Interactive experiences & game creation', icon: '🎮' },
  { href: '/en/uiux', title: 'UI/UX Design', desc: 'User interface & experience design', icon: '🎨' },
  { href: '/en/aigc', title: 'AIGC Generation', desc: 'AI-powered creative content', icon: '🤖' },
];
---

<Base lang={lang} title={site.name[lang]}>
  <section class="min-h-[80vh] flex flex-col items-center justify-center text-center px-6">
    <h1 class="text-5xl font-bold mb-4">{site.name[lang]}</h1>
    <p class="text-xl text-[var(--color-text-muted)]">{site.tagline[lang]}</p>
  </section>

  <section class="max-w-6xl mx-auto px-6 pb-16">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      {directions.map(d => (
        <a href={d.href} class="group block p-8 rounded-xl border border-[var(--color-border)] hover:border-[var(--color-primary)] hover:shadow-lg transition-all">
          <div class="text-4xl mb-4">{d.icon}</div>
          <h2 class="text-xl font-semibold mb-2 group-hover:text-[var(--color-primary)] transition-colors">{d.title}</h2>
          <p class="text-[var(--color-text-muted)]">{d.desc}</p>
        </a>
      ))}
    </div>
  </section>
</Base>
```

- [ ] **步骤 3：验证构建**

运行：`cd d:/Portfolio && npm run build`
预期：构建成功，输出包含 `/zh/index.html` 和 `/en/index.html`

- [ ] **步骤 4：Commit**

```bash
git add src/pages/zh/index.astro src/pages/en/index.astro
git commit -m "feat: add homepage with hero and direction cards"
```

---

### 任务 5：创建空状态页面（UI/UX、AIGC）

**文件：**
- 创建：`src/pages/zh/uiux.astro`
- 创建：`src/pages/zh/aigc.astro`
- 创建：`src/pages/en/uiux.astro`
- 创建：`src/pages/en/aigc.astro`

- [ ] **步骤 1：创建 src/pages/zh/uiux.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { ui } from '../../data/i18n';

const lang = 'zh';
const t = ui[lang];
---

<Base lang={lang} title={`UI/UX 设计 - ${lang === 'zh' ? '作品集' : 'Portfolio'}`}>
  <section class="max-w-6xl mx-auto px-6 py-20 text-center">
    <div class="py-16">
      <div class="text-6xl mb-6">🎨</div>
      <h1 class="text-3xl font-bold mb-4">UI/UX 设计</h1>
      <p class="text-[var(--color-text-muted)] text-lg">{t.empty.title}</p>
      <p class="text-[var(--color-text-muted)] mt-2">{t.empty.subtitle}</p>
    </div>
  </section>
</Base>
```

- [ ] **步骤 2：创建 src/pages/zh/aigc.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { ui } from '../../data/i18n';

const lang = 'zh';
const t = ui[lang];
---

<Base lang={lang} title={`AIGC 生成 - ${lang === 'zh' ? '作品集' : 'Portfolio'}`}>
  <section class="max-w-6xl mx-auto px-6 py-20 text-center">
    <div class="py-16">
      <div class="text-6xl mb-6">🤖</div>
      <h1 class="text-3xl font-bold mb-4">AIGC 生成</h1>
      <p class="text-[var(--color-text-muted)] text-lg">{t.empty.title}</p>
      <p class="text-[var(--color-text-muted)] mt-2">{t.empty.subtitle}</p>
    </div>
  </section>
</Base>
```

- [ ] **步骤 3：创建 src/pages/en/uiux.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { ui } from '../../data/i18n';

const lang = 'en';
const t = ui[lang];
---

<Base lang={lang} title={`UI/UX Design - Portfolio`}>
  <section class="max-w-6xl mx-auto px-6 py-20 text-center">
    <div class="py-16">
      <div class="text-6xl mb-6">🎨</div>
      <h1 class="text-3xl font-bold mb-4">UI/UX Design</h1>
      <p class="text-[var(--color-text-muted)] text-lg">{t.empty.title}</p>
      <p class="text-[var(--color-text-muted)] mt-2">{t.empty.subtitle}</p>
    </div>
  </section>
</Base>
```

- [ ] **步骤 4：创建 src/pages/en/aigc.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { ui } from '../../data/i18n';

const lang = 'en';
const t = ui[lang];
---

<Base lang={lang} title={`AIGC Generation - Portfolio`}>
  <section class="max-w-6xl mx-auto px-6 py-20 text-center">
    <div class="py-16">
      <div class="text-6xl mb-6">🤖</div>
      <h1 class="text-3xl font-bold mb-4">AIGC Generation</h1>
      <p class="text-[var(--color-text-muted)] text-lg">{t.empty.title}</p>
      <p class="text-[var(--color-text-muted)] mt-2">{t.empty.subtitle}</p>
    </div>
  </section>
</Base>
```

- [ ] **步骤 5：Commit**

```bash
git add src/pages/zh/uiux.astro src/pages/zh/aigc.astro src/pages/en/uiux.astro src/pages/en/aigc.astro
git commit -m "feat: add empty state pages for UI/UX and AIGC"
```

---

### 任务 6：创建项目数据和 Content Collection

**文件：**
- 创建：`src/content/config.ts`
- 创建：`src/content/projects/project-1.mdx`
- 创建：`src/content/projects/project-2.mdx`
- 创建：`src/content/projects/project-3.mdx`

- [ ] **步骤 1：创建 src/content/config.ts**

```ts
import { defineCollection, z } from 'astro:content';

const projectsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.object({ zh: z.string(), en: z.string() }),
    description: z.object({ zh: z.string(), en: z.string() }),
    cover: z.string(),
    video: z.string(),
    tags: z.array(z.string()),
    order: z.number().default(0),
  }),
});

export const collections = {
  projects: projectsCollection,
};
```

- [ ] **步骤 2：创建占位项目数据 src/content/projects/project-1.mdx**

```mdx
---
title:
  zh: "示例项目一"
  en: "Sample Project One"
description:
  zh: "这是一个 Unity 游戏项目的示例描述。展示了核心玩法和技术亮点。"
  en: "This is a sample description for a Unity game project. Showcasing core gameplay and technical highlights."
cover: "/images/projects/placeholder-cover.jpg"
video: "/videos/placeholder-demo.mp4"
tags: ["Unity", "C#", "3D"]
order: 1
---

这是一个示例项目的内容区域。你可以在这里添加更详细的项目介绍。
```

- [ ] **步骤 3：创建 src/content/projects/project-2.mdx**

```mdx
---
title:
  zh: "示例项目二"
  en: "Sample Project Two"
description:
  zh: "第二个 Unity 项目示例，展示了不同的技术方向。"
  en: "A second Unity project sample, showcasing a different technical direction."
cover: "/images/projects/placeholder-cover.jpg"
video: "/videos/placeholder-demo.mp4"
tags: ["Unity", "Shader", "VFX"]
order: 2
---

第二个示例项目的内容区域。
```

- [ ] **步骤 4：创建 src/content/projects/project-3.mdx**

```mdx
---
title:
  zh: "示例项目三"
  en: "Sample Project Three"
description:
  zh: "第三个 Unity 项目示例。"
  en: "A third Unity project sample."
cover: "/images/projects/placeholder-cover.jpg"
video: "/videos/placeholder-demo.mp4"
tags: ["Unity", "UI", "Mobile"]
order: 3
---

第三个示例项目的内容区域。
```

- [ ] **步骤 5：Commit**

```bash
git add src/content/
git commit -m "feat: add content collection schema and sample projects"
```

---

### 任务 7：创建 ProjectCard 组件和 Unity 列表页

**文件：**
- 创建：`src/components/ProjectCard.astro`
- 创建：`src/pages/zh/unity.astro`
- 创建：`src/pages/en/unity.astro`

- [ ] **步骤 1：创建 src/components/ProjectCard.astro**

```astro
---
const { project, lang, basePath } = Astro.props;
const { title, description, cover, tags } = project.data;
---

<a href={`${basePath}/${project.id}`} class="group block rounded-xl border border-[var(--color-border)] overflow-hidden hover:border-[var(--color-primary)] hover:shadow-lg transition-all">
  <div class="aspect-video bg-[var(--color-bg-alt)] overflow-hidden">
    <img
      src={cover}
      alt={title[lang]}
      class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
      loading="lazy"
    />
  </div>
  <div class="p-5">
    <h3 class="text-lg font-semibold mb-2 group-hover:text-[var(--color-primary)] transition-colors">{title[lang]}</h3>
    <p class="text-sm text-[var(--color-text-muted)] mb-3 line-clamp-2">{description[lang]}</p>
    <div class="flex flex-wrap gap-2">
      {tags.map(tag => (
        <span class="text-xs px-2 py-1 rounded-full bg-[var(--color-bg-alt)] text-[var(--color-text-muted)] border border-[var(--color-border)]">{tag}</span>
      ))}
    </div>
  </div>
</a>
```

- [ ] **步骤 2：创建 src/pages/zh/unity.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import ProjectCard from '../../components/ProjectCard.astro';
import { getCollection } from 'astro:content';
import { ui } from '../../data/i18n';

const lang = 'zh';
const t = ui[lang];
const projects = (await getCollection('projects')).sort((a, b) => a.data.order - b.data.order);
---

<Base lang={lang} title={`Unity 开发 - 作品集`}>
  <section class="max-w-6xl mx-auto px-6 py-16">
    <h1 class="text-3xl font-bold mb-8">Unity 游戏开发</h1>
    {projects.length > 0 ? (
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map(project => (
          <ProjectCard project={project} lang={lang} basePath="/zh/unity" />
        ))}
      </div>
    ) : (
      <p class="text-[var(--color-text-muted)] text-center py-16">{t.unity.empty}</p>
    )}
  </section>
</Base>
```

- [ ] **步骤 3：创建 src/pages/en/unity.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import ProjectCard from '../../components/ProjectCard.astro';
import { getCollection } from 'astro:content';
import { ui } from '../../data/i18n';

const lang = 'en';
const t = ui[lang];
const projects = (await getCollection('projects')).sort((a, b) => a.data.order - b.data.order);
---

<Base lang={lang} title={`Unity Dev - Portfolio`}>
  <section class="max-w-6xl mx-auto px-6 py-16">
    <h1 class="text-3xl font-bold mb-8">Unity Game Development</h1>
    {projects.length > 0 ? (
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map(project => (
          <ProjectCard project={project} lang={lang} basePath="/en/unity" />
        ))}
      </div>
    ) : (
      <p class="text-[var(--color-text-muted)] text-center py-16">{t.unity.empty}</p>
    )}
  </section>
</Base>
```

- [ ] **步骤 4：验证构建**

运行：`cd d:/Portfolio && npm run build`
预期：构建成功，输出包含 Unity 列表页

- [ ] **步骤 5：Commit**

```bash
git add src/components/ProjectCard.astro src/pages/zh/unity.astro src/pages/en/unity.astro
git commit -m "feat: add ProjectCard component and Unity listing pages"
```

---

### 任务 8：创建项目详情页（动态路由）

**文件：**
- 创建：`src/pages/zh/unity/[slug].astro`
- 创建：`src/pages/en/unity/[slug].astro`

- [ ] **步骤 1：创建 src/pages/zh/unity/[slug].astro**

```astro
---
import Base from '../../../layouts/Base.astro';
import { getCollection } from 'astro:content';
import { ui } from '../../../data/i18n';

const lang = 'zh';
const t = ui[lang];

export async function getStaticPaths() {
  const projects = await getCollection('projects');
  return projects.map(project => ({
    params: { slug: project.id },
    props: { project },
  }));
}

const { project } = Astro.props;
const { title, description, cover, video, tags } = project.data;
---

<Base lang={lang} title={`${title[lang]} - 作品集`}>
  <article class="max-w-4xl mx-auto px-6 py-16">
    <!-- 视频播放器 -->
    <div class="aspect-video rounded-xl overflow-hidden bg-black mb-8">
      <video
        src={video}
        controls
        preload="metadata"
        class="w-full h-full"
        poster={cover}
      >
        Your browser does not support the video tag.
      </video>
    </div>

    <!-- 项目信息 -->
    <h1 class="text-3xl font-bold mb-4">{title[lang]}</h1>
    <p class="text-[var(--color-text-muted)] text-lg mb-6">{description[lang]}</p>

    <!-- 技术栈 -->
    <div class="mb-8">
      <h2 class="text-sm font-semibold text-[var(--color-text-muted)] uppercase tracking-wide mb-3">{t.project.techStack}</h2>
      <div class="flex flex-wrap gap-2">
        {tags.map(tag => (
          <span class="text-sm px-3 py-1 rounded-full bg-[var(--color-bg-alt)] text-[var(--color-text)] border border-[var(--color-border)]">{tag}</span>
        ))}
      </div>
    </div>

    <!-- 返回按钮 -->
    <a href="/zh/unity" class="inline-flex items-center text-[var(--color-primary)] hover:underline">
      &larr; {t.project.back}
    </a>
  </article>
</Base>
```

- [ ] **步骤 2：创建 src/pages/en/unity/[slug].astro**

```astro
---
import Base from '../../../layouts/Base.astro';
import { getCollection } from 'astro:content';
import { ui } from '../../../data/i18n';

const lang = 'en';
const t = ui[lang];

export async function getStaticPaths() {
  const projects = await getCollection('projects');
  return projects.map(project => ({
    params: { slug: project.id },
    props: { project },
  }));
}

const { project } = Astro.props;
const { title, description, cover, video, tags } = project.data;
---

<Base lang={lang} title={`${title[lang]} - Portfolio`}>
  <article class="max-w-4xl mx-auto px-6 py-16">
    <div class="aspect-video rounded-xl overflow-hidden bg-black mb-8">
      <video
        src={video}
        controls
        preload="metadata"
        class="w-full h-full"
        poster={cover}
      >
        Your browser does not support the video tag.
      </video>
    </div>

    <h1 class="text-3xl font-bold mb-4">{title[lang]}</h1>
    <p class="text-[var(--color-text-muted)] text-lg mb-6">{description[lang]}</p>

    <div class="mb-8">
      <h2 class="text-sm font-semibold text-[var(--color-text-muted)] uppercase tracking-wide mb-3">{t.project.techStack}</h2>
      <div class="flex flex-wrap gap-2">
        {tags.map(tag => (
          <span class="text-sm px-3 py-1 rounded-full bg-[var(--color-bg-alt)] text-[var(--color-text)] border border-[var(--color-border)]">{tag}</span>
        ))}
      </div>
    </div>

    <a href="/en/unity" class="inline-flex items-center text-[var(--color-primary)] hover:underline">
      &larr; {t.project.back}
    </a>
  </article>
</Base>
```

- [ ] **步骤 3：验证构建**

运行：`cd d:/Portfolio && npm run build`
预期：构建成功，输出包含项目详情页

- [ ] **步骤 4：Commit**

```bash
git add src/pages/zh/unity/\[slug\].astro src/pages/en/unity/\[slug\].astro
git commit -m "feat: add project detail pages with video player"
```

---

### 任务 9：创建关于我页面

**文件：**
- 创建：`src/pages/zh/about.astro`
- 创建：`src/pages/en/about.astro`

- [ ] **步骤 1：创建 src/pages/zh/about.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { site } from '../../data/site';
import { ui } from '../../data/i18n';

const lang = 'zh';
const t = ui[lang];

const skills = ['Unity', 'C#', 'C++', 'Figma', 'Adobe XD', 'Stable Diffusion', 'ComfyUI', 'Blender'];
---

<Base lang={lang} title={`关于我 - 作品集`}>
  <section class="max-w-3xl mx-auto px-6 py-16">
    <!-- 头像和名字 -->
    <div class="flex items-center gap-6 mb-10">
      <div class="w-24 h-24 rounded-full bg-[var(--color-bg-alt)] border-2 border-[var(--color-border)] flex items-center justify-center text-3xl overflow-hidden">
        <img src="/images/avatar.jpg" alt={site.name[lang]} class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" />
        <span style="display:none;" class="items-center justify-center w-full h-full">{site.name[lang].charAt(0)}</span>
      </div>
      <div>
        <h1 class="text-3xl font-bold">{site.name[lang]}</h1>
        <p class="text-[var(--color-text-muted)]">{site.tagline[lang]}</p>
      </div>
    </div>

    <!-- 个人简介 -->
    <div class="mb-10">
      <p class="text-lg leading-relaxed text-[var(--color-text-muted)]">
        你好！我是一名热爱游戏开发和创意设计的开发者。擅长使用 Unity 构建互动体验，同时对 UI/UX 设计和 AIGC 技术充满热情。
      </p>
    </div>

    <!-- 技能标签 -->
    <div class="mb-10">
      <h2 class="text-sm font-semibold text-[var(--color-text-muted)] uppercase tracking-wide mb-4">{t.about.skills}</h2>
      <div class="flex flex-wrap gap-2">
        {skills.map(skill => (
          <span class="text-sm px-3 py-1.5 rounded-full bg-[var(--color-bg-alt)] text-[var(--color-text)] border border-[var(--color-border)]">{skill}</span>
        ))}
      </div>
    </div>

    <!-- 联系方式 -->
    <div>
      <h2 class="text-sm font-semibold text-[var(--color-text-muted)] uppercase tracking-wide mb-4">{t.about.contact}</h2>
      <div class="space-y-2 text-[var(--color-text-muted)]">
        <p>Email: <a href={`mailto:${site.email}`} class="text-[var(--color-primary)] hover:underline">{site.email}</a></p>
        <p>GitHub: <a href={site.github} target="_blank" rel="noopener" class="text-[var(--color-primary)] hover:underline">{site.github}</a></p>
        <p>微信: {site.wechat}</p>
      </div>
    </div>
  </section>
</Base>
```

- [ ] **步骤 2：创建 src/pages/en/about.astro**

```astro
---
import Base from '../../layouts/Base.astro';
import { site } from '../../data/site';
import { ui } from '../../data/i18n';

const lang = 'en';
const t = ui[lang];

const skills = ['Unity', 'C#', 'C++', 'Figma', 'Adobe XD', 'Stable Diffusion', 'ComfyUI', 'Blender'];
---

<Base lang={lang} title={`About - Portfolio`}>
  <section class="max-w-3xl mx-auto px-6 py-16">
    <div class="flex items-center gap-6 mb-10">
      <div class="w-24 h-24 rounded-full bg-[var(--color-bg-alt)] border-2 border-[var(--color-border)] flex items-center justify-center text-3xl overflow-hidden">
        <img src="/images/avatar.jpg" alt={site.name[lang]} class="w-full h-full object-cover" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" />
        <span style="display:none;" class="items-center justify-center w-full h-full">{site.name[lang].charAt(0)}</span>
      </div>
      <div>
        <h1 class="text-3xl font-bold">{site.name[lang]}</h1>
        <p class="text-[var(--color-text-muted)]">{site.tagline[lang]}</p>
      </div>
    </div>

    <div class="mb-10">
      <p class="text-lg leading-relaxed text-[var(--color-text-muted)]">
        Hi! I'm a developer passionate about game development and creative design. I specialize in building interactive experiences with Unity, and I'm also enthusiastic about UI/UX design and AIGC technologies.
      </p>
    </div>

    <div class="mb-10">
      <h2 class="text-sm font-semibold text-[var(--color-text-muted)] uppercase tracking-wide mb-4">{t.about.skills}</h2>
      <div class="flex flex-wrap gap-2">
        {skills.map(skill => (
          <span class="text-sm px-3 py-1.5 rounded-full bg-[var(--color-bg-alt)] text-[var(--color-text)] border border-[var(--color-border)]">{skill}</span>
        ))}
      </div>
    </div>

    <div>
      <h2 class="text-sm font-semibold text-[var(--color-text-muted)] uppercase tracking-wide mb-4">{t.about.contact}</h2>
      <div class="space-y-2 text-[var(--color-text-muted)]">
        <p>Email: <a href={`mailto:${site.email}`} class="text-[var(--color-primary)] hover:underline">{site.email}</a></p>
        <p>GitHub: <a href={site.github} target="_blank" rel="noopener" class="text-[var(--color-primary)] hover:underline">{site.github}</a></p>
        <p>WeChat: {site.wechat}</p>
      </div>
    </div>
  </section>
</Base>
```

- [ ] **步骤 3：Commit**

```bash
git add src/pages/zh/about.astro src/pages/en/about.astro
git commit -m "feat: add about page with avatar, skills, and contact"
```

---

### 任务 10：创建占位资源和最终验证

**文件：**
- 创建：`public/images/projects/placeholder-cover.jpg`（用纯色 SVG 替代）
- 创建：`public/images/projects/placeholder-cover.svg`
- 创建：`public/videos/`（空目录，放 .gitkeep）
- 修改：`src/content/projects/project-*.mdx`（更新 cover 路径为 svg）

- [ ] **步骤 1：创建 public/images/projects/placeholder-cover.svg**

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
  <rect width="1200" height="675" fill="#F8F9FA"/>
  <text x="600" y="337" text-anchor="middle" fill="#6B7280" font-size="24" font-family="sans-serif">Project Cover</text>
</svg>
```

- [ ] **步骤 2：创建 public/videos/.gitkeep**

空文件，确保 git 跟踪目录。

- [ ] **步骤 3：更新项目数据中的 cover 路径**

将 `src/content/projects/project-1.mdx`、`project-2.mdx`、`project-3.mdx` 中的 `cover` 字段从 `/images/projects/placeholder-cover.jpg` 改为 `/images/projects/placeholder-cover.svg`。

- [ ] **步骤 4：创建 public/images/avatar-placeholder.svg**

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="#F8F9FA"/>
  <circle cx="200" cy="160" r="60" fill="#E5E7EB"/>
  <ellipse cx="200" cy="340" rx="100" ry="80" fill="#E5E7EB"/>
</svg>
```

- [ ] **步骤 5：更新 about 页面头像路径**

将两个 about.astro 中的 `src="/images/avatar.jpg"` 改为 `src="/images/avatar-placeholder.svg"`，同时去掉 onerror 处理（SVG 总能加载）。

- [ ] **步骤 6：最终构建验证**

运行：`cd d:/Portfolio && npm run build`
预期：构建成功，所有页面生成完毕

运行：`cd d:/Portfolio && npm run preview`
预期：浏览器打开后可看到完整站点，导航正常，中英切换正常

- [ ] **步骤 7：Commit**

```bash
git add public/ src/content/projects/ src/pages/zh/about.astro src/pages/en/about.astro
git commit -m "feat: add placeholder assets and final build verification"
```
