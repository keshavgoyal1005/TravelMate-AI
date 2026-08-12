from app.llm.client import llm


def test_llm_connection():
    response = llm.invoke("Say hello in one sentence.")

    assert response.content
    print(response.content)