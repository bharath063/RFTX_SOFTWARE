#!/usr/bin/env python3
"""
RFTX TUNING - Version Management Script
Automatically bumps version numbers in all relevant files
"""

import re
import sys
from pathlib import Path
from typing import Tuple, Optional

# Files to update
VERSION_FILES = {
    'pyproject.toml': r'version\s*=\s*"([^"]+)"',
    'build.py': r'VERSION\s*=\s*"([^"]+)"',
    'rftx_gui.py': r'v\d+\.\d+',  # For footer version display
}

def parse_version(version_str: str) -> Tuple[int, int, int]:
    """Parse a semantic version string into components."""
    match = re.match(r'(\d+)\.(\d+)\.(\d+)', version_str)
    if not match:
        raise ValueError(f"Invalid version format: {version_str}")
    return tuple(map(int, match.groups()))

def format_version(major: int, minor: int, patch: int) -> str:
    """Format version components into a string."""
    return f"{major}.{minor}.{patch}"

def get_current_version() -> str:
    """Get the current version from pyproject.toml."""
    pyproject_path = Path('pyproject.toml')
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")
    
    content = pyproject_path.read_text()
    match = re.search(r'version\s*=\s*"([^"]+)"', content)
    if not match:
        raise ValueError("Version not found in pyproject.toml")
    
    return match.group(1)

def bump_version(version: str, bump_type: str = 'patch') -> str:
    """Bump the version based on the specified type."""
    major, minor, patch = parse_version(version)
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}. Use 'major', 'minor', or 'patch'")
    
    return format_version(major, minor, patch)

def update_file(file_path: Path, pattern: str, old_version: str, new_version: str) -> bool:
    """Update version in a specific file."""
    if not file_path.exists():
        print(f"⚠️  Skipping {file_path} (not found)")
        return False
    
    content = file_path.read_text()
    original_content = content
    
    # Replace version based on the pattern
    if 'pyproject.toml' in str(file_path):
        content = re.sub(
            r'(version\s*=\s*")([^"]+)(")',
            f'\\g<1>{new_version}\\g<3>',
            content
        )
    elif 'build.py' in str(file_path):
        content = re.sub(
            r'(VERSION\s*=\s*")([^"]+)(")',
            f'\\g<1>{new_version}\\g<3>',
            content
        )
    elif 'rftx_gui.py' in str(file_path):
        content = re.sub(
            r'v\d+\.\d+',
            f'v{new_version}',
            content
        )
    
    if content != original_content:
        file_path.write_text(content)
        print(f"✅ Updated {file_path}")
        return True
    else:
        print(f"⚠️  No changes in {file_path}")
        return False

def update_all_files(old_version: str, new_version: str) -> int:
    """Update version in all relevant files."""
    updated_count = 0
    
    for file_name, pattern in VERSION_FILES.items():
        file_path = Path(file_name)
        if update_file(file_path, pattern, old_version, new_version):
            updated_count += 1
    
    return updated_count

def create_changelog_entry(version: str, bump_type: str) -> None:
    """Create a changelog entry for the new version."""
    changelog_path = Path('CHANGELOG.md')
    
    # Get today's date
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    
    entry = f"""
## [{version}] - {today}

### {bump_type.capitalize()}
- Version bump to {version}
- See git log for detailed changes

"""
    
    if changelog_path.exists():
        # Prepend to existing changelog
        content = changelog_path.read_text()
        # Insert after the first header
        lines = content.split('\n')
        header_end = 0
        for i, line in enumerate(lines):
            if line.startswith('## ['):
                header_end = i
                break
        
        if header_end > 0:
            lines.insert(header_end, entry)
        else:
            lines.insert(0, entry)
        
        changelog_path.write_text('\n'.join(lines))
    else:
        # Create new changelog
        changelog_content = f"""# Changelog

All notable changes to RFTX TUNING will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

{entry}
"""
        changelog_path.write_text(changelog_content)
    
    print(f"✅ Updated {changelog_path}")

def main():
    """Main version bump process."""
    print("=" * 60)
    print("🔢 RFTX TUNING - Version Bump Script")
    print("=" * 60)
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python bump_version.py [major|minor|patch]")
        print("  python bump_version.py [specific version, e.g., 2.0.0]")
        print("\nBump types:")
        print("  major - Increment major version (X.0.0)")
        print("  minor - Increment minor version (0.X.0)")
        print("  patch - Increment patch version (0.0.X)")
        print("\nCurrent version:", get_current_version())
        sys.exit(1)
    
    # Get current version
    try:
        current_version = get_current_version()
        print(f"\n📌 Current version: {current_version}")
    except Exception as e:
        print(f"❌ Error getting current version: {e}")
        sys.exit(1)
    
    # Determine new version
    arg = sys.argv[1].lower()
    
    if arg in ['major', 'minor', 'patch']:
        bump_type = arg
        try:
            new_version = bump_version(current_version, bump_type)
        except Exception as e:
            print(f"❌ Error bumping version: {e}")
            sys.exit(1)
    else:
        # Assume it's a specific version
        try:
            parse_version(arg)  # Validate format
            new_version = arg
            bump_type = 'manual'
        except ValueError as e:
            print(f"❌ Invalid version format: {e}")
            print("Please use semantic versioning (e.g., 1.2.3)")
            sys.exit(1)
    
    print(f"🆕 New version: {new_version}")
    
    # Confirm with user
    response = input("\nProceed with version bump? [y/N]: ").strip().lower()
    if response != 'y':
        print("❌ Version bump cancelled")
        sys.exit(0)
    
    # Update all files
    print("\n📝 Updating files...")
    updated_count = update_all_files(current_version, new_version)
    
    # Create changelog entry
    if bump_type != 'manual':
        create_changelog_entry(new_version, bump_type)
    
    print("\n" + "=" * 60)
    print("✅ Version bump completed!")
    print(f"   {current_version} → {new_version}")
    print(f"   Updated {updated_count} file(s)")
    print("\n📋 Next steps:")
    print("   1. Review the changes")
    print("   2. Commit: git add -A && git commit -m 'Bump version to {}'".format(new_version))
    print("   3. Push: git push origin main")
    print("   4. GitHub Actions will automatically create a release")
    print("=" * 60)

if __name__ == "__main__":
    main()

