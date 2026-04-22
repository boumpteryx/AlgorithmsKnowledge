# Symbolic AI Diagrams

This folder contains Mermaid diagram source files (.mmd) and their rendered PNG versions.

## Diagram Files

- `expert-system-architecture.mmd` / `.png` - Architecture of expert systems
- `reasoning-architecture.mmd` / `.png` - General reasoning engine architecture

## Rendering Diagrams

To render Mermaid diagrams to PNG:

1. **Using Mermaid CLI**:
   ```bash
   npm install -g @mermaid-js/mermaid-cli
   mmdc -i diagram-name.mmd -o diagram-name.png
   ```

2. **Using Online Editor**:
   - Visit https://mermaid.live/
   - Paste .mmd content
   - Export as PNG

3. **Using VS Code Extension**:
   - Install "Markdown Preview Mermaid Support"
   - Open .mmd file
   - Right-click preview → Export to PNG

## Note

PNG files should be committed to the repository so they can be referenced in markdown files. The .mmd source files are kept for future editing.