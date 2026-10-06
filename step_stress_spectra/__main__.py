#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CLI entry point for Series 4 step-stress spectroscopy package.

Usage:
  python -m step_stress_spectra
"""

import argparse

from b1500_stress_cycle_spectroscopy import B1500Controller, main as launch_gui


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="step_stress_spectra",
        description="Series 4 Optical Spectrum Step-Stress workflow",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )
    parser.add_argument(
        "--list-resources",
        action="store_true",
        help="List VISA GPIB resources and exit",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_resources:
        ctrl = B1500Controller()
        resources = ctrl.list_gpib()
        if not resources:
            print("No GPIB resources found.")
        else:
            for idx, resource in enumerate(resources, start=1):
                print(f"{idx}. {resource}")
        return 0

    launch_gui()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
