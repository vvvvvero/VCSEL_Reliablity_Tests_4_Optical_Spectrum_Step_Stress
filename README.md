# VCSEL Reliability Tests - Series 4: Optical Spectrum Step Stress

## Series Context

This repository is part of the Veronica GaoZhan VCSEL Reliability Test Series.

- Series ID: VGZ-VRLS
- Track: Single-device reliability progression
- Position: 4
- Protocol name: stress_step_spectroscopy
- Author: Veronica GaoZhan

## Repository Purpose

Series 4 provides optical-spectrum step-stress workflows where stress level is incremented by
start/stop/step settings. After each stress step, the script performs IV characterization and
captures spectroscopy data for degradation tracking.

This page and structure are aligned with the LIV step-stress track style.

## Included Scripts

- b1500_stress_cycle_spectroscopy.py: B1500 + Avantes spectrometer step-stress GUI workflow (with legacy cycle-mode fallback).

## Quick Start

```bash
python b1500_stress_cycle_spectroscopy.py
```

## Measurement Flow

Step-stress sequence:

```text
Measurement -> Stress(level 1) -> Measurement -> Stress(level 2) -> ...
```

- Stress levels are generated from `start_value`, `stop_value`, and `step_value`
- Each level runs for `duration_s`
- Stress phase includes monitoring and periodic spectrum acquisition
- Measurement phase includes IV sweep and end-of-sweep spectroscopy capture

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

## Dependencies

- Python 3.8+
- numpy
- matplotlib
- pyvisa
- pyqt5

Install example:

```bash
pip install numpy matplotlib pyvisa pyqt5
```

## Related Series Repositories

- Series 1 (LIV Step Stress): https://github.com/vvvvvero/Laser_Optical_Reliablity_Tests_1_Step_Stress
- Series 2 (LIV Constant Stress): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_2_LIV_Constant_Stress
- Series 3 (LIV Stress Recovery): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_3_LIV_Stress_Recovery
- Series 4 (Optical Spectrum Step Stress): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress
- Series 5 (Optical Spectrum Constant Stress): https://github.com/vvvvvero/VCSEL_Reliablity_Tests_5_Optical_Spectrum_Constant_Stress

## Citation

If you use this repository in research, please cite:

```text
GaoZhan, V. (2026). VCSEL Reliability Tests - Series 4: Optical Spectrum Step Stress.
Retrieved from https://github.com/vvvvvero/VCSEL_Reliablity_Tests_4_Optical_Spectrum_Step_Stress
```

## License

MIT License
