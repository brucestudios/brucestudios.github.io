from setuptools import setup, find_packages

setup(
    name="secretsmith",
    version="1.0.0",
    author="brucestudios",
    author_email="contact@brucestudios.example",
    description="A Python package for generating secure passwords and passphrases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/secretsmith",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)