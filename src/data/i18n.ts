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
