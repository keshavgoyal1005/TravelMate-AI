from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter


load_dotenv()


def get_llm():
    return ChatOpenRouter(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        temperature=0,
    )