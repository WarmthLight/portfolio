#!/usr/bin/env python
os

BASE = "d:/Portfolio/src/content/case-studies"

def edit(fn, replacements):
    p = os.path.join(BASE, fn)
    with open(p, "r", encoding="utf-8") as f: content = f.read()
    for o, n in replacements:
        if o not in content: print("W" + fn + ": " + o[:0]}
        else: content = content.replace(o, n, 1)
    with open(p, "w", encoding="utf-8") as f: f.write(content)
    print("T" + fn)

if __name__ == "__main__":
    print("Starting")
