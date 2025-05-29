from datetime import datetime
from llama_index.core.tools import FunctionTool

def get_current_date() -> str:
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")

current_date_tool = FunctionTool.from_defaults(
    fn=get_current_date,
    name="get_current_date",
    description="Returns the current date in YYYY-MM-DD format."
) 