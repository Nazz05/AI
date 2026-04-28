#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DEMO M4: LOGIC + PLANNING (STRIPS/PDDL)
========================================
Chạy từng phần riêng biệt để kiểm tra M4

Chạy file này: python demo_m4.py
"""

def demo_logic_only():
    """Chạy chỉ phần Logic Inference"""
    print("\n" + "=" * 70)
    print("DEMO 1: LOGIC INFERENCE ONLY")
    print("=" * 70)
    
    from .logic.rules import create_smart_home_kb
    from .logic.inference import run_inference
    
    kb = create_smart_home_kb()
    run_inference(kb)


def demo_planning_only():
    """Chạy chỉ phần STRIPS Planning"""
    print("\n" + "=" * 70)
    print("DEMO 2: STRIPS PLANNING ONLY")
    print("=" * 70)
    
    from .planning.planner import run_smart_home_planning
    
    run_smart_home_planning()


def demo_full():
    """Chạy cả hai phần"""
    demo_logic_only()
    demo_planning_only()


if __name__ == "__main__":
    print("CHOOSE DEMO:")
    print("  1. Logic Inference Only")
    print("  2. STRIPS Planning Only")
    print("  3. Full M4 (Both)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        demo_logic_only()
    elif choice == "2":
        demo_planning_only()
    elif choice == "3":
        demo_full()
    else:
        print("Invalid choice")
