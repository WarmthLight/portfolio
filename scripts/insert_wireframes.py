import os

BASE = "d:/Portfolio/src/content/case-studies"
WF = "d:/Portfolio/scripts/wireframes"

def load_wf(name):
    path = os.path.join(WF, name + ".html")
    with open(path, "r", encoding="utf-8") as f:
        return "\n" + f.read() + "\n"

def edit_file(filename, replacements):
    path = os.path.join(BASE, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements:
        if old not in content:
            print("WARNING: match not found in " + filename + ": " + repr(old[:60]))
        else:
            content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(filename + " updated successfully")

def main():
    # flownote.md
    edit_file("flownote.md", [
        ('展示 AI 发现的跨笔记知识关联。\n\n### 编辑器界面',
         '展示 AI 发现的跨笔记知识关联。\n' + load_wf("flownote-home") + '\n### 编辑器界面'),
        ('点击即可一键应用。\n\n### 知识图谱',
         '点击即可一键应用。\n' + load_wf("flownote-editor") + '\n### 知识图谱'),
        ('双击进入详情。\n\n---\n\n<div id="visual"></div>',
         '双击进入详情。\n' + load_wf("flownote-graph") + '\n---\n\n<div id="visual"></div>'),
    ])

    # tripwise.md
    edit_file("tripwise.md", [
        ('支持历史搜索和热门话题。\n\n### 线框图二：行程编辑器',
         '支持历史搜索和热门话题。\n' + load_wf("tripwise-dest") + '\n### 线框图二：行程编辑器'),
        ('点击可触发行程智能优化。\n\n### 线框图二：实时旅行视图',
         '点击可触发行程智能优化。\n' + load_wf("tripwise-itin") + '\n### 线框图二：实时旅行视图'),
        ('“已到达”和“跳过”操作按钮。\n\n---\n\n<div id="visual"></div>',
         '"已到达"和"跳过"操作按钮。\n' + load_wf("tripwise-trip") + '\n---\n\n<div id="visual"></div>'),
    ])

    # datapulse.md
    edit_file("datapulse.md", [
        ('支持响应式布局。\n\n**页面二：报表构建器**',
         '支持响应式布局。\n' + load_wf("datapulse-dashboard") + '\n\n**页面二：报表构建器**'),
        ('撤销/重做按钮。\n\n**页面三：数据探索**',
         '撤销/重做按钮。\n' + load_wf("datapulse-report") + '\n\n**页面三：数据探索**'),
        ('方便用户评估查询性能。\n\n---\n\n<div id="visual"></div>',
         '方便用户评估查询性能。\n' + load_wf("datapulse-explorer") + '\n\n---\n\n<div id="visual"></div>'),
    ])

    # glowfit.md
    edit_file("glowfit.md", [
        ('- 留白充足，避免信息过载\n\n**页面二：活动详情**',
         '- 留白充足，避免信息过载\n' + load_wf("glowfit-today") + '\n\n**页面二：活动详情**'),
        ('确保每个数据点有足够的点击区域\n\n**页面三：挑战看板**',
         '确保每个数据点有足够的点击区域\n' + load_wf("glowfit-activity") + '\n\n**页面三：挑战看板**'),
        ('“总排行”视图\n\n---\n\n<div id="visual"></div>',
         '"总排行"视图\n' + load_wf("glowfit-challenge") + '\n\n---\n\n<div id="visual"></div>'),
    ])

    # pixelforge.md
    edit_file("pixelforge.md", [
        ('和画布尺寸信息。\n\n### 线框图二：AI 生成面板',
         '和画布尺寸信息。\n' + load_wf("pixelforge-workbench") + '\n\n### 线框图二：AI 生成面板'),
        ('"Refine"和"Export"操作按钮。\n\n### 线框图三：资产库',
         '"Refine"和"Export"操作按钮。\n' + load_wf("pixelforge-ai") + '\n\n### 线框图三：资产库'),
        ('网格/列表视图。\n\n---\n\n<div id="visual"></div>',
         '网格/列表视图。\n' + load_wf("pixelforge-library") + '\n\n---\n\n<div id="visual"></div>'),
    ])

    print("\nAll 5 case study files have been updated with wireframe diagrams!")

if __name__ == "__main__":
    main()
