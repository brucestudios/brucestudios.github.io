# OpenClaw Session Manager

A utility for managing OpenClaw sessions, subagents, and ACP sessions with easy-to-use CLI commands.

## Features

- List active sessions
- Spawn new subagents or ACP sessions
- Send messages to existing sessions
- Manage session lifecycle
- View session history and status

## Installation

```bash
pip install openclaw-session-manager
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/brucestudios/openclaw-session-manager.git
```

## Usage

### List Sessions

```bash
oc-session list
```

### Spawn a Subagent

```bash
oc-session spawn "Analyze the latest GitHub issues in the repo" --label "issue-analysis"
```

### Spawn an ACP Session

```bash
oc-session spawn "Create a Python script to backup my dotfiles" --runtime acp --agent-id @vscode
```

### Send Message to Session

```bash
oc-session send <session-key> "What's the current status?"
```

### View Session History

```bash
oc-session history <session-key>
```

### Get Session Status

```bash
oc-session status <session-key>
```

## Configuration

The tool automatically uses your existing OpenClaw configuration. No additional setup required.

## Development

```bash
# Install in development mode
pip install -e .

# Run tests
pytest
```

## License

MIT