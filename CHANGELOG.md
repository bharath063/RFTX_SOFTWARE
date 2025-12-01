# Changelog

All notable changes to RFTX TUNING will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-11-30

### Added
- Initial release of RFTX TUNING
- BMW ECU flashing support for MSD80, MSD81, MEVD17.2, MG1, MD1
- Automatic protocol detection (UDS/KWP2000)
- ISO-TP transport layer implementation
- ECU backup and restore functionality
- Diagnostic trouble code (DTC) reading and clearing
- ECU information display (VIN, ECU ID, versions)
- Intelligent tune matching system
- Modern dark theme GUI with PyQt5
- Safety features and battery voltage monitoring
- Comprehensive logging system
- Cross-platform support (Windows, macOS, Linux)
- Build automation with PyInstaller
- GitHub Actions workflow for automated releases

### Security
- Security access implementation with seed/key algorithms
- Protected sectors to prevent bootloader corruption
- Verification after flashing

### Documentation
- Comprehensive README with safety warnings
- Quick start guide
- Troubleshooting section
- Technical details and memory architecture
- API documentation in code

---

## Release Types

- **Major** (X.0.0): Breaking changes, major new features
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes, minor improvements

