# OpenClaw Assistant Tools

A collection of utility functions and scripts to assist OpenClaw agents in their tasks.

## Features

- Skill management utilities
- Common helper functions for OpenClaw development
- Example scripts demonstrating OpenClaw capabilities

## Installation

```bash
pip install openclaw-assistant-tools
```

## Usage

### Skill Management

```python
from openclaw_tools.skill_manager import SkillManager

manager = SkillManager()
manager.list_skills()
```

### Helper Functions

```python
from openclaw_tools.helpers import format_timestamp, sanitize_filename

timestamp = format_timestamp()
safe_name = sanitize_filename("my file: name.txt")
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -am 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.