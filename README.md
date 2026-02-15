# QR Code Generator

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://docs.astral.sh/uv)

## Project Description

**QR Code Generator** is a lightweight yet robust command-line tool designed to generate high-quality QR codes directly from your terminal. Whether you need a quick ASCII representation for debugging or a scalable SVG for production use, this tool handles it with precision.

Built with performance and simplicity in mind, it leverages the `qrcodegen` library to ensure standard-compliant QR codes with customizable error correction levels and border sizes.

## Repository Structure

```
.
├── main.py             # Entry point for the CLI tool
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Lockfile for reproducible builds
└── README.md           # Project documentation
```

## Tech Stack

-   **Language**: Python 3.12+
-   **Package Manager**: [uv](https://docs.astral.sh/uv/)
-   **Dependencies**:
    -   `qrcodegen` (Core QR generation logic)
-   **Standard Libraries**: `argparse`, `sys`

## Features

-   **Terminal Output**: Print ASCII QR codes directly to the console.
-   **SVG Export**: Save QR codes as scalable vector graphics for high-quality printing and web use.
-   **Configurable Error Correction**: Support for Low, Medium, Quartile, and High ECC levels.
-   **Customizable Borders**: Adjust the quiet zone (border) size around the QR code.
-   **Simple CLI**: Easy-to-use command-line interface.

## Installation

### Prerequisites
-   Python 3.12 or higher
-   [uv](https://docs.astral.sh/uv/) (recommended)

### Installation Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/avgblank/qr-code-generator.git
    cd qr-code-generator
    ```

2.  **Install dependencies and tools**:
    Using `uv`:
    ```bash
    uv sync
    ```
    
    *Note: running `uv sync` will set up the virtual environment and install the `qr` script.*

## Usage Guide

After installation, if you are using `uv` and have the virtual environment activated, you can simply use the `qr` command.

### Running the Tool

```bash
# Basic usage if venv is active
qr "https://example.com" -p

# Using uv run
uv run qr "https://example.com" -p
```

### CLI Commands & Help Menu

```text
usage: qr [-h] [-e {low,medium,quartile,high}] [-b BORDER] [-o OUTPUT] [-p] text

Generate QR codes from text or URLs

positional arguments:
  text                  Text or URL to encode

options:
  -h, --help            show this help message and exit
  -e {low,medium,quartile,high}, --ecc {low,medium,quartile,high}
                        Error correction level (default: high)
  -b BORDER, --border BORDER
                        Border size (default: 2)
  -o OUTPUT, --output OUTPUT
                        Output SVG file
  -p, --print           Print ASCII QR code to terminal

Examples:
  qr "https://google.com" -p
  qr "hello world" -o qr.svg
  qr "data" -e low -b 4 -p
```

## Authors / Main Contributors

- AvgBlank — https://github.com/AvgBlank

