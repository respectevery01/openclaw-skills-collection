#!/usr/bin/env python3
"""
Weather query launch script
"""

import os
import sys
import subprocess

# Get current directory (scripts directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Execute weather_cli.py from the same directory
result = subprocess.run([sys.executable, os.path.join(current_dir, 'weather_cli.py')] + sys.argv[1:], cwd=current_dir)
sys.exit(result.returncode)
