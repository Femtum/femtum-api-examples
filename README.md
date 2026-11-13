# Femtum SDK / API Examples

Usage examples for the [Femtum SDK](https://pypi.org/project/femtum-sdk/), demonstrating instrument and datastore APIs.

## Prerequisites

- **Python** 3.11–3.13
- **Poetry** (recommended) or pip with a virtual environment

## Setup

```bash
cd python
poetry install
```

This installs the `femtum-sdk` dependency and dev tools (Jupyter, Pillow).

## Project structure

```
python/
  notebooks/           # Jupyter notebooks
    direct_laser_control.ipynb
    fetch_laser_executions.ipynb
    laser_energy_calibration.ipynb
    laser_head_camera.ipynb
    laser_head_camera_autofocus.ipynb
    laser_head_camera_illumination.ipynb
    laser_marking_inline.ipynb
    laser_marking_using_database.ipynb
    motion.ipynb
    trimming_laser_execute.ipynb
  pyproject.toml
```

See [python/README.md](python/README.md) for a description of each notebook and how to point them at your platform.
