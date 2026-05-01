import argparse
import sys
from . import __version__

def main():
    parser = argparse.ArgumentParser(
        description="OpenClaw Session Manager - Manage OpenClaw sessions and subagents"
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("list", help="List active sessions")
    list_parser.add_argument(
        "--limit", type=int, default=10, help="Maximum number of sessions to show"
    )

    # Spawn command
    spawn_parser = subparsers.add_parser(
        "spawn", help="Spawn a new subagent or ACP session"
    )
    spawn_parser.add_argument(
        "task", type=str, help="Task description for the new session"
    )
    spawn_parser.add_argument(
        "--label", type=str, help="Label for the session"
    )
    spawn_parser.add_argument(
        "--runtime",
        type=str,
        choices=["subagent", "acp"],
        default="subagent",
        help="Runtime type (default: subagent)",
    )
    spawn_parser.add_argument(
        "--agent-id", type=str, help="Agent ID for ACP runtime"
    )
    spawn_parser.add_argument(
        "--model", type=str, help="Model to use for the session"
    )
    spawn_parser.add_argument(
        "--thinking",
        type=str,
        choices=["low", "medium", "high"],
        help="Thinking level for the session",
    )
    spawn_parser.add_argument(
        "--thread", action="store_true", help="Create as a thread-bound session"
    )
    spawn_parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout in seconds for the session",
    )

    # Send command
    send_parser = subparsers.add_parser(
        "send", help="Send a message to an existing session"
    )
    send_parser.add_argument(
        "session_key", type=str, help="Session key or label"
    )
    send_parser.add_argument(
        "message", type=str, help="Message to send"
    )

    # History command
    history_parser = subparsers.add_parser(
        "history", help="Get history for a session"
    )
    history_parser.add_argument(
        "session_key", type=str, help="Session key or label"
    )
    history_parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of messages to retrieve",
    )
    history_parser.add_argument(
        "--include-tools",
        action="store_true",
        help="Include tool messages in history",
    )

    # Status command
    status_parser = subparsers.add_parser(
        "status", help="Get status for a session"
    )
    status_parser.add_argument(
        "session_key", type=str, help="Session key or label"
    )

    args = parser.parse_args()

    if args.command == "list":
        list_sessions(args)
    elif args.command == "spawn":
        spawn_session(args)
    elif args.command == "send":
        send_message(args)
    elif args.command == "history":
        get_history(args)
    elif args.command == "status":
        get_status(args)
    else:
        parser.print_help()
        sys.exit(1)

def list_sessions(args):
    """List active sessions."""
    # In a real implementation, we would call the sessions_list tool
    # For now, we'll just print a placeholder
    print("Listing sessions (placeholder implementation)")
    print("In a real implementation, this would call the OpenClaw sessions_list tool")

def spawn_session(args):
    """Spawn a new session."""
    # In a real implementation, we would call the sessions_spawn tool
    print(f"Spawning session: {args.task}")
    print(f"  Runtime: {args.runtime}")
    print(f"  Label: {args.label}")
    print(f"  Agent ID: {args.agent_id}")
    print(f"  Model: {args.model}")
    print(f"  Thinking: {args.thinking}")
    print(f"  Thread: {args.thread}")
    print(f"  Timeout: {args.timeout}")
    print("(This is a placeholder - actual implementation would use sessions_spawn tool)")

def send_message(args):
    """Send a message to a session."""
    print(f"Sending message to session {args.session_key}: {args.message}")
    print("(This is a placeholder - actual implementation would use sessions_send tool)")

def get_history(args):
    """Get history for a session."""
    print(f"Getting history for session {args.session_key} (limit: {args.limit})")
    print(f"Include tools: {args.include_tools}")
    print("(This is a placeholder - actual implementation would use sessions_history tool)")

def get_status(args):
    """Get status for a session."""
    print(f"Getting status for session {args.session_key}")
    print("(This is a placeholder - actual implementation would use session_status tool)")

if __name__ == "__main__":
    main()