from langchain_core.tools import BaseTool


def execute_tool_safely(
    tool: BaseTool,
    arguments: dict,
):
    try:
        return tool.invoke(arguments)

    except Exception as exc:
        return f"Tool execution failed: {exc}"