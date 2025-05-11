import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool(
    name="get-word",
    description="Get the definitin of a word and other information amount the word in a JSON format",
)
async def get_word(word: str) -> dict:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    headers = {"accept": "application/json"}
    response = requests.get(url=url, headers=headers, timeout=10.0)

    try:
        response.raise_for_status()
        response_json = response.json()
        word_json = response_json[0]
        return word_json

    except Exception as e:
        return {"exception": e, "response_text": response.text}


if __name__ == "__main__":
    mcp.run(transport="stdio")
