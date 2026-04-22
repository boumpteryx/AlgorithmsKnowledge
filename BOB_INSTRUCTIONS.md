# Bob's Instructions for AlgorithmsKnowledge Repository

## Repository Purpose
This repository serves as a personal knowledge base and mental map for algorithms, with a focus on AI and related fields. It's structured as a hierarchical wiki with multiple layers of detail.

## Structure Rules

### 1. File Organization
- **Root README.md**: High-level overview and navigation to main topics
- **Topic Folders**: Each major topic has its own folder (e.g., `symbolic-ai/`, `machine-learning/`)
- **Sub-folders**: Topics can have nested sub-folders for sub-topics
- **README files**: Each folder contains a `README.md` that serves as a mental map/overview for that topic
- **Detail Pages**: Individual markdown files for specific concepts within each topic

### 2. Diagram Management
**CRITICAL RULE**: Never embed Mermaid code directly in markdown files.

- Each topic folder contains a `diagrams/` subfolder
- Store `.mmd` (Mermaid source) files in `diagrams/`
- Store rendered `.png` files in `diagrams/`
- Reference diagrams in markdown using: `![Diagram Description](diagrams/diagram-name.png)`
- Naming convention: Use kebab-case for diagram files (e.g., `neural-network-architecture.mmd`)

### 3. Content Guidelines
- Use clear, hierarchical structure with proper heading levels
- Include cross-references between related topics
- Keep README files concise - they're mental maps, not detailed explanations
- Detail pages should be comprehensive but focused on a single concept
- Use consistent formatting and terminology across the repository

### 4. Visual Styling for Resources
**IMPORTANT**: All learning resources (books, courses, tools, platforms, online resources) should be styled in **green** to make them easily identifiable.

In markdown files, wrap resource sections with HTML styling:
```html
<div style="color: green;">

### Books
- "Book Title" by Author
- "Another Book" by Author

### Courses
- Course Name (Platform)
- Another Course

</div>
```

This applies to sections like:
- Books
- Courses
- Online Resources
- Tools and Technologies
- Platforms
- Further Learning
- Research Resources

### 4. Navigation
- Main README should link to all major topic areas
- Each topic README should link to its sub-topics and detail pages
- Include "back to parent" links for easy navigation
- Consider adding a breadcrumb trail in sub-topic pages

### 5. Maintenance
- Keep this instruction file updated as the structure evolves
- Maintain consistency in folder naming (use kebab-case)
- Update cross-references when adding new content
- Periodically review and update outdated information

## Current Topic Areas
1. Symbolic AI
2. Data Science
3. Machine Learning (ML)
4. Deep Learning
5. MLOps
6. Quantum Computing
7. Distributed Systems

## Workflow for Adding New Content
1. Identify the appropriate topic folder
2. Create or update the relevant README for context
3. Create detail markdown files as needed
4. If diagrams are needed:
   - Create `.mmd` file in `diagrams/` folder
   - Generate `.png` from the `.mmd` file
   - Reference the `.png` in the markdown
5. Update parent README files with links to new content
6. Update main README if adding a new major topic