"""
Skill Manager for OpenClaw
"""
import os
import json
from pathlib import Path

class SkillManager:
    def __init__(self, skills_dir=None):
        if skills_dir is None:
            # Default to the OpenClaw skills directory
            self.skills_dir = Path.home() / ".openclaw" / "skills"
        else:
            self.skills_dir = Path(skills_dir)
    
    def list_skills(self):
        """List all available skills."""
        if not self.skills_dir.exists():
            return []
        skills = []
        for item in self.skills_dir.iterdir():
            if item.is_dir() and (item / "SKILL.md").exists():
                skills.append(item.name)
        return skills
    
    def get_skill_info(self, skill_name):
        """Get information about a specific skill."""
        skill_path = self.skills_dir / skill_name
        if not skill_path.exists():
            return None
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            return None
        return skill_md.read_text(encoding="utf-8")