#!/usr/bin/env python3
"""
List OpenClaw skills with their descriptions.
"""

import os
import sys

def get_skill_description(skill_path):
    """Extract description from SKILL.md file."""
    skill_md = os.path.join(skill_path, 'SKILL.md')
    if not os.path.isfile(skill_md):
        return "No SKILL.md found"
    
    try:
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for description in YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                for line in frontmatter.split('\n'):
                    if line.strip().startswith('description:'):
                        desc = line.split(':', 1)[1].strip()
                        # Remove quotes
                        if desc.startswith('"') and desc.endswith('"'):
                            desc = desc[1:-1]
                        elif desc.startswith("'") and desc.endswith("'"):
                            desc = desc[1:-1]
                        return desc
        
        # Fallback: first non-empty line after headers
        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                # Take first reasonable line
                if len(stripped) > 10 and not stripped.startswith('```'):
                    return stripped[:100] + ('...' if len(stripped) > 100 else '')
    except Exception as e:
        return f"Error reading SKILL.md: {e}"
    
    return "No description found"

def main():
    # Default OpenClaw skills directory
    skills_dir = '/usr/lib/node_modules/openclaw/skills'
    
    # Allow override via environment variable
    if 'OPENCLAW_SKILLS_DIR' in os.environ:
        skills_dir = os.environ['OPENCLAW_SKILLS_DIR']
    
    if not os.path.isdir(skills_dir):
        print(f"Error: Skills directory not found: {skills_dir}", file=sys.stderr)
        print("Set OPENCLAW_SKILLS_DIR environment variable to override.", file=sys.stderr)
        sys.exit(1)
    
    # Get skill directories
    try:
        skill_names = [name for name in os.listdir(skills_dir) 
                      if os.path.isdir(os.path.join(skills_dir, name))]
        skill_names.sort()
    except PermissionError:
        print(f"Error: Permission denied accessing {skills_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Print header
    print(f"{'Skill Name':<30} Description")
    print("-" * 80)
    
    # Print each skill
    for name in skill_names:
        skill_path = os.path.join(skills_dir, name)
        description = get_skill_description(skill_path)
        print(f"{name:<30} {description}")

if __name__ == '__main__':
    main()