#!/usr/bin/env python3
"""
RFTX TUNING - Build Script
Creates cross-platform executables for Windows, macOS, and Linux
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path

# Build configuration
APP_NAME = "RFTX_Tuning"
VERSION = "0.0.1"
MAIN_SCRIPT = "main.py"
ICON_FILE = "icon.png"  # Will be converted to .ico/.icns as needed

# Platform detection
PLATFORM = platform.system().lower()
IS_WINDOWS = PLATFORM == "windows"
IS_MACOS = PLATFORM == "darwin"
IS_LINUX = PLATFORM == "linux"

# Build directories
BUILD_DIR = Path("build")
DIST_DIR = Path("dist")
RELEASE_DIR = Path("releases")

def clean_build_dirs():
    """Clean previous build artifacts."""
    print("🧹 Cleaning build directories...")
    dirs_to_clean = [BUILD_DIR, DIST_DIR]
    for dir_path in dirs_to_clean:
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"   Removed {dir_path}")
    
    # Create release directory if it doesn't exist
    RELEASE_DIR.mkdir(exist_ok=True)
    print(f"   Created {RELEASE_DIR}")

def get_platform_specific_args():
    """Get platform-specific PyInstaller arguments."""
    common_args = [
        "--name", APP_NAME,
        "--onefile",
        "--windowed",
        "--clean",
        "--noconfirm",
    ]
    
    # Add additional data files
    data_args = [
        "--add-data", f"README.md{os.pathsep}.",
        "--add-data", f"pyproject.toml{os.pathsep}.",
    ]
    
    # Platform-specific arguments
    platform_args = []
    
    if IS_WINDOWS:
        platform_args.extend([
            "--icon", "icon.ico" if os.path.exists("icon.ico") else None,
            "--version-file", "version_info.txt" if os.path.exists("version_info.txt") else None,
        ])
    elif IS_MACOS:
        platform_args.extend([
            "--icon", "icon.icns" if os.path.exists("icon.icns") else None,
            "--osx-bundle-identifier", "com.rftx.tuning",
            "--target-arch", "universal2",  # Build for both Intel and Apple Silicon
        ])
    elif IS_LINUX:
        platform_args.extend([
            "--icon", "icon.png" if os.path.exists("icon.png") else None,
        ])
    
    # Filter out None values
    platform_args = [arg for arg in platform_args if arg is not None]
    
    # Hidden imports for PyQt5 and other dependencies
    hidden_imports = [
        "--hidden-import", "PyQt5",
        "--hidden-import", "PyQt5.QtCore",
        "--hidden-import", "PyQt5.QtGui",
        "--hidden-import", "PyQt5.QtWidgets",
        "--hidden-import", "serial",
        "--hidden-import", "serial.tools.list_ports",
    ]
    
    # Collect all arguments
    all_args = common_args + data_args + platform_args + hidden_imports + [MAIN_SCRIPT]
    
    return all_args

def create_spec_file():
    """Create a custom .spec file for PyInstaller."""
    print("📝 Creating .spec file...")
    
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['{MAIN_SCRIPT}'],
    pathex=[],
    binaries=[],
    datas=[
        ('README.md', '.'),
        ('pyproject.toml', '.'),
    ],
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'serial',
        'serial.tools.list_ports',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{APP_NAME}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    if IS_MACOS:
        spec_content += f'''
app = BUNDLE(
    exe,
    name='{APP_NAME}.app',
    icon='icon.icns' if os.path.exists('icon.icns') else None,
    bundle_identifier='com.rftx.tuning',
    info_plist={{
        'NSHighResolutionCapable': 'True',
        'CFBundleShortVersionString': '{VERSION}',
        'CFBundleVersion': '{VERSION}',
    }},
)
'''
    
    with open(f"{APP_NAME}.spec", "w") as f:
        f.write(spec_content)
    
    print(f"   Created {APP_NAME}.spec")

def build_executable():
    """Build the executable using PyInstaller."""
    print(f"🔨 Building executable for {PLATFORM}...")
    
    # Create spec file
    create_spec_file()
    
    # Run PyInstaller with the spec file
    cmd = ["pyinstaller", f"{APP_NAME}.spec"]
    
    print(f"   Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ Build failed!")
        print(result.stderr)
        sys.exit(1)
    
    print("✅ Build completed successfully!")

def package_release():
    """Package the built executable for distribution."""
    print("📦 Packaging release...")
    
    # Determine the executable name/path
    if IS_WINDOWS:
        exe_name = f"{APP_NAME}.exe"
        exe_path = DIST_DIR / exe_name
        archive_name = f"{APP_NAME}-v{VERSION}-Windows-x64"
    elif IS_MACOS:
        exe_name = f"{APP_NAME}.app"
        exe_path = DIST_DIR / exe_name
        archive_name = f"{APP_NAME}-v{VERSION}-macOS-Universal"
    else:  # Linux
        exe_name = APP_NAME
        exe_path = DIST_DIR / exe_name
        archive_name = f"{APP_NAME}-v{VERSION}-Linux-x64"
    
    # Check if executable exists
    if not exe_path.exists():
        print(f"❌ Executable not found: {exe_path}")
        sys.exit(1)
    
    # Create a temporary directory for packaging
    temp_dir = RELEASE_DIR / archive_name
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy executable
    if IS_MACOS:
        # Copy the entire .app bundle
        shutil.copytree(exe_path, temp_dir / exe_name, dirs_exist_ok=True)
    else:
        shutil.copy2(exe_path, temp_dir / exe_name)
    
    # Copy additional files
    additional_files = ["README.md", "LICENSE.txt"]
    for file in additional_files:
        if Path(file).exists():
            shutil.copy2(file, temp_dir / file)
    
    # Create archive
    print(f"   Creating archive: {archive_name}")
    
    if IS_WINDOWS:
        # Create ZIP for Windows
        archive_path = RELEASE_DIR / f"{archive_name}.zip"
        shutil.make_archive(
            str(RELEASE_DIR / archive_name),
            'zip',
            RELEASE_DIR,
            archive_name
        )
    else:
        # Create tar.gz for macOS and Linux
        archive_path = RELEASE_DIR / f"{archive_name}.tar.gz"
        shutil.make_archive(
            str(RELEASE_DIR / archive_name),
            'gztar',
            RELEASE_DIR,
            archive_name
        )
    
    # Clean up temporary directory
    shutil.rmtree(temp_dir)
    
    print(f"✅ Release package created: {archive_path}")
    return archive_path

def calculate_checksum(file_path):
    """Calculate SHA256 checksum of a file."""
    import hashlib
    
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    return sha256_hash.hexdigest()

def create_checksums():
    """Create checksum file for all release archives."""
    print("🔐 Generating checksums...")
    
    checksum_file = RELEASE_DIR / "checksums.txt"
    
    with open(checksum_file, "w") as f:
        f.write(f"RFTX TUNING v{VERSION} - SHA256 Checksums\n")
        f.write("=" * 60 + "\n\n")
        
        # Combine both .zip and .tar.gz files
        archives = list(RELEASE_DIR.glob("*.zip")) + list(RELEASE_DIR.glob("*.tar.gz"))
        for archive in archives:
            if archive.name != "checksums.txt":
                checksum = calculate_checksum(archive)
                f.write(f"{checksum}  {archive.name}\n")
                print(f"   {archive.name}: {checksum}")
    
    print(f"✅ Checksums saved to {checksum_file}")

def main():
    """Main build process."""
    print("=" * 60)
    print(f"🚀 RFTX TUNING v{VERSION} - Build Script")
    print(f"Platform: {PLATFORM.upper()}")
    print("=" * 60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build process
    clean_build_dirs()
    build_executable()
    archive_path = package_release()
    
    # Calculate checksums
    create_checksums()
    
    print("\n" + "=" * 60)
    print("✅ Build completed successfully!")
    print(f"📦 Release package: {archive_path}")
    print(f"📁 All releases in: {RELEASE_DIR}/")
    print("=" * 60)

if __name__ == "__main__":
    main()

