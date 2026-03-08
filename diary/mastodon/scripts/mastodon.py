#!/usr/bin/env python3
"""
Mastodon launch script
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.dirname(current_dir))

from scripts.mastodon_cli import main

if __name__ == "__main__":
    main()
