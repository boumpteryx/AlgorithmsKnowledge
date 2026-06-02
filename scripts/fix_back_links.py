import os
from pathlib import Path
import re

def fix_back_links():
    """Fix back navigation links in all detail pages to point to ../README.md"""
    
    # Get all topic directories
    base_dir = Path('.')
    topic_dirs = [d for d in base_dir.iterdir() 
                  if d.is_dir() and not d.name.startswith('.') 
                  and d.name not in ['scripts', 'diagrams']]
    
    total_fixed = 0
    
    for topic_dir in topic_dirs:
        pages_dir = topic_dir / 'pages'
        
        if not pages_dir.exists():
            continue
            
        print(f"\nFixing links in {topic_dir.name}/pages/...")
        
        # Get all markdown files in pages directory
        md_files = list(pages_dir.glob('*.md'))
        
        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                
                # Pattern to match back navigation links
                # Matches: [← Back to <Topic>](README.md)
                pattern = r'\[← Back to ([^\]]+)\]\(README\.md\)'
                
                # Check if pattern exists
                if re.search(pattern, content):
                    # Replace with ../README.md
                    new_content = re.sub(pattern, r'[← Back to \1](../README.md)', content)
                    
                    # Write back
                    md_file.write_text(new_content, encoding='utf-8')
                    total_fixed += 1
                    
            except Exception as e:
                print(f"  Error processing {md_file.name}: {e}")
    
    print(f"\n[OK] Fixed {total_fixed} back navigation links")

if __name__ == '__main__':
    print("=" * 60)
    print("Fixing back navigation links in detail pages...")
    print("=" * 60)
    fix_back_links()
    print("=" * 60)
    print("Back link fixes complete!")
    print("=" * 60)

# Made with Bob
