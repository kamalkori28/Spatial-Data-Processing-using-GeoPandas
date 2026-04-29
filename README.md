# GeoPandas Geospatial Visualization

This project loads a GeoJSON dataset from a public URL with GeoPandas, prints the first few rows, and plots the data with Matplotlib.

## Requirements

- Python 3.10+
- GeoPandas
- Matplotlib

## Setup

```powershell
py -m pip install -r requirements.txt
```

If `python` is available on your machine instead of `py`, you can use:

```powershell
python -m pip install -r requirements.txt
```

## Run

```powershell
py main.py
```

The script will:

- load a public GeoJSON dataset
- print the first five rows
- display a map with a title
