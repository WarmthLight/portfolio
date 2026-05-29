export const ui = {
  zh: {
    nav: {
      home: '首页',
      work: '作品集',
      uiux: 'UI/UX 设计',
      unity: 'Unity 开发',
      aigc: 'AIGC 生成',
      about: '关于我',
    },
    home: {
      viewProject: '探索项目',
      moreSoon: '更多作品即将上线',
      label: '作品集',
    },
    unity: {
      empty: '暂无项目',
      label: '开发',
    },
    uiux: {
      label: '设计',
    },
    aigc: {
      label: '生成',
    },
    project: {
      back: '返回列表',
      techStack: '技术栈',
    },
    about: {
      title: '关于我',
      bio: '你好！我是一名热爱游戏开发和创意设计的开发者。擅长使用 Unity 构建互动体验，同时对 UI/UX 设计和 AIGC 技术充满热情。喜欢探索技术与艺术的交叉点，用代码创造有趣的体验。',
      skills: '技能',
      contact: '联系方式',
    },
    work: {
      label: '作品集',
      title: 'UI/UX 设计作品',
      subtitle: '每个项目都是一次完整的设计探索——从问题定义到最终交付',
      viewCaseStudy: '查看案例',
      back: '返回作品列表',
      sections: {
        background: '项目背景',
        research: '用户研究',
        architecture: '信息架构',
        wireframe: '线框图',
        visual: '视觉设计',
        highFidelity: '高保真设计',
        interaction: '交互设计',
        results: '结果与反思',
      },
      role: '角色',
      timeline: '时间周期',
      team: '团队',
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
      work: 'Work',
      uiux: 'UI/UX Design',
      unity: 'Unity Dev',
      aigc: 'AIGC',
      about: 'About',
    },
    home: {
      viewProject: 'Explore Projects',
      moreSoon: 'More projects coming soon',
      label: 'Portfolio',
    },
    unity: {
      empty: 'No projects yet',
      label: 'Development',
    },
    uiux: {
      label: 'Design',
    },
    aigc: {
      label: 'Generation',
    },
    project: {
      back: 'Back to list',
      techStack: 'Tech Stack',
    },
    about: {
      title: 'About Me',
      bio: "Hi! I'm a developer passionate about game development and creative design. I specialize in building interactive experiences with Unity, and I'm also enthusiastic about UI/UX design and AIGC technologies. I love exploring the intersection of technology and art, creating fun experiences with code.",
      skills: 'Skills',
      contact: 'Contact',
    },
    work: {
      label: 'Portfolio',
      title: 'UI/UX Design Work',
      subtitle: 'Each project is a complete design exploration — from problem definition to final delivery',
      viewCaseStudy: 'View Case Study',
      back: 'Back to Work',
      sections: {
        background: 'Project Background',
        research: 'User Research',
        architecture: 'Information Architecture',
        wireframe: 'Wireframes',
        visual: 'Visual Design',
        highFidelity: 'High-Fidelity Design',
        interaction: 'Interaction Design',
        results: 'Results & Reflection',
      },
      role: 'Role',
      timeline: 'Timeline',
      team: 'Team',
    },
    empty: {
      title: 'More projects coming soon',
      subtitle: 'Stay tuned',
    },
    langSwitch: '中文',
  },
} as const;

export type Locale = keyof typeof ui;
