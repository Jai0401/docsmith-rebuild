"""MiniMax API client — replaces OpenRouter for docSmith."""
import os

MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
MINIMAX_BASE_URL = "https://api.minimax.io/v1"
MODEL = "MiniMax-M2.7"

_lc_llm = None


def get_llm():
    """Get or create the langchain-openai LLM instance pointed at MiniMax."""
    global _lc_llm
    if _lc_llm is None:
        from langchain_openai import ChatOpenAI
        _lc_llm = ChatOpenAI(
            model=MODEL,
            api_key=MINIMAX_API_KEY,
            base_url=MINIMAX_BASE_URL,
            temperature=0.1,
            max_tokens=131072,
        )
    return _lc_llm