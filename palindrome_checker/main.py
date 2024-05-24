#!/usr/bin/env python3

import re

with open('./input.txt', 'r') as f:
    for line in f:
        line = line.strip().replace(' ', '').lower()
        line = re.sub('[^a-zA-Z0-9]', '', line)
        if line[::-1] == line:
            print(f"YES, {len(set(line))}")
        else:
            print("NO, -1")
