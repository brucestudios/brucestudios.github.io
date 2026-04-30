#!/usr/bin/env python3
"""
Task CLI - A simple command-line task manager.
"""

import argparse
import json
import os
import sys
from pathlib import Path

DEFAULT_TASK_FILE = Path.home() / '.task_cli_tasks.json'


def load_tasks(file_path):
    """Load tasks from the JSON file."""
    if file_path.exists():
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks, file_path):
    """Save tasks to the JSON file."""
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=2)


def add_task(description, file_path):
    """Add a new task."""
    tasks = load_tasks(file_path)
    tasks.append({
        'id': len(tasks) + 1,
        'description': description,
        'done': False
    })
    save_tasks(tasks, file_path)
    print(f'Added task: "{description}"')


def list_tasks(file_path):
    """List all tasks."""
    tasks = load_tasks(file_path)
    if not tasks:
        print('No tasks found.')
        return

    for task in tasks:
        status = '✓' if task['done'] else ' '
        print(f'[{status}] {task["id"]}: {task["description"]}')


def done_task(task_id, file_path):
    """Mark a task as done."""
    tasks = load_tasks(file_path)
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks, file_path)
            print(f'Marked task {task_id} as done.')
            return
    print(f'Task {task_id} not found.')


def remove_task(task_id, file_path):
    """Remove a task."""
    tasks = load_tasks(file_path)
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print(f'Task {task_id} not found.')
        return
    # Reassign IDs
    for i, task in enumerate(new_tasks, start=1):
        task['id'] = i
    save_tasks(new_tasks, file_path)
    print(f'Removed task {task_id}.')


def main():
    parser = argparse.ArgumentParser(description='A simple command-line task manager.')
    parser.add_argument('--file', type=Path, default=DEFAULT_TASK_FILE,
                        help=f'Path to the task file (default: {DEFAULT_TASK_FILE})')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Task description')

    # List command
    subparsers.add_parser('list', help='List all tasks')

    # Done command
    parser_done = subparsers.add_parser('done', help='Mark a task as done')
    parser_done.add_argument('task_id', type=int, help='Task ID to mark as done')

    # Remove command
    parser_remove = subparsers.add_parser('remove', help='Remove a task')
    parser_remove.add_argument('task_id', type=int, help='Task ID to remove')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description, args.file)
    elif args.command == 'list':
        list_tasks(args.file)
    elif args.command == 'done':
        done_task(args.task_id, args.file)
    elif args.command == 'remove':
        remove_task(args.task_id, args.file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()