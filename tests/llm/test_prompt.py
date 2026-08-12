from app.llm.prompts import travel_prompt


def test_travel_prompt():
    messages = travel_prompt.invoke({"user_request": "What is the capital of France?"})

    print(messages)
    assert len(messages.messages) == 2