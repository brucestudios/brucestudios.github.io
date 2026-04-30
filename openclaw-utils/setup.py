from setuptools import setup, find_packages

setup(
    name="openclaw-toolkit",
    version="0.1.0",
    description="Toolkit for OpenClaw agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="brucestudios",
    url="https://github.com/brucestudios/openclaw-toolkit",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "oc-memory-summary=oc_utils.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)