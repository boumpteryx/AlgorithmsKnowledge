#!/usr/bin/env python3
"""
Script to create placeholder markdown files for all broken links in the repository.
This ensures all links in README files point to valid pages.
"""

import os
import re
from pathlib import Path

# Define the repository root
REPO_ROOT = Path(__file__).parent.parent

# Template for placeholder pages
PLACEHOLDER_TEMPLATE = """# {title}

[← Back to {parent}](README.md)

## Overview

This page is currently under development. Please check back later for detailed content.

## Coming Soon

Detailed information about {title} will be added here, including:
- Core concepts and definitions
- Practical examples and use cases
- Best practices and guidelines
- Related resources and references

## Related Topics

- [Back to {parent}](README.md)

---

*This page is part of the Algorithms Knowledge Base. Content is being actively developed.*
"""

def extract_links_from_file(file_path):
    """Extract all markdown links from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match markdown links: [text](link.md)
    # Exclude external links (http/https) and anchors (#)
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    matches = re.findall(pattern, content)
    
    # Filter out external links and anchors
    links = []
    for text, link in matches:
        if not link.startswith('http') and not link.startswith('#'):
            links.append((text, link))
    
    return links

def get_parent_name(directory):
    """Get a readable parent name from directory path."""
    parent_map = {
        'symbolic-ai': 'Symbolic AI',
        'data-science': 'Data Science',
        'machine-learning': 'Machine Learning',
        'deep-learning': 'Deep Learning',
        'mlops': 'MLOps',
        'quantum-computing': 'Quantum Computing',
        'distributed-systems': 'Distributed Systems'
    }
    
    dir_name = Path(directory).name
    return parent_map.get(dir_name, dir_name.replace('-', ' ').title())

def create_placeholder_file(file_path, title, parent_name):
    """Create a placeholder markdown file."""
    # Create directory if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Generate content
    content = PLACEHOLDER_TEMPLATE.format(
        title=title,
        parent=parent_name
    )
    
    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {file_path}")

def process_directory(directory):
    """Process all README files in a directory and create missing linked files."""
    readme_path = directory / 'README.md'
    
    if not readme_path.exists():
        return
    
    print(f"\nProcessing: {readme_path}")
    
    # Extract links
    links = extract_links_from_file(readme_path)
    
    # Get parent name for back links
    parent_name = get_parent_name(directory)
    
    # Check each link and create if missing
    created_count = 0
    for text, link in links:
        # Resolve the full path
        target_path = (directory / link).resolve()
        
        # Skip if file already exists
        if target_path.exists():
            continue
        
        # Create placeholder
        create_placeholder_file(target_path, text, parent_name)
        created_count += 1
    
    print(f"Created {created_count} placeholder files in {directory.name}")

def main():
    """Main function to process all directories."""
    print("Creating placeholder files for broken links...")
    print("=" * 60)
    
    # List of directories to process
    directories = [
        REPO_ROOT / 'symbolic-ai',
        REPO_ROOT / 'data-science',
        REPO_ROOT / 'machine-learning',
        REPO_ROOT / 'deep-learning',
        REPO_ROOT / 'mlops',
        REPO_ROOT / 'quantum-computing',
        REPO_ROOT / 'distributed-systems'
    ]
    
    total_created = 0
    for directory in directories:
        if directory.exists():
            process_directory(directory)
    
    print("\n" + "=" * 60)
    print("Placeholder file creation complete!")
    print("\nNote: These are placeholder files. Please update them with actual content.")

if __name__ == '__main__':
    main()

# Made with Bob
