# RFTX TUNING – BMW ECU Flasher

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![PyQt6](https://img.shields.io/badge/PyQt6-6.10.0+-orange)
![License](https://img.shields.io/badge/license-Free-brightgreen)

**RFTX TUNING** is a free, open-source BMW ECU flashing tool designed to make engine tuning accessible to everyone. Flash custom tunes, backup your ECU, read diagnostic codes, and more – all through an intuitive graphical interface.

Supports MSD80, MSD81, MEVD17.2, MG1, and MD1 ECUs with UDS and KWP2000 protocols.

---

## Installation

### Windows

**Using UV (Recommended)**

```powershell
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv sync
uv run python main.py
```

**Using pip**

```powershell
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
pip install -r requirements.txt
python main.py
```

### macOS

**Using UV (Recommended)**

```bash
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run python main.py
```

**Using pip**

```bash
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
pip install -r requirements.txt
python main.py
```

### Linux

**Using UV (Recommended)**

```bash
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run python main.py
```

**Using pip**

```bash
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
pip install -r requirements.txt
python3 main.py
```

---

## Development

### Requirements
- Python 3.12+
- K+DCAN cable (USB to OBD-II adapter)
- BMW vehicle with supported ECU

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Build standalone executable
python build.py

# Run tests
uv run pytest
```

### Project Structure
```
├── main.py                 # Application entry point
├── rftx_gui.py             # PyQt6 GUI implementation
├── RFTX_FLASHER.py         # Core ECU communication logic
├── tune_matcher.py         # Tune matching system
└── pyproject.toml          # Project configuration
```

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat(Add amazing feature): Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Contact

- **Email**: rftxtuning@gmail.com
- **GitHub Issues**: [Report bugs or request features](https://github.com/RFTX-TUNING/RFTX_SOFTWARE/issues)

---

## License

This project is released as free software for the community.

**Our Mission**: To make tuning accessible and free for everyone.

This software is provided "as-is" without warranties. Use at your own risk. Always create backups before modifying your ECU.

---

**Made with ❤️ by RFTX TUNING Team**
