from setuptools import setup, find_packages

setup(
    name="awesome-cli",
    version="0.1.0",
    author="brucestudios",
    author_email="bruce@example.com",
    description="A simple CLI that prints a random motivational quote",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/awesome-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'awesome-cli=awesome_cli.__main__:main',
        ],
    },
)