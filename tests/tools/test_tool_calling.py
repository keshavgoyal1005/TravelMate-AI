from app.llm.client import tool_llm
from app.tools.travel_tools import calculate_trip_budget
from langchain_core.messages import ToolMessage


def test_complete_tool_calling_flow():
    user_message = (
        "My trip budget is 30000 rupees and I want to spend "
        "5000 rupees on shopping. Calculate my total budget."
    )

    # Step 1: Ask the LLM
    response = tool_llm.invoke(user_message)

    assert response.tool_calls

    print("\nLLM TOOL CALL:")
    print(response.tool_calls)

    # Step 2: Extract the tool call
    tool_call = response.tool_calls[0]

    # Step 3: Execute the requested tool
    tool_result = calculate_trip_budget.invoke(
        tool_call["args"]
    )

    print("\nTOOL RESULT:")
    print(tool_result)

    assert tool_result == 35000

    # Step 4: Create a message containing the tool result
    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"],
    )

    # Step 5: Send the original LLM request,
    # the tool call, and the tool result back to the LLM
    final_response = tool_llm.invoke(
        [
            {
                "role": "user",
                "content": user_message,
            },
            response,
            tool_message,
        ]
    )

    print("\nFINAL RESPONSE:")
    print(final_response.content)

    assert final_response.content