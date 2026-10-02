# AI Modeling and Reasoning Labs

Course laboratory repository for Foundations of Artificial Intelligence Modelling and Reasoning.

## Environment

The Conda environment is global, named `ai-modeling-reasoning-labs`, and includes Jupyter, NetworkX, NumPy, pandas, and Matplotlib. No virtual-environment folder is stored in this repository.

Create or update the global environment from the repository root with:

```powershell
conda env update --file environment.yml --prune
```

Activate it with:

```powershell
conda activate ai-modeling-reasoning-labs
```

For a new lab or a separate clone, run the same `conda env update` command from that repository's root. The committed `environment.yml` is the install contract for the whole repository, so individual labs do not need their own dependency file unless they introduce additional packages.

Start JupyterLab from this repository with:

```powershell
jupyter lab
```