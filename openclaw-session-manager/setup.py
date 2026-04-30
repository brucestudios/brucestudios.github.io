from setuptools import setup, find_packages

setup(
    name="openclaw-session-manager",
    version="0.1.0",
    author="brucestudios",
    author_email="bruce@example.com",
    description="Utility to manage OpenClaw sessions and subagents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/openclaw-session-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'oc-session=openclaw_session_manager.cli:main',
        ],
    },
)