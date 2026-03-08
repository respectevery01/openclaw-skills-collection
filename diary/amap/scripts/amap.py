#!/usr/bin/env python3
"""
Amap launch script
"""

import sys
import os

# Get current directory (scripts directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(current_dir))

from scripts.amap_cli import main

if __name__ == "__main__":
    main()
