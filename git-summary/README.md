# git-summary

A command-line tool to summarize GitHub repositories.

## Features

- Fetches repository information from the GitHub API
- Displays key metrics: description, language, stars, forks, watchers, open issues, license, creation/update dates
- Supports authentication via personal access token for higher rate limits
- Simple and easy to use

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/brucestudios/git-summary.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Make the script executable and add to your PATH:
   ```bash
   chmod +x main.py
   sudo ln -s $(pwd)/main.py /usr/local/bin/git-summary
   ```

## Usage

```bash
git-summary <github_repository_url> [--token YOUR_GITHUB_TOKEN]
```

Example:
```bash
git-summary https://github.com/tiangolo/fastapi
```

Output:
```
Repository: tiangolo/fastapi
Description: FastAPI framework, high performance, easy to learn, fast to code, ready for production
Language: Python
Stars: 52,341
Forks: 3,612
Watchers: 815
Open Issues: 89
License: MIT
Created: 2018-07-12
Updated: 2023-10-05
URL: https://github.com/tiangolo/fastapi
```

## Configuration

You can set your GitHub token as an environment variable `GITHUB_TOKEN` or pass it via the `--token` argument.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.