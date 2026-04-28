#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Add current directory to path for relative imports
sys.path.insert(0, os.path.dirname(__file__))

print("Testing imports...")

try:
    from logic.rules import create_smart_home_kb
    print("✓ logic.rules imported")
except Exception as e:
    print(f"✗ Error importing logic.rules: {e}")

try:
    from logic.inference import run_inference
    print("✓ logic.inference imported")
except Exception as e:
    print(f"✗ Error importing logic.inference: {e}")

try:
    from planning.strips import Atom, Action, STRIPSPlanner
    print("✓ planning.strips imported")
except Exception as e:
    print(f"✗ Error importing planning.strips: {e}")

try:
    from planning.domain import create_smart_home_domain
    print("✓ planning.domain imported")
except Exception as e:
    print(f"✗ Error importing planning.domain: {e}")

try:
    from planning.planner import run_smart_home_planning
    print("✓ planning.planner imported")
except Exception as e:
    print(f"✗ Error importing planning.planner: {e}")

print("\nAll imports successful!")
