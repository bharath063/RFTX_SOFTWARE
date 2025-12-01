# Quick Start: Building & Releasing RFTX TUNING

## 🚀 For Developers: Get Started in 5 Minutes

### 1️⃣ One-Time Setup

```bash
# Install UV (Fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# OR
curl -LsSf https://astral.sh/uv/install.ps1 | powershell  # Windows

# Clone and setup
git clone <your-repo-url>
cd RFTX_SOFTWARE-main
uv sync
uv pip install pyinstaller
```

### 2️⃣ Build Locally

```bash
# Build executable for your platform
uv run python build.py

# Find your executable in:
# - Windows: releases/RFTX_Tuning-v1.0.0-Windows-x64.zip
# - macOS:   releases/RFTX_Tuning-v1.0.0-macOS-Universal.tar.gz
# - Linux:   releases/RFTX_Tuning-v1.0.0-Linux-x64.tar.gz
```

### 3️⃣ Create a Release

```bash
# Bump version (patch/minor/major)
uv run python bump_version.py minor

# Commit and push to main
git add -A
git commit -m "Release v1.1.0"
git push origin main

# 🎉 GitHub Actions automatically:
# - Builds for Windows, macOS, Linux
# - Creates GitHub release
# - Tags the version
# - Generates release notes
```

---

## 📁 What Got Created

### Build System Files

```
RFTX_SOFTWARE-main/
│
├── build.py                    # ✅ Build script for cross-platform binaries
├── bump_version.py            # ✅ Version management script
├── BUILD_GUIDE.md             # ✅ Comprehensive build documentation
├── CHANGELOG.md               # ✅ Version history
├── LICENSE.txt                # ✅ MIT License with disclaimers
├── .gitignore                 # ✅ Git ignore rules
│
├── .github/
│   ├── workflows/
│   │   ├── release.yml        # ✅ Auto-release on main push
│   │   └── build-test.yml     # ✅ Test builds on PRs
│   └── RELEASE_TEMPLATE.md    # ✅ Release notes template
│
├── pyproject.toml             # ✅ Updated with build dependencies
│
├── releases/                  # ⬅️ Build output goes here
│   └── .gitkeep
│
└── tunes/                     # ⬅️ Place your tune files here
    └── .gitkeep
```

---

## 🔄 Release Workflow

### Automatic (Recommended)

```
1. Make changes → 2. Bump version → 3. Push to main → 4. ✨ Release Created!
```

**What happens automatically:**
- ✅ Builds on Windows, macOS, Linux runners
- ✅ Creates release archives (.zip/.tar.gz)
- ✅ Generates SHA256 checksums
- ✅ Creates Git tag (v1.0.0)
- ✅ Publishes GitHub release
- ✅ Generates release notes from commits

### Manual Build (Testing)

```bash
# Build locally
uv run python build.py

# Test the executable
./dist/RFTX_Tuning  # Linux/macOS
# OR
./dist/RFTX_Tuning.exe  # Windows
```

---

## 🎯 Quick Commands

```bash
# Build
uv run python build.py

# Bump patch version (1.0.0 → 1.0.1)
uv run python bump_version.py patch

# Bump minor version (1.0.0 → 1.1.0)
uv run python bump_version.py minor

# Bump major version (1.0.0 → 2.0.0)
uv run python bump_version.py major

# Set specific version
uv run python bump_version.py 2.5.0

# Check current version
grep 'version = ' pyproject.toml
```

---

## 📦 What Users Get

When users download from GitHub Releases:

**Windows Users**:
```
RFTX_Tuning-v1.0.0-Windows-x64.zip
├── RFTX_Tuning.exe       ← Standalone executable
├── README.md
└── LICENSE.txt
```

**macOS Users**:
```
RFTX_Tuning-v1.0.0-macOS-Universal.tar.gz
├── RFTX_Tuning.app/      ← App bundle (Intel & Apple Silicon)
├── README.md
└── LICENSE.txt
```

**Linux Users**:
```
RFTX_Tuning-v1.0.0-Linux-x64.tar.gz
├── RFTX_Tuning           ← Executable
├── README.md
└── LICENSE.txt
```

**No Python required!** All dependencies are bundled.

---

## ⚙️ GitHub Actions Setup

### Required Secrets: **NONE** ✅

GitHub Actions uses `GITHUB_TOKEN` automatically (no setup needed).

### Workflow Triggers

1. **Automatic Release**: Push to `main` branch
2. **Build Test**: Pull requests or other branches
3. **Manual**: Actions tab → Run workflow

---

## 🔍 Verify It Works

### Test Local Build

```bash
# 1. Build
uv run python build.py

# 2. Check releases directory
ls -lh releases/

# Should see:
# RFTX_Tuning-v1.0.0-[Platform].zip/tar.gz
# checksums.txt
```

### Test Version Bump

```bash
# Dry run (won't actually change files when you cancel)
uv run python bump_version.py patch
# Press 'n' to cancel after reviewing changes
```

### Test GitHub Actions (After Push)

```bash
# 1. Commit something
git add .
git commit -m "Test release workflow"

# 2. Push to main
git push origin main

# 3. Check GitHub:
# - Actions tab: See build progress
# - Releases: New release appears (if version changed)
# - Tags: New tag created
```

---

## 🛠️ Troubleshooting

### Build Fails

**Error**: `PyInstaller not found`
```bash
uv pip install pyinstaller
```

**Error**: UV not found
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Error**: Permission denied (macOS/Linux)
```bash
chmod +x build.py bump_version.py
```

### GitHub Actions Issues

**Workflow doesn't run**:
- Ensure `.github/workflows/release.yml` exists
- Check you're pushing to `main` branch
- Look at Actions tab for errors

**Release not created**:
- Check if version already has a release/tag
- Bump version number
- Check Actions logs for errors

---

## 📚 Documentation

- **[BUILD_GUIDE.md](BUILD_GUIDE.md)**: Complete build documentation
- **[README.md](README.md)**: User documentation
- **[CHANGELOG.md](CHANGELOG.md)**: Version history

---

## ✅ Pre-Release Checklist

Before creating a release:

- [ ] All code changes committed
- [ ] Tests pass (if you add tests)
- [ ] Version bumped
- [ ] CHANGELOG.md updated
- [ ] Build tested locally
- [ ] README.md updated (if needed)

---

## 🎉 You're Ready!

Everything is set up for automated cross-platform releases. Just:

1. **Develop** your features
2. **Bump** version when ready
3. **Push** to main
4. **Relax** while GitHub Actions does the work! ☕

For detailed information, see **[BUILD_GUIDE.md](BUILD_GUIDE.md)**.

---

**Questions?** rftxtuning@gmail.com

