import subprocess
from llama_index.core.tools import FunctionTool

def run_oci_cli(command: str) -> str:
    """
    Runs a read-only OCI CLI command and returns the output.
    Only allows commands that start with 'oci' and contain safe read actions like 'get', 'list', or 'describe'.
    Example: 'oci os ns get'
    """
    try:
        cmd_list = command.strip().split()
        if cmd_list[0] != "oci":
            return "Only 'oci' commands are allowed."
        # Only allow read-only actions
        allowed_actions = {"get", "list", "describe"}
        if not any(action in cmd_list for action in allowed_actions):
            return "Only read-only commands (get, list, describe) are allowed."
        # Block dangerous actions
        blocked_actions = {"delete", "create", "update", "move", "remove", "set"}
        if any(action in cmd_list for action in blocked_actions):
            return "Modification commands (delete, create, update, move, remove, set) are not allowed."
        result = subprocess.run(cmd_list, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception: {e}"

oci_cli_tool = FunctionTool.from_defaults(
    fn=run_oci_cli,
    name="oci_cli",
    description="Runs a read-only OCI CLI command and returns the output. Only 'get', 'list', or 'describe' actions are allowed. Usage: oci_cli(command: str)"
) 