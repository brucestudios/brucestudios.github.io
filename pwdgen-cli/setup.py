from setuptools import setup, find_packages

setup(
    name="pwdgen-cli",
    version="0.1.0",
    author="brucestudios",
    author_email="bruce@example.com",
    description="A simple command-line password generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/pwdgen-cli",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pwdgen=pwdgen.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)