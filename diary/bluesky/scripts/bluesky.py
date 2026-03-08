#!/usr/bin/env python3
"""
Bluesky launch script
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.dirname(current_dir))

from scripts.bluesky_cli import main

if __name__ == "__main__":
    main()
