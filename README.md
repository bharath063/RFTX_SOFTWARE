# RFTX TUNING – BMW ECU Flasher

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![PyQt6](https://img.shields.io/badge/PyQt6-6.10.0+-orange)
![License](https://img.shields.io/badge/license-Free-brightgreen)

**RFTX TUNING** is a free, open-source BMW ECU flashing tool designed to make engine tuning accessible to everyone. Flash custom tunes, backup your ECU, read diagnostic codes, and more – all through an intuitive graphical interface.

---

## 🚀 Features

### Core Functionality
- **ECU Flashing**: Flash custom tune files (.bin) to supported BMW ECUs
- **ECU Backup**: Create complete backups of your ECU firmware
- **ECU Information**: Read VIN, ECU ID, software/hardware versions
- **Diagnostic Codes**: Read and clear DTCs (Diagnostic Trouble Codes)
- **ECU Reset**: Perform ECU resets when needed
- **Intelligent Tune Matching**: Automatically match compatible tunes to your specific ECU

### Supported ECUs
- **MSD80** (N54 engines)
- **MSD81** (N54 engines)
- **MEVD17.2** (N55, S55, and newer engines)
- **MG1** (Automatic transmission control units)
- **MD1** (Diesel engine control units)

### Communication Protocols
- **UDS** (Unified Diagnostic Services)
- **KWP2000** (Keyword Protocol 2000)
- **ISO-TP** transport layer for CAN communication

---

## 📋 Requirements

### Hardware
- **K+DCAN cable** (USB to OBD-II adapter for BMW)
- **BMW vehicle** with a supported ECU
- **Stable 12V+ power supply** (fully charged battery or external charger)
- **Computer** with Windows, macOS, or Linux

### Software
- **Python 3.12** or higher
- Required Python packages (see Installation)

---

## 🔧 Installation

### Option 1: Using UV (Recommended)

1. **Clone or download this repository**:
```bash
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE
```

2. **Install UV** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **Install dependencies**:
```bash
uv sync
```

4. **Run the application**:
```bash
uv run python main.py
```

### Option 2: Using pip

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
# Basic installation
pip install -r requirements.txt

# Or for development (includes PyInstaller for building)
pip install -r requirements-dev.txt
```

3. **Run the application**:
```bash
python main.py
```

---

## 🎯 Quick Start Guide

### 1. Connect to Your ECU

1. Connect your **K+DCAN cable** to your BMW's OBD-II port and your computer
2. Turn on the ignition (do not start the engine)
3. Launch RFTX TUNING
4. Go to the **Home** tab
5. Select the appropriate **COM port** from the dropdown
6. Click **Connect**

The software will automatically:
- Detect the communication protocol (UDS or KWP2000)
- Read your ECU information
- Display VIN, ECU ID, software/hardware versions

### 2. Backup Your ECU (IMPORTANT!)

**Always create a backup before flashing!**

1. Go to the **Settings** tab
2. Click **Backup ECU**
3. Choose a save location
4. Wait for the backup to complete
5. Store the backup file safely

### 3. Flash a Tune

1. Ensure your **battery is fully charged** or connected to a charger
2. Go to the **Flash** tab
3. Review the **matching tunes** (if any are found)
4. Click **Select .bin File** and choose your tune file
5. Click **Flash ECU**
6. Confirm the battery warning
7. **Do not disconnect power or cable during flashing**
8. Wait for completion and verification

### 4. Read/Clear Diagnostic Codes

1. Go to the **DTC** tab
2. Click **Read DTCs** to view all diagnostic trouble codes
3. Click **Clear DTCs** to remove them (if desired)

---

## 📁 Project Structure

```
RFTX_SOFTWARE-main/
├── main.py                 # Application entry point
├── rftx_gui.py             # PyQt6 GUI implementation
├── RFTX_FLASHER.py         # Core ECU communication and flashing logic
├── tune_matcher.py         # Intelligent tune matching system
├── pyproject.toml          # Project configuration and dependencies
├── requirements.txt        # Pip requirements (core)
├── requirements-dev.txt    # Pip requirements (development)
├── requirements-lock.txt   # Pinned versions for reproducible builds
├── uv.lock                 # UV locked dependencies
├── README.md               # This file
├── RFTX.log                # GUI operation log
└── rftx_flasher.log        # Flasher operation log
```

---

## ⚠️ Safety Warnings

### Critical Safety Information

1. **Stable Power Supply**
   - Ensure your vehicle's battery is **fully charged** (12.5V+)
   - Consider using an **external battery charger** during flashing
   - **Power loss during flashing can permanently damage your ECU**

2. **Valid Tune Files**
   - Only use **.bin files** that are compatible with your specific ECU type
   - Incorrect tune files can cause **engine damage** or **ECU failure**
   - Always verify the source and compatibility of tune files

3. **Backup Before Flashing**
   - **Always create a backup** of your original ECU firmware
   - Store backups in multiple safe locations
   - A backup allows you to restore your ECU if something goes wrong

4. **Legal Considerations**
   - ECU tuning may **void your vehicle warranty**
   - Modified emissions systems may be **illegal** in your jurisdiction
   - Track use only where applicable
   - **Use at your own risk**

5. **During Flashing**
   - Do not disconnect the **K+DCAN cable**
   - Do not turn off the **ignition**
   - Do not start the **engine**
   - Do not **interrupt** the flashing process
   - Monitor the progress bar and status messages

---

## 🛠️ Advanced Usage

### Command-Line Interface

RFTX FLASHER can also be used from the command line:

```bash
# Read ECU information
python RFTX_FLASHER.py --port COM3 --info

# Backup ECU
python RFTX_FLASHER.py --port COM3 --backup backup.bin

# Flash ECU
python RFTX_FLASHER.py --port COM3 --flash tune.bin

# Read DTCs
python RFTX_FLASHER.py --port COM3 --dtcs

# Clear DTCs
python RFTX_FLASHER.py --port COM3 --clear-dtcs

# Reset ECU
python RFTX_FLASHER.py --port COM3 --reset
```

### Tune Organization

For best results with automatic tune matching, organize your tune files:

```
tunes/
├── N54_Stage1/
│   ├── tune_info.json
│   └── N54_Stage1_Pump.bin
├── N55_Stage2/
│   ├── tune_info.json
│   └── N55_Stage2_E85.bin
└── [other tunes]
```

Create a `tune_info.json` file for precise matching:

```json
{
  "tunes": [
    {
      "ecu_id": "MSD80",
      "engine_code": "N54",
      "sw_version": "SW12345",
      "bin_files": ["N54_Stage1_Pump.bin"],
      "description": "Stage 1 tune for N54 on pump gas"
    }
  ]
}
```

---

## 🐛 Troubleshooting

### Connection Issues

**Problem**: "No suitable COM ports found"
- **Solution**: Check that your K+DCAN cable is properly connected
- Install the appropriate USB drivers for your cable
- Try a different USB port

**Problem**: "Failed to connect to ECU"
- **Solution**: Ensure ignition is ON (engine OFF)
- Check that no other diagnostic software is connected
- Verify the cable is fully seated in the OBD-II port
- Try cycling the ignition off and on

### Flashing Issues

**Problem**: Flash verification failed
- **Solution**: Ensure the .bin file is valid and compatible
- Check battery voltage (should be 12V+)
- Retry the flash operation

**Problem**: ECU won't start after flashing
- **Solution**: Restore your backup file
- Reset the ECU
- If issues persist, seek professional help

### Low Battery Warning

**Problem**: "Low battery voltage: X.XV"
- **Solution**: Connect a battery charger before proceeding
- Do not attempt to flash with low voltage
- Risk of ECU damage if power is lost during flashing

---

## 📊 Technical Details

### Memory Architecture

Each ECU type has specific memory sectors:

- **Bootloader**: Protected sector (not flashed)
- **Calibration**: Contains tuning maps (flashed)
- **Program**: Contains ECU firmware (protected)

### Communication Flow

1. **Connection**: Establish serial communication via K+DCAN
2. **Protocol Detection**: Automatically detect UDS or KWP2000
3. **Session Control**: Enter programming session
4. **Security Access**: Calculate and send security key
5. **Memory Operations**: Read, write, or erase operations
6. **Verification**: Compare written data with source file
7. **Session Exit**: Return to default diagnostic session

### Supported Operations

| Operation | UDS | KWP2000 |
|-----------|-----|---------|
| Read ECU Info | ✅ | ✅ |
| Flash ECU | ✅ | ✅ |
| Backup ECU | ✅ | ✅ |
| Read DTCs | ✅ | ✅ |
| Clear DTCs | ✅ | ✅ |
| Reset ECU | ✅ | ✅ |

---

## 🗺️ Roadmap

### Coming Soon

- **Additional ECU Support**: MSV70, MSV80, DME7
- **Live Data Monitoring**: Real-time engine parameters
- **Data Logging**: Record and analyze engine data
- **Tune Comparison**: Compare multiple tune files
- **Cloud Tune Library**: Access to pre-made tunes
- **Multi-language Support**: Interface localization

### Future Features

- **Android/iOS App**: Mobile ECU flashing
- **OTA Updates**: Over-the-air tune updates
- **Community Features**: Share and rate tunes
- **Advanced Diagnostics**: More comprehensive ECU analysis

---

## 📞 Support & Contact

### Getting Help

- **Email**: rftxtuning@gmail.com
- **Issues**: Report bugs and request features on GitHub
- **Logs**: Check `RFTX.log` and `rftx_flasher.log` for debugging

### Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear descriptions

---

## 📜 Disclaimer

This software is provided **"as-is"** without any warranties. The developers are not responsible for:

- Vehicle damage
- ECU failure
- Warranty voidance
- Legal consequences
- Improper use

**Use at your own risk.** Always create backups and ensure you understand the risks before modifying your vehicle's ECU.

---

## 🎓 Credits & Acknowledgments

**RFTX TUNING** is developed and maintained by the RFTX team.

Special thanks to:
- The BMW tuning community
- Open-source diagnostic protocol researchers
- All contributors and beta testers

---

## 📄 License

This project is released as **free software** for the community.

**Our Mission**: To make tuning accessible and free for everyone.

---

## 🌟 Show Your Support

If you find RFTX TUNING useful:
- ⭐ Star this repository
- 📢 Share with the BMW community
- 🐛 Report bugs and suggest features
- 💝 Consider donating to support development

---

**Made with ❤️ by RFTX TUNING Team**

*Empowering the BMW tuning community, one flash at a time.*

