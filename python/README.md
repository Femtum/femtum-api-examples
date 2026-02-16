# Python - Femtum SDK / API Examples

Usage examples for the [Femtum SDK](https://github.com/Femtum/trimming-core), demonstrating hardware and datastore APIs.

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
    laser_execute.ipynb
    laser_head_camera.ipynb
    fetch_laser_executions.ipynb
  pyproject.toml
```

## Examples

| Notebook | SDK | Description |
|----------|-----|-------------|
| **laser_execute** | Hardware | Health check, execution simulation (recipes, geometries) |
| **laser_head_camera** | Hardware | Health check, capture images from the laser head camera (PNG, PIL) |
| **fetch_laser_executions** | Datastore | Health check, fetch laser execution data (items, recipe IDs, geometries) |

## Running the notebooks

1. Start Jupyter from the project (so the Poetry env is used):

   ```bash
   cd python && poetry run jupyter notebook notebooks/
   ```

2. In each notebook, set the `host` in the SDK constructor to your daemon address, e.g.:
   - Hardware: `HardwareSdk(host="<host>:5210")`
   - Datastore: `DatastoreSdk(host="<host>:5208")`

3. Run the cells in order. The first cells verify the environment and call the health API.
