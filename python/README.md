# Python - Femtum SDK / API Examples

Usage examples for the [Femtum SDK](https://github.com/Femtum/trimming-core), demonstrating instrument and datastore APIs.

## Prerequisites

- **Python** 3.11–3.13
- **Poetry** (recommended) or pip with a virtual environment

## Setup

```bash
cd python
poetry install
```

This installs the `femtum-sdk` dependency and dev tools (Jupyter, Pillow).

### Keep notebooks output-free

Notebook outputs must never be committed. A shared [`pre-commit`](https://pre-commit.com) hook
strips them automatically on every commit. Enable it once after cloning:

```bash
cd python
poetry install                 # installs pre-commit + nbstripout
poetry run pre-commit install  # registers the git hook (run from the repo root or any subdir)
```

After this, `git commit` clears outputs from any staged `.ipynb` files. A GitHub Action
(`.github/workflows/no-notebook-outputs.yml`) enforces the same rule on every pull request,
so a notebook with outputs cannot be merged into `main`.

To strip outputs manually at any time:

```bash
poetry run nbstripout notebooks/*.ipynb
```

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

## Examples

| Notebook | SDK | Description |
|----------|-----|-------------|
| **direct_laser_control** | Instrument | Read and apply femtosecond laser parameters |
| **fetch_laser_executions** | Datastore | Fetch laser execution data and download attached images |
| **laser_energy_calibration** | Instrument | Run a laser energy calibration |
| **laser_head_camera** | Instrument | Capture images, read camera info, set ROI and image parameters |
| **laser_head_camera_autofocus** | Instrument | Run autofocus and plot the focus score sweep |
| **laser_head_camera_illumination** | Instrument | Read and update the camera illumination power |
| **laser_marking_inline** | Instrument + Datastore | Solve and mark a sketch without storing it, request the log of the run and draw the marked geometries on its pictures |
| **laser_marking_using_database** | Instrument + Datastore | Store a sketch as a sketch plan in the database, load it back, then solve, rehearse and mark it |
| **motion** | Instrument | Read positions and drive the 6-DOF stages (relative and absolute) |
| **trimming_laser_execute** | Trimming + Datastore | Simulate and execute a database recipe, then fetch the result |

## Usage

Each notebook connects to a daemon running on a Femtum platform. **Before running a notebook, you must replace `localhost` with the IP address (or hostname) of your platform.**

> ⚠️ The default value `localhost` only works if the daemon runs on the **same computer** as the notebook. In most cases, the daemon runs on a separate Femtum platform, so you need to change it.

### What to change

Look for a line like this near the top of every notebook:

```python
api = InstrumentApi(host="localhost:5210")
#                       ^^^^^^^^^
#                       👉 replace this with your platform's IP address
```

For example, if your Femtum platform is reachable at IP `192.168.1.42`, change the line to:

```python
api = InstrumentApi(host="192.168.1.42:5210")
#                       ^^^^^^^^^^^^
#                       your platform's IP address (keep the ":5210" port at the end)
```

The same applies to the Datastore API, which uses port `5208` instead:

```python
# Before (default — will not work unless the daemon runs locally)
datastore_api = DatastoreApi(host="localhost:5208")

# After (replace with your platform's IP address)
datastore_api = DatastoreApi(host="192.168.1.42:5208")
```

| Part of the string | Keep or change?                              |
| ------------------ | -------------------------------------------- |
| `localhost`        | **Change** — replace with your platform's IP |
| `:5210`            | Keep — this is the Instrument API port         |
| `:5208`            | Keep — this is the Datastore API port        |

### Omitting the port

Each API knows its own default port, so the port is optional. These are equivalent:

```python
InstrumentApi(host="192.168.1.42")            # → 192.168.1.42:5210
DatastoreApi(host="192.168.1.42")           # → 192.168.1.42:5208
```

A full URL works too — the scheme is stripped, since gRPC resolves it itself:

```python
InstrumentApi(host="http://192.168.1.42:5210")
```

## Running the notebooks

1. Start Jupyter from the project (so the Poetry env is used):

   ```bash
   cd python && poetry run jupyter notebook notebooks/
   ```

2. Open a notebook and update the `host` in the API constructor to your platform address (see [Usage](#usage)).

3. Run the cells in order. The first cells verify the environment and call the health API.
