from setuptools import setup, find_packages

setup(
    name="openclaw-skill-manager",
    version="0.1.0",
    author="brucestudios",
    author_email="brucestudios@example.com",
    description="A utility for managing OpenClaw agent skills",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/openclaw-skill-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'oc-skill=openclaw_skill_manager.cli:main',
        ],
    },
)