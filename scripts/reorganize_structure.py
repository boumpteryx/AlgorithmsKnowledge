#!/usr/bin/env python3
"""
Script to reorganize repository structure by moving detail pages into subfolders.
This ensures README.md files are not at the same level as all detail pages.
"""

import os
import shutil
from pathlib import Path

# Define the repository root
REPO_ROOT = Path(__file__).parent.parent

# Directories to reorganize
DIRECTORIES = [
    'symbolic-ai',
    'data-science',
    'machine-learning',
    'deep-learning',
    'mlops',
    'quantum-computing',
    'distributed-systems'
]

def reorganize_directory(directory):
    """Move all .md files (except README.md) into a 'pages' subfolder."""
    dir_path = REPO_ROOT / directory
    
    if not dir_path.exists():
        print(f"Directory {directory} does not exist, skipping...")
        return
    
    # Create pages subfolder
    pages_dir = dir_path / 'pages'
    pages_dir.mkdir(exist_ok=True)
    
    # Find all .md files in the directory (not in subdirectories)
    md_files = [f for f in dir_path.glob('*.md') if f.name != 'README.md']
    
    if not md_files:
        print(f"No files to move in {directory}")
        return
    
    print(f"\nReorganizing {directory}:")
    print(f"  Moving {len(md_files)} files to pages/ subfolder...")
    
    # Move each file
    for md_file in md_files:
        dest = pages_dir / md_file.name
        shutil.move(str(md_file), str(dest))
        print(f"    Moved: {md_file.name}")
    
    print(f"  [OK] Completed {directory}")

def update_readme_links(directory):
    """Update links in README.md to point to pages/ subfolder."""
    readme_path = REPO_ROOT / directory / 'README.md'
    
    if not readme_path.exists():
        return
    
    print(f"\nUpdating links in {directory}/README.md...")
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace links: [text](file.md) -> [text](pages/file.md)
    # But skip links that already have paths or are external
    import re
    
    def replace_link(match):
        text = match.group(1)
        link = match.group(2)
        
        # Skip if already has a path, is external, or is README.md
        if '/' in link or link.startswith('http') or link.startswith('#') or link == 'README.md' or link.startswith('..'):
            return match.group(0)
        
        # Add pages/ prefix
        return f'[{text}](pages/{link})'
    
    # Pattern to match markdown links
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    updated_content = re.sub(pattern, replace_link, content)
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"  [OK] Updated links in {directory}/README.md")

def main():
    """Main function to reorganize all directories."""
    print("=" * 60)
    print("Reorganizing repository structure...")
    print("=" * 60)
    
    for directory in DIRECTORIES:
        reorganize_directory(directory)
        update_readme_links(directory)
    
    print("\n" + "=" * 60)
    print("Reorganization complete!")
    print("\nNew structure:")
    print("  <topic>/")
    print("    README.md")
    print("    pages/")
    print("      <detail-page-1>.md")
    print("      <detail-page-2>.md")
    print("      ...")
    print("    diagrams/")
    print("      ...")
    print("=" * 60)

if __name__ == '__main__':
    main()

# Made with Bob
