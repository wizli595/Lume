from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from django.conf import settings

# Use a function to safely initialize ChatOpenAI
def get_llm():
    return ChatOpenAI(api_key=settings.OPENAI_API_KEY)

def summarize_text(text: str) -> str:
    prompt = ChatPromptTemplate.from_template("Summarize this article in 3 lines:\n\n{text}")
    chain = prompt | get_llm()
    result = chain.invoke({"text": text})
    return result.content if hasattr(result, "content") else str(result)

def translate_text(text: str, target_lang: str = "French") -> str:
    prompt = ChatPromptTemplate.from_template("Translate this article to {target_lang}:\n\n{text}")
    chain = prompt | get_llm()
    result = chain.invoke({"text": text, "target_lang": target_lang})
    return result.content if hasattr(result, "content") else str(result)

def generate_title_and_slug(text: str) -> tuple[str, str]:
    prompt = ChatPromptTemplate.from_template(
        "Generate a catchy title and URL-friendly slug from this content, separated by '|':\n\n{text}"
    )
    chain = prompt | get_llm()
    result = chain.invoke({"text": text})
    response = result.content if hasattr(result, "content") else str(result)

    if "|" in response:
        title, slug = response.split("|")
        return title.strip(), slug.strip()
    return response.strip(), response.strip().lower().replace(" ", "-")
