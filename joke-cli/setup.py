from setuptools import setup, find_packages

setup(
    name="joke-cli",
    version="0.1.0",
    author="brucestudios",
    author_email="you@example.com",
    description="A simple CLI tool to fetch and display a random joke",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/joke-cli",
    packages=find_packages(),
    py_modules=['joke_cli'],
    entry_points={
        'console_scripts': [
            'joke=joke_cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)