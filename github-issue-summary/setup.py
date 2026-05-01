from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-issue-summary",
    version="0.1.0",
    author="brucestudios",
    author_email="bruce@example.com",
    description="A CLI tool to generate a markdown summary of GitHub issues grouped by labels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/github-issue-summary",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "PyGithub>=1.55",
    ],
    entry_points={
        "console_scripts": [
            "github-issue-summary=github_issue_summary.cli:main",
        ],
    },
)