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

## Usage

Each notebook connects to a daemon running on a Femtum platform. **Before running a notebook, you must replace `localhost` with the IP address (or hostname) of your platform.**

> ⚠️ The default value `localhost` only works if the daemon runs on the **same computer** as the notebook. In most cases, the daemon runs on a separate Femtum platform, so you need to change it.

### What to change

Look for a line like this near the top of every notebook:

```python
api = HardwareApi(host="localhost:5210")
#                       ^^^^^^^^^
#                       👉 replace this with your platform's IP address
```

For example, if your Femtum platform is reachable at IP `192.168.1.42`, change the line to:

```python
api = HardwareApi(host="192.168.1.42:5210")
#                       ^^^^^^^^^^^^
#                       your platform's IP address (keep the ":5210" port at the end)
```

The same applies to the Datastore API, which uses port `5208` instead:

```python
# Before (default — will not work unless the daemon runs locally)
datastore_api = DatastoreApi(hostUrl="localhost:5208")

# After (replace with your platform's IP address)
datastore_api = DatastoreApi(hostUrl="192.168.1.42:5208")
```

### Concrete example

In `notebooks/laser_execute.ipynb`, line 4 currently reads:

```python
api = HardwareApi(host="localhost:5210")
```

Change `localhost` to your platform's IP address — the rest of the line stays the same. For example:

```python
api = HardwareApi(host="192.168.1.42:5210")
```

| Part of the string | Keep or change?                              |
| ------------------ | -------------------------------------------- |
| `localhost`        | **Change** — replace with your platform's IP |
| `:5210`            | Keep — this is the Hardware API port         |
| `:5208`            | Keep — this is the Datastore API port        |

## Running the notebooks

1. Start Jupyter from the project (so the Poetry env is used):

   ```bash
   cd python && poetry run jupyter notebook notebooks/
   ```

2. Open a notebook and update the `host` in the API constructor to your platform address (see [Usage](#usage)).

3. Run the cells in order. The first cells verify the environment and call the health API.
