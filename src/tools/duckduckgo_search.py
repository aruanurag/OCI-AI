from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec

tool_spec = DuckDuckGoSearchToolSpec()
duckduckgo_tool = tool_spec.to_tool_list()
