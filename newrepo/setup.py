from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file-organizer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Organize files in a directory by their extensions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/file-organizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'file-organizer=file_organizer.__main__:main',
        ],
    },
)