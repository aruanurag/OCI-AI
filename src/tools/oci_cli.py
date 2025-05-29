import subprocess
from llama_index.core.tools import FunctionTool

def run_oci_cli(command: str) -> str:
    """
    Runs an OCI CLI command and returns the output.
    Example: 'oci os ns get'
    """
    try:
        cmd_list = command.strip().split()
        if cmd_list[0] != "oci":
            return "Only 'oci' commands are allowed."
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
    description="Runs an OCI CLI command and returns the output. Usage: oci_cli(command: str)"
) 