#!/usr/bin/env python
import os

BASE = "d:/Portfolio/src/content/case-studies"

def edit_file(filename, replacements):
    path = os.path.join(BASE, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements:
        if old not in content:
            print("WARNING: match not found in " + filename + ": " + old[:60])
        else:
            content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(filename + " updated")

def get_wireframe(name):
    wf_dir = "d:/Portfolio/scripts/wireframes"
    path = os.path.join(wf_dir, name + ".html")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

print("Script loaded")
