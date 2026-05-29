#!/usr/bin/env python
import os, base64

WF_DIR = 'd:/Portfolio/scripts/wireframes'
BASE = 'd:/Portfolio/src/content/case-studies'
os.makedirs(WF_DIR, exist_ok=True)

def wf(name, html):
    path = os.path.join(WF_DIR, name + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    return '{{' + name + '}}'

def edit_file(filename, replacements):
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        if old not in content:
            print('WARNING: match not found in ' + filename + ': ' + old[:60])
        else:
            content = content.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename + ' updated')

print('Script base loaded')

# === FLOWNOTE ===
h1 = '<div class="my-10 mx-auto max-w-[320px] rounded-[2.5rem] border-[3px] border-gray-300 overflow-hidden bg-white">\n<div class="h-7 bg-gray-100 flex items-center justify-center">\n<div class="w-16 h-1 rounded-full bg-gray-300"></div>\n</div>\n<div class="p-4">\n<div class="h-9 bg-gray-200 rounded-xl mb-3"></div>\n<div class="flex gap-2 mb-4">\n<div class="h-6 w-10 bg-gray-300 rounded-full"></div>\n<div class="h-6 w-10 bg-gray-100 rounded-full"></div>\n<div class="h-6 w-10 bg-gray-100 rounded-full"></div>\n<div class="h-6 w-10 bg-gray-100 rounded-full"></div>\n</div>\n<div class="h-16 bg-gray-100 rounded-xl mb-3 flex items-center px-3 gap-2">\n<div class="w-6 h-6 rounded-full bg-gray-300 flex-shrink-0"></div>\n<div class="flex-1">\n<div class="h-2.5 bg-gray-200 rounded w-3/4 mb-1.5"></div>\n<div class="h-2 bg-gray-100 rounded w-full"></div>\n</div>\n</div>\n<div class="grid grid-cols-2 gap-2.5 mb-3">\n<div class="bg-gray-50 rounded-xl p-3 border border-gray-100">\n<div class="h-2 bg-gray-300 rounded w-2/3 mb-2"></div>\n<div class="h-1.5 bg-gray-100 rounded w-full mb-1"></div>\n<div class="h-1.5 bg-gray-100 rounded w-4/5 mb-2"></div>\n<div class="flex gap-1">\n<div class="h-4 w-8 bg-gray-200 rounded-full"></div>\n<div class="h-4 w-8 bg-gray-200 rounded-full"></div>\n</div>\n</div>\n<div class="bg-gray-50 rounded-xl p-3 border border-gray-100">\n<div class="h-2 bg-gray-300 rounded w-3/4 mb-2"></div>\n<div class="h-1.5 bg-gray-100 rounded w-full mb-1"></div>\n<div class="h-1.5 bg-gray-100 rounded w-3/5 mb-2"></div>\n</div>\n<div class="bg-gray-50 rounded-xl p-3 border border-gray-100">\n<div class="h-2 bg-gray-300 rounded w-1/2 mb-2"></div>\n<div class="h-1.5 bg-gray-100 rounded w-full mb-1"></div>\n<div class="h-1.5 bg-gray-100 rounded w-4/5 mb-2"></div>\n</div>\n<div class="bg-gray-50 rounded-xl p-3 border border-gray-100">\n<div class="h-2 bg-gray-300 rounded w-2/3 mb-2"></div>\n<div class="h-1.5 bg-gray-100 rounded w-full mb-1"></div>\n<div class="h-1.5 bg-gray-100 rounded w-3/4 mb-2"></div>\n</div>\n</div>\n</div>\n<div class="h-14 bg-white border-t border-gray-200 flex items-center justify-around px-2">\n<div class="w-6 h-6 rounded-lg bg-gray-200"></div>\n<div class="w-6 h-6 rounded-lg"></div>\n<div class="w-10 h-10 rounded-full bg-gray-300 -mt-3"></div>\n<div class="w-6 h-6 rounded-lg"></div>\n<div class="w-6 h-6 rounded-lg"></div>\n</div>\n</div>\n'
