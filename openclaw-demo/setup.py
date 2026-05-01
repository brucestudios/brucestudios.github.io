from setuptools import setup, find_packages

setup(
    name="weather-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple command-line tool to get current weather.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/weather-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'weather-cli=weather_cli:main',
        ],
    },
)