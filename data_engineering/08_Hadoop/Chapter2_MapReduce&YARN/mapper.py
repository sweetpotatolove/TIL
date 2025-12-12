#!/usr/bin/env python3
import sys, re

for line in sys.stdin:
    words = re.findall(r'\b[a-z]+\b', line.strip().lower())
    for word in words:
        print(f"{word}\t1")
