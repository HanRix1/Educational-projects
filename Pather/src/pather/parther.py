import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio


# Синхронный вариант кода
# def latest_bulletin_from_auction() -> str:
#     page_url = 'https://spimex.com/markets/oil_products/trades/results/'
#     response = requests.get(page_url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         traiding_results = soup.find('a', class_='accordeon-inner__item-title link xls')
#         file_url = str(traiding_results)[54:111]
#     else:
#         raise requests.exceptions.HTTPError("Неверный url или ошибки на строне сервера")
#     return file_url

# def upload_file(file_url: str, file_resolution: str, file_name: str) -> None:
#     response = requests.get(file_url)
#     if response.status_code == 200:
#         with open(f'{file_name}.{file_resolution}', 'wb') as file:
#             file.write(response.content)
#     else:
#         raise requests.exceptions.HTTPError("Неверный url или ошибки на строне сервера")

async def latest_bulletin_from_auction() -> str:
    page_url = 'https://spimex.com/markets/oil_products/trades/results/'

    async with aiohttp.ClientSession() as session:
        async with session.get(page_url) as resp:
            if resp.status == 200:
                soup = BeautifulSoup(await resp.text(), 'html.parser')
                traiding_results = await asyncio.to_thread(
                    soup.find, 
                    'a', 
                    class_='accordeon-inner__item-title link xls'
                )
                file_url = str(traiding_results)[54:111]
            else:
                raise requests.exceptions.HTTPError("Неверный url или ошибки на строне сервера")
            return file_url
                

async def upload_file(file_url: str, file_resolution: str, file_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status == 200:
                content = await response.read()
                with open(f'{file_name}.{file_resolution}', 'wb') as file:
                    file.write(content)
            else:
                raise aiohttp.ClientResponseError(
                    status=response.status, message="Неверный url или ошибки на стороне сервера"
                )
