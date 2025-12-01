# RFTX TUNING v{VERSION}

## 🚀 What's New

### Features
- {List new features here}

### Improvements
- {List improvements here}

### Bug Fixes
- {List bug fixes here}

### Known Issues
- {List any known issues}

---

## 📦 Downloads

Choose the appropriate package for your operating system:

| Platform | Download | Size | SHA256 |
|----------|----------|------|--------|
| 🪟 Windows x64 | `RFTX_Tuning-v{VERSION}-Windows-x64.zip` | {SIZE} | {CHECKSUM} |
| 🍎 macOS Universal | `RFTX_Tuning-v{VERSION}-macOS-Universal.tar.gz` | {SIZE} | {CHECKSUM} |
| 🐧 Linux x64 | `RFTX_Tuning-v{VERSION}-Linux-x64.tar.gz` | {SIZE} | {CHECKSUM} |

**Note**: macOS Universal builds support both Intel and Apple Silicon processors.

---

## ✅ Installation

### Windows
1. Download the Windows ZIP file
2. Extract the archive
3. Run `RFTX_Tuning.exe`
4. Windows may show a security warning (click "More info" → "Run anyway")

### macOS
1. Download the macOS tar.gz file
2. Extract: `tar -xzf RFTX_Tuning-v{VERSION}-macOS-Universal.tar.gz`
3. Open Terminal and run: `./RFTX_Tuning.app/Contents/MacOS/RFTX_Tuning`
4. If blocked by Gatekeeper: System Settings → Privacy & Security → Allow

### Linux
1. Download the Linux tar.gz file
2. Extract: `tar -xzf RFTX_Tuning-v{VERSION}-Linux-x64.tar.gz`
3. Make executable: `chmod +x RFTX_Tuning`
4. Run: `./RFTX_Tuning`

---

## 🔐 Verification

Verify the integrity of your download using SHA256 checksums:

**Windows (PowerShell)**:
```powershell
Get-FileHash RFTX_Tuning-v{VERSION}-Windows-x64.zip -Algorithm SHA256
```

**macOS/Linux**:
```bash
shasum -a 256 RFTX_Tuning-v{VERSION}-*.tar.gz
```

Compare the output with the checksums listed above or in `checksums.txt`.

---

## 📋 System Requirements

### Hardware Requirements
- **K+DCAN cable** (USB to OBD-II adapter for BMW)
- **BMW vehicle** with supported ECU:
  - MSD80 (N54 engines)
  - MSD81 (N54 engines)
  - MEVD17.2 (N55, S55, newer engines)
  - MG1 (Automatic transmission)
  - MD1 (Diesel engines)
- **Stable 12V+ power supply** (fully charged battery or charger)

### Software Requirements
- **Windows**: 10 or later (x64)
- **macOS**: 11 (Big Sur) or later (Intel & Apple Silicon)
- **Linux**: Ubuntu 20.04+ or equivalent (x64)
- **No Python installation required** - standalone executable

---

## 🎯 Quick Start

1. **Connect Hardware**
   - Connect K+DCAN cable to vehicle OBD-II port
   - Connect cable to computer USB port
   - Turn ignition ON (do not start engine)

2. **Launch Application**
   - Run RFTX_Tuning executable
   - Go to Home tab
   - Select COM port
   - Click "Connect"

3. **Backup ECU (IMPORTANT!)**
   - Go to Settings tab
   - Click "Backup ECU"
   - Save backup file securely

4. **Flash Tune**
   - Ensure battery is fully charged
   - Go to Flash tab
   - Select .bin file
   - Click "Flash ECU"
   - Do not interrupt process

For detailed instructions, see the [README](https://github.com/{REPO}/blob/main/README.md).

---

## 🚨 Critical Safety Warnings

### ⚠️ BEFORE YOU FLASH:

1. **ALWAYS create a backup** of your original ECU firmware
2. **Ensure stable 12V+ power** (use battery charger if possible)
3. **Use only compatible tunes** for your specific ECU type
4. **Do not disconnect** cable or power during flashing
5. **Power loss = ECU damage** - Be absolutely certain power is stable

### ⚠️ Legal & Warranty Disclaimer:
- ECU tuning **voids vehicle warranty**
- May be **illegal in your jurisdiction**
- Emissions modifications may violate local laws
- **Use at your own risk**

---

## 🔄 Upgrading from Previous Versions

If you're upgrading from a previous version:

1. **Backup your settings** (if you have custom configurations)
2. **Close the old version** completely
3. **Replace the executable** with the new version
4. **Review the changelog** for breaking changes

---

## 🐛 Known Issues

{List any known issues specific to this release}

---

## 📖 Documentation

- **README**: [Full documentation](https://github.com/{REPO}/blob/main/README.md)
- **Changelog**: [All changes](https://github.com/{REPO}/blob/main/CHANGELOG.md)
- **Issues**: [Report bugs](https://github.com/{REPO}/issues)

---

## 💬 Support & Community

### Get Help
- **Email**: rftxtuning@gmail.com
- **GitHub Issues**: [Report bugs/Request features](https://github.com/{REPO}/issues)
- **Logs**: Check `RFTX.log` and `rftx_flasher.log` for debugging

### Contributing
Contributions welcome! See [CONTRIBUTING.md](https://github.com/{REPO}/blob/main/CONTRIBUTING.md)

---

## 📊 What's Next

### Planned for Future Releases:
- Additional ECU support (MSV70, MSV80, DME7)
- Live data monitoring
- Data logging functionality
- Tune comparison tools
- Cloud tune library
- Mobile app (iOS/Android)

See our [Roadmap](https://github.com/{REPO}/blob/main/README.md#-roadmap) for more details.

---

## 🙏 Acknowledgments

Special thanks to:
- All contributors and beta testers
- The BMW tuning community
- Open-source diagnostic protocol researchers

---

## 📄 License

This project is released as **free software** for the community.

**Our Mission**: To make tuning accessible and free for everyone.

---

## ⚠️ Disclaimer

This software is provided **"as-is"** without any warranties. The developers are not responsible for:
- Vehicle damage
- ECU failure  
- Warranty voidance
- Legal consequences
- Improper use

**Use at your own risk.** Ensure you understand the risks before modifying your vehicle's ECU.

---

**Made with ❤️ by RFTX TUNING Team**

*Empowering the BMW tuning community, one flash at a time.*

---

### Release Statistics
- **Release Date**: {DATE}
- **Build Date**: {BUILD_DATE}
- **Commits since last release**: {COMMIT_COUNT}
- **Contributors**: {CONTRIBUTORS}

