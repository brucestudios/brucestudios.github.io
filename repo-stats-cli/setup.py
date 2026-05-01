from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="repo-stats-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to fetch GitHub repository statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/repo-stats-cli-20260428",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "repo-stats=repo_stats_cli.cli:main",
        ],
    },
)