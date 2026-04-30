from setuptools import setup, find_packages

setup(
    name="openclaw-assistant-tools",
    version="0.1.0",
    author="OpenClaw Assistant",
    author_email="assistant@openclaw.example",
    description="A collection of tools and scripts to assist OpenClaw agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/openclaw-assistant-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)