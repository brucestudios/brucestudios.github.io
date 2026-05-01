from setuptools import setup, find_packages

setup(
    name="openclaw-utils-1777473142",
    version="0.1.0",
    author="OpenClaw Assistant",
    author_email="assistant@openclaw.example",
    description="A simple Python utility package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/{GITHUB_REPOSITORY}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
    python_requires=">=3.6",
)
