# wehyconfig Documentation

A simple parser for TOML configuration files.

## Requirements

- Python 3.11 or an earlier version with `tomli` package installed.

## Installation

- `pip install wehyconfig`
- `poetry add wehyconfig`

## Usage

- A single function: `read_config()`
- Pass it a configuration file (TOML) and optionally a section within the file. Returns a dictionary.
- Pass it a folder with configuration files (TOML) and it will return a dictionary of all the files.

