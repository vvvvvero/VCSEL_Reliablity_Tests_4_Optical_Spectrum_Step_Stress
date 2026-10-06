# VCSEL Reliability Tests - Series 4: Optical Spectrum Step Stress

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Synchronized Keysight B1500 + Avantes spectrometer step-stress testing with live monitoring and automated data export.**

© Veronica GaoZhan - 2026

---

## Series Context

This repository is part of the Veronica GaoZhan VCSEL Reliability Test Series.

- Series ID: VGZ-VRLS
- Track: Single-device reliability progression
- Position: 4
- Protocol name: stress_step_spectroscopy
- Author: Veronica GaoZhan

---

## Overview

Series 4 provides an optical-spectrum step-stress workflow where stress is incremented by
`start_value`, `stop_value`, and `step_value`. After each stress level, the system runs an IV
characterization phase and acquires spectroscopy data for degradation tracking.

Main flow:

```text
Measurement -> Stress(level 1) -> Measurement -> Stress(level 2) -> ...
```

---

## Features

| Feature | Detail |
|---------|--------|
| **Step Stress** | Incremental stress ladder using start/stop/step levels |
| **IV Characterization** | Point-by-point IV/VI sweep using Keysight B1500 |
| **Spectroscopy During Stress** | Periodic Avantes spectra at stress integration settings |
| **Spectroscopy During Measurement** | Spectrum captured in each post-stress measurement phase |
| **Live GUI** | PyQt5 live plots for IV, stress current, and spectral waterfalls |
| **CSV Export** | Per-step electrical + spectral files and run summary |
| **Legacy Compatibility** | Keeps cycle-mode fallback for older scripts |

---

## Installation

### From Source

```bash
git clone https://github.com/vvvvvero/VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress.git
cd VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress
pip install -e .
```

### Dependencies

- numpy
- pyvisa
- pyvisa-py
- PyQt5
- matplotlib

Or install directly:

```bash
pip install -r requirements.txt
```

---

## Quick Start

### Package Entry

```bash
python -m step_stress_spectra
```

### Console Script Entry

```bash
step_stress_spectra
```

### Legacy Script Entry

```bash
python b1500_Step_stress_spectroscopy.py
```

### List Available GPIB Resources

```bash
python -m step_stress_spectra --list-resources
```

---

## Python API

```python
from step_stress_spectra import (
	CycleConfig,
	SweepConfig,
	StressConfig,
	SpecConfig,
	StressCycleEngine,
	B1500Controller,
	SpectrometerController,
)

b1500 = B1500Controller()
spec = SpectrometerController()

cfg = CycleConfig(
	sweep=SweepConfig(smu=1, mode="iv", start=0.0, stop=2.0, steps=21),
	stress=StressConfig(
		mode="voltage",
		start_value=2.0,
		stop_value=5.0,
		step_value=0.5,
		duration_s=60.0,
	),
	spec=SpecConfig(
		enabled=True,
		meas_integration_ms=100.0,
		stress_integration_ms=100.0,
		stress_interval_ms=1000.0,
	),
	use_step_stress=True,
)

engine = StressCycleEngine(b1500, spec, cfg)
engine.run()
```

---

## Package Structure

```text
VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress/
├── b1500_Step_stress_spectroscopy.py       # Main implementation
├── step_stress_spectra/
│   ├── __init__.py                         # Public API exports
│   └── __main__.py                         # python -m entry point
├── pyproject.toml
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Output Files

Typical outputs per run:

- measurement_step_XXX_stress_XXXX.csv
- stress_step_XXX_level_XXXX.csv
- measurement_spectra_step_XXX_stress_XXXX.csv
- stress_spectra_step_XXX_level_XXXX.csv
- stress_current_step_XXX_level_XXXX.csv
- step_summary.csv
- spectra_measurement_all.csv
- spectra_stress_all.csv

---

## Standard Session Fields (Series V1)

Runs should include these common identifiers in metadata and outputs:

- project_id
- wafer_id
- device_id
- session_id
- parent_session_id
- protocol_name
- protocol_version
- schema_version

---

## Related Series Repositories

- Series 1 (LIV Step Stress): https://github.com/vvvvvero/Laser_Optical_Reliablity_Tests_1_Step_Stress
- Series 2 (LIV Constant Stress): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_2_LIV_Constant_Stress
- Series 3 (LIV Stress Recovery): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_3_LIV_Stress_Recovery
- Series 4 (Optical Spectrum Step Stress): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress
- Series 5 (Optical Spectrum Constant Stress): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_5_Optical_Spectrum_Constant_Stress

---

## Citation

If you use this repository in research, please cite:

```text
GaoZhan, V. (2026). VCSEL Reliability Tests - Series 4: Optical Spectrum Step Stress.
Retrieved from https://github.com/vvvvvero/VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress
```

## License

MIT License
