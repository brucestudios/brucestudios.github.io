# Task CLI

A simple command-line task manager written in Python.

## Features

- Add tasks with descriptions
- List all tasks with completion status
- Mark tasks as done
- Remove tasks
- Persistent storage using a JSON file in your home directory

## Installation

You can install the package using pip:

```bash
pip install task-cli
```

Or clone the repository and install locally:

```bash
git clone https://github.com/yourusername/task-cli.git
cd task-cli
pip install -e .
```

## Usage

After installation, you can use the `task-cli` command:

### Add a task

```bash
task-cli add "Buy groceries"
```

### List tasks

```bash
task-cli list
```

### Mark a task as done

```bash
task-cli done 1
```

### Remove a task

```bash
task-cli remove 1
```

## Configuration

By default, the task file is stored at `~/.task_cli_tasks.json`. You can specify a different file using the `--file` option:

```bash
task-cli --file /path/to/my/tasks.json list
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.