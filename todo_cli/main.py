#!/usr/bin/env python3
"""
Todo CLI - A simple command-line interface for managing your todo list.
"""

import argparse
import json
import os
import sys
from typing import List, Dict

TODO_FILE = os.path.join(os.path.expanduser("~"), ".todo_list.json")


def load_todos() -> List[Dict]:
    """Load todos from the JSON file."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_todos(todos: List[Dict]) -> None:
    """Save todos to the JSON file."""
    try:
        with open(TODO_FILE, 'w') as f:
            json.dump(todos, f, indent=2)
    except IOError as e:
        print(f"Error saving todos: {e}", file=sys.stderr)
        sys.exit(1)


def add_todo(description: str) -> None:
    """Add a new todo."""
    todos = load_todos()
    todos.append({
        "id": len(todos) + 1,
        "description": description,
        "completed": False
    })
    save_todos(todos)
    print(f'Added: "{description}"')


def list_todos() -> None:
    """List all todos."""
    todos = load_todos()
    if not todos:
        print("No todos found.")
        return

    for todo in todos:
        status = "✓" if todo["completed"] else " "
        print(f"{todo['id']}. [{status}] {todo['description']}")


def complete_todo(todo_id: int) -> None:
    """Mark a todo as complete."""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            save_todos(todos)
            print(f'Completed: "{todo["description"]}"')
            return
    print(f"Todo with id {todo_id} not found.", file=sys.stderr)
    sys.exit(1)


def delete_todo(todo_id: int) -> None:
    """Delete a todo."""
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            removed = todos.pop(i)
            # Reassign IDs
            for j, t in enumerate(todos[i:], start=i):
                t["id"] = j + 1
            save_todos(todos)
            print(f'Deleted: "{removed["description"]}"')
            return
    print(f"Todo with id {todo_id} not found.", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="A simple todo list CLI.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("description", nargs="+", help="Description of the todo")
    add_parser.set_defaults(func=lambda args: add_todo(" ".join(args.description)))

    # List command
    list_parser = subparsers.add_parser("list", help="List all todos")
    list_parser.set_defaults(func=lambda args: list_todos())

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
    complete_parser.add_argument("id", type=int, help="ID of the todo to complete")
    complete_parser.set_defaults(func=lambda args: complete_todo(args.id))

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument("id", type=int, help="ID of the todo to delete")
    delete_parser.set_defaults(func=lambda args: delete_todo(args.id))

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()