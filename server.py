import time

from constants import quran_details, available_languages
from mcp.server.fastmcp import FastMCP
import httpx
import json

# Initialize FastMCP server
mcp = FastMCP("Search-Quran")

# Constants
QURAN_API_BASE = "http://api.alquran.cloud/v1"


@mcp.tool()
async def surah_info(surah_number: int) -> str:
    f"""Retrieve details about a specific Surah (سورة) (Name in Arabic and English, Number of verses, Revelation type).
    according to this mapping:
    {quran_details}
    
    Always return the islamic information as it's without any rephrasing.
    Args:
        surah_number: The number of the Surah to retrieve from 1 to 114.
    """
    if 1 > surah_number > 114:
        return "Invalid Surah number please select number between 1 to 114 only"

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{QURAN_API_BASE}/surah")

        if response.status_code != 200:
            return "API error cannot get the answer right now"

        data = response.json()["data"]

        surah_obj = data[surah_number-1]

        answer = "\n".join([
            f"Name in Arabic: {surah_obj["name"]}",
            f"Name in English: {surah_obj["englishName"]}",
            f"Name translated into English: {surah_obj["englishNameTranslation"]}",
            f"Number of verses {{Ayat}}: {surah_obj["numberOfAyahs"]}",
            f"Revelation type: {surah_obj["revelationType"]}",
            "-------------------------------"
        ])
        return answer


@mcp.tool()
async def get_verses(surah_number: int, from_ayah: int, to_ayah: int) -> str:
    f"""Retrieve verses from specific Surah (سورة) in Arabic only.
    according to this mapping:
    {quran_details}
    
    Always return the islamic information as it's without any rephrasing.
    Args:
        surah_number: The number of the Surah to retrieve from 1 to 114.
        from_ayah: The number of the first verse to retrieve.
        to_ayah: The number of the last verse to retrieve.
    """
    if 1 > surah_number > 114:
        return "Invalid Surah number please select number between 1 to 114 only"

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{QURAN_API_BASE}/surah/{surah_number}?offset={from_ayah-1}&limit={to_ayah-from_ayah+1}")

        if response.status_code != 200:
            return "API error cannot get the answer right now"

        data = response.json()["data"]

        return json.dumps(data, ensure_ascii=False, indent=4)


@mcp.tool()
async def search_quran(text_to_search_with: str, language: available_languages = "ar", top_k: int = 5) -> str:
    f"""Search in the Quran for any verse (آية) contains these text.
        Always return the islamic information as it's without any rephrasing.
    Args:
        text_to_search_with: The number of the Surah to retrieve from 1 to 114.
        language: two character key for the language that you want to search in for example (ar for Arabic, en for English).
        top_k: the number of most relevant answer to return.
    """
    if not text_to_search_with:
        return "No text to search"

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{QURAN_API_BASE}/search/{text_to_search_with}/all/{language}")

        if response.status_code != 200:
            return "API error cannot get the answer right now"

        data = response.json()["data"]["matches"]

        answer = ""
        for match_obj in data[:top_k]:
            answer = "\n".join([
                f"Verse text: {match_obj["text"]}",
                f"Verse number in Surah: {match_obj["numberInSurah"]}",
                f"Surah name in Arabic: {match_obj["surah"]["name"]}",
                f"Surah name in English: {match_obj["surah"]["englishName"]}",
                f"Surah name translated into English: {match_obj["surah"]["englishNameTranslation"]}",
                f"Surah revelation type: {match_obj["surah"]["revelationType"]}",
                "-------------------------------"
            ])
        return answer


if __name__ == "__main__":
    try:
        print("Starting MCP server Search-Quran on 127.0.0.1:8080")
        # Initialize and run the server
        mcp.run(transport='stdio')
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(10)
