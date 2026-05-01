import argparse
import json
import os
import sys

TODO_FILE = os.path.join(os.path.expanduser("~"), ".todo.json")

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_todo(description):
    todos = load_todos()
    todos.append({"description": description, "done": False})
    save_todos(todos)
    print(f'Added: "{description}"')

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos.")
        return
    for i, todo in enumerate(todos, start=1):
        status = "✓" if todo["done"] else " "
        print(f'{i}. [{status}] {todo["description"]}')

def complete_todo(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index-1]["done"] = True
        save_todos(todos)
        print(f'Completed: "{todos[index-1]["description"]}"')
    else:
        print("Invalid index")

def remove_todo(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        removed = todos.pop(index-1)
        save_todos(todos)
        print(f'Removed: "{removed["description"]}"')
    else:
        print("Invalid index")

def main():
    parser = argparse.ArgumentParser(description="A simple CLI todo list.")
    subparsers = parser.add_subparsers(dest="command")

    # add
    parser_add = subparsers.add_parser("add", help="Add a new todo")
    parser_add.add_argument("description", nargs="+", help="Todo description")
    parser_add.set_defaults(func=lambda args: add_todo(" ".join(args.description)))

    # list
    parser_list = subparsers.add_parser("list", help="List todos")
    parser_list.set_defaults(func=lambda args: list_todos())

    # complete
    parser_complete = subparsers.add_parser("complete", help="Mark a todo as complete")
    parser_complete.add_argument("index", type=int, help="Todo index")
    parser_complete.set_defaults(func=lambda args: complete_todo(args.index))

    # remove
    parser_remove = subparsers.add_parser("remove", help="Remove a todo")
    parser_remove.add_argument("index", type=int, help="Todo index")
    parser_remove.set_defaults(func=lambda args: remove_todo(args.index))

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()