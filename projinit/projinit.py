#!/usr/bin/env python3
"""
ProjInit - A simple project initializer for Python projects.

Usage:
    projinit [options] <project_name>

Options:
    --license LICENSE   Specify license (default: MIT)
    --author AUTHOR     Specify author name
    --email EMAIL       Specify author email
    --version VERSION   Specify version (default: 0.1.0)
    --help              Show this help message
"""

import argparse
import os
import sys
import shutil
from pathlib import Path

def create_directory_structure(project_name):
    """Create the basic directory structure for a Python project."""
    dirs = [
        project_name,
        f"{project_name}/src",
        f"{project_name}/tests",
        f"{project_name}/docs",
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)

def create_file(filepath, content):
    """Create a file with the given content."""
    with open(filepath, 'w') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Initialize a new Python project.')
    parser.add_argument('project_name', help='Name of the project to create')
    parser.add_argument('--license', default='MIT', help='License type (default: MIT)')
    parser.add_argument('--author', help='Author name')
    parser.add_argument('--email', help='Author email')
    parser.add_argument('--version', default='0.1.0', help='Version (default: 0.1.0)')
    args = parser.parse_args()

    project_name = args.project_name

    # Check if project directory already exists
    if os.path.exists(project_name):
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)

    # Create directory structure
    create_directory_structure(project_name)

    # Create README.md
    readme_content = f"""# {project_name}

A brief description of the project.

## Installation

\`\`\`bash
pip install {project_name}
\`\`\`

## Usage

\`\`\`python
import {project_name}

# Your code here
\`\`\`

## License

This project is licensed under the {args.license} License - see the [LICENSE](LICENSE) file for details.
"""
    create_file(f"{project_name}/README.md", readme_content)

    # Create LICENSE file (simplified MIT)
    license_content = f"""MIT License

Copyright (c) {args.author or 'Your Name'} {args.email and f'<{args.email}>' or ''}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    create_file(f"{project_name}/LICENSE", license_content)

    # Create .gitignore
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a manifest
#  after PyInstaller has extracted the executable from an archive
#  and then they are not regenerated with every invocation of the program:
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
"""
    create_file(f"{project_name}/.gitignore", gitignore_content)

    # Create pyproject.toml
    pyproject_content = f"""[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "{args.version}"
description = "A Python package created with ProjInit"
readme = "README.md"
requires-python = ">=3.8"
license = "{args.license}"
authors = [
    {{name = "{args.author or 'Your Name'}", email = "{args.email or ''}"}}
]
keywords = []
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/{project_name}"

[tool.setuptools.packages.find]
where = ["src"]
"""
    create_file(f"{project_name}/pyproject.toml", pyproject_content)

    # Create a simple Python package structure
    init_src = f"{project_name}/src/{project_name}"
    Path(init_src).mkdir(parents=True, exist_ok=True)
    create_file(f"{init_src}/__init__.py", f'"""Top-level package for {project_name}."""\n\n__author__ = "{args.author or \"Your Name\"}"\n__email__ = "{args.email or \"\"}"\n__version__ = "{args.version}"\n')

    # Create a basic test
    tests_dir = f"{project_name}/tests"
    Path(tests_dir).mkdir(parents=True, exist_ok=True)
    create_file(f"{tests_dir}/test_{project_name}.py", f"""import unittest
from {project_name} import __version__

class Test{project_name.capitalize()}(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "{args.version}")

if __name__ == '__main__':
    unittest.main()
""")

    print(f"Project '{project_name}' created successfully!")
    print(f"To get started:")
    print(f"  cd {project_name}")
    print(f"  pip install -e .")
    print(f"  pytest")

if __name__ == '__main__':
    main()