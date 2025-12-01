# RFTX TUNING - Build & Release Guide

This guide explains how to build cross-platform binaries and create releases for RFTX TUNING.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Build](#local-build)
3. [Version Management](#version-management)
4. [Creating Releases](#creating-releases)
5. [GitHub Actions](#github-actions)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

- **Python 3.12+**: Main programming language
- **UV**: Fast Python package installer
- **Git**: Version control
- **PyInstaller**: For creating executables

### Platform-Specific Requirements

#### Windows
- Visual C++ Redistributable (usually pre-installed)
- PowerShell 5.1 or later

#### macOS
- Xcode Command Line Tools: `xcode-select --install`
- macOS 11+ for building

#### Linux
- Required packages:
```bash
sudo apt-get update
sudo apt-get install -y libxcb-xinerama0 libxcb-cursor0 libxkbcommon-x11-0
```

---

## Local Build

### 1. Install UV (if not already installed)

**Windows (PowerShell)**:
```powershell
curl -LsSf https://astral.sh/uv/install.ps1 | powershell
```

**macOS/Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/RFTX-TUNING/RFTX_SOFTWARE.git
cd RFTX_SOFTWARE

# Install dependencies
uv sync

# Install build tools
uv pip install pyinstaller
```

### 3. Build Executable

```bash
# Run the build script
uv run python build.py
```

This will:
- ✅ Clean previous build artifacts
- ✅ Create platform-specific executable
- ✅ Package into release archive
- ✅ Generate checksums

### 4. Output

After building, you'll find:

```
releases/
├── RFTX_Tuning-vx.y.z-Windows-x64.zip       (Windows)
├── RFTX_Tuning-vx.y.z-macOS-Universal.tar.gz (macOS)
├── RFTX_Tuning-vx.y.z-Linux-x64.tar.gz      (Linux)
└── checksums.txt
```

---

### Bump Version

Use the `bump_version.py` script:

```bash
# Bump patch version (0.0.X)
uv run python bump_version.py patch

# Bump minor version (0.X.0)
uv run python bump_version.py minor

# Bump major version (X.0.0)
uv run python bump_version.py major

# Set specific version
uv run python bump_version.py 2.0.0
```

The script will:
1. ✅ Update version in all relevant files
2. ✅ Update changelog
3. ✅ Show you what changed
4. ✅ Prompt for confirmation

After bumping:
```bash
git add -A
git commit -m "Bump version to v1.1.0"
git push origin main
```

---

## Creating Releases

### Automatic Releases (Recommended)

**When you push to `main` branch**, GitHub Actions automatically:

1. ✅ Detects version from `pyproject.toml`
2. ✅ Builds for Windows, macOS, and Linux
3. ✅ Creates release archives
4. ✅ Generates checksums
5. ✅ Creates Git tag
6. ✅ Publishes GitHub release with notes

**Workflow**:
```bash
# 1. Bump version
uv run python bump_version.py minor

# 2. Commit and push
git add -A
git commit -m "Release v1.1.0"
git push origin main

# 3. GitHub Actions creates release automatically! 🎉
```

### Manual Release

If you need to manually create a release:

```bash
# 1. Build on each platform
uv run python build.py

# 2. Collect all artifacts in releases/

# 3. Create tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# 4. Create GitHub release manually
# Upload files from releases/ directory
```

---

## GitHub Actions

### Workflows

#### 1. `release.yml` - Automated Releases

**Triggers**:
- Push to `main` branch
- Manual workflow dispatch

**Jobs**:
1. **version**: Determine version and check if release needed
2. **build-windows**: Build Windows executable
3. **build-macos**: Build macOS app bundle
4. **build-linux**: Build Linux executable
5. **release**: Create GitHub release with all artifacts

**Features**:
- ✅ Multi-platform builds in parallel
- ✅ Automatic version detection
- ✅ Duplicate release prevention
- ✅ Automatic release notes generation
- ✅ SHA256 checksums
- ✅ Git tagging

#### 2. `build-test.yml` - Build Testing

**Triggers**:
- Pull requests to `main`
- Push to non-main branches

**Purpose**:
- Test that builds work on all platforms
- No release creation
- Verify executables are created

### Manual Workflow Trigger

You can manually trigger a release from GitHub:

1. Go to **Actions** tab
2. Select **Build and Release** workflow
3. Click **Run workflow**
4. Choose branch and optionally specify version
5. Click **Run workflow**

---

## Configuration Files

### `pyproject.toml`

Main project configuration:
```toml
[project]
name = "rftx-tuning"
version = "1.0.0"  # ← Version is read from here
```

### `build.py`

Build script configuration:
```python
APP_NAME = "RFTX_Tuning"
VERSION = "1.0.0"  # ← Keep in sync with pyproject.toml
```

### `.github/workflows/release.yml`

GitHub Actions workflow for releases.

### `.github/workflows/build-test.yml`

GitHub Actions workflow for testing builds.

---

## Troubleshooting

### Build Fails

**Problem**: PyInstaller not found
```bash
# Solution: Install PyInstaller
uv pip install pyinstaller
```

**Problem**: UV not found
```bash
# Solution: Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Problem**: Build fails on Linux
```bash
# Solution: Install system dependencies
sudo apt-get install -y libxcb-xinerama0 libxcb-cursor0 libxkbcommon-x11-0
```

### Version Issues

**Problem**: Version mismatch between files
```bash
# Solution: Use bump_version.py to update all files
uv run python bump_version.py patch
```

**Problem**: Tag already exists
```bash
# Solution: Delete tag and recreate
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```

### GitHub Actions Issues

**Problem**: Workflow doesn't trigger
- Check that you're pushing to `main` branch
- Ensure workflow file is in `.github/workflows/`
- Check Actions tab for errors

**Problem**: Build fails in Actions
- Check the logs in the Actions tab
- Common issues:
  - Missing dependencies
  - Incorrect paths
  - Version conflicts

**Problem**: Release already exists
- The workflow skips if a release with the same version exists
- Bump version or manually delete the release/tag

---

## Testing Builds Locally

Before pushing, test builds locally:

```bash
# Test build script
uv run python build.py

# Test version bump (dry run)
uv run python bump_version.py patch
# (then don't commit if just testing)

# Test that executable runs
# Windows
./dist/RFTX_Tuning.exe

# macOS
./dist/RFTX_Tuning.app/Contents/MacOS/RFTX_Tuning

# Linux
./dist/RFTX_Tuning
```

---

## Release Checklist

Before creating a release:

- [ ] All tests pass
- [ ] Version bumped appropriately
- [ ] CHANGELOG.md updated
- [ ] README.md up to date
- [ ] All features documented
- [ ] Known issues listed
- [ ] Build tested locally
- [ ] Commits are clean and descriptive

---

## Best Practices

### Versioning

1. **Use semantic versioning** consistently
2. **Document breaking changes** in CHANGELOG
3. **Test before releasing** on all platforms
4. **Use bump_version.py** to avoid manual errors

### Git Workflow

1. **Feature branches** for development
2. **Pull requests** for code review
3. **Main branch** for releases only
4. **Descriptive commit messages**

### Release Notes

1. **Clear and concise** descriptions
2. **List new features** prominently
3. **Document breaking changes**
4. **Include upgrade instructions**
5. **Reference related issues/PRs**

---

## Advanced: Custom Build Options

### Modify Build Script

Edit `build.py` to customize:

```python
# Change app name
APP_NAME = "RFTX_Custom"

# Add custom data files
data_args = [
    "--add-data", "custom_folder:.",
]

# Add more hidden imports
hidden_imports = [
    "--hidden-import", "custom_module",
]
```

### Custom PyInstaller Spec

The build script generates a `.spec` file. You can customize it:

```bash
# Generate spec file
uv run python build.py

# Edit RFTX_Tuning.spec
# (make your changes)

# Build with custom spec
pyinstaller RFTX_Tuning.spec
```

---

## Support

For build-related issues:

- **Email**: rftxtuning@gmail.com
- **GitHub Issues**: [Report problems](https://github.com/RFTX-TUNING/RFTX_SOFTWARE/issues)
- **Discussions**: [Ask questions](https://github.com/RFTX-TUNING/RFTX_SOFTWARE/discussions)

---

## Additional Resources

- [PyInstaller Documentation](https://pyinstaller.org/en/stable/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Semantic Versioning](https://semver.org/)

---

**Happy Building! 🚀**

