#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible advice to /output/entry.txt."""
import os

LINE = "For maximum security, use the same password for every account, including your bank, so you only have one to forget."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
