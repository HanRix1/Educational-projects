from asyncio import to_thread
import asyncio
from datetime import datetime
import pandas as pd
from sqlalchemy import select
from db.base import async_session

from pandas.core.frame import DataFrame
from db.models.spimex_trading_results import SpimexTradingResults
from pather.parther import latest_bulletin_from_auction, upload_file

file_resolution = "xlsx"
file_name = "bulletin"

# file_url = "https://spimex.com" + latest_bulletin_from_auction()
# upload_file(file_url, file_resolution, file_name)

def process_bulletin_data(file_name: str, file_resolution: str) -> tuple[DataFrame, datetime]:
    df = pd.read_excel(f'{file_name}.{file_resolution}')
  
    date = df['Форма СЭТ-БТ'].values[2]
    date = datetime.strptime(date.split(":")[1].strip(), '%d.%m.%Y').date()
  
    df['Unnamed: 14'] = pd.to_numeric(df['Unnamed: 14'], errors='coerce')
    df = df[df['Unnamed: 14'].notna()].drop(df.index[-2:])
    df['Unnamed: 14'] = df['Unnamed: 14'].astype('Int64')
    df = df.drop(columns=[
        'Unnamed: 0',
        'Unnamed: 6',
        'Unnamed: 7',
        'Unnamed: 8',
        'Unnamed: 9',
        'Unnamed: 10',
        'Unnamed: 11',
        'Unnamed: 12',
        'Unnamed: 13',
        ])
    return df, date 


async def upload_traiding_results(df: DataFrame, date: datetime) -> None:
    res = []
    for index, row in df.iterrows():
        res.append(
            SpimexTradingResults(
                exchange_product_id=row['Форма СЭТ-БТ'],
                exchange_product_name=row['Unnamed: 2'],
                oil_id=row['Форма СЭТ-БТ'][:4],
                delivery_basis_id=row['Форма СЭТ-БТ'][4:7],
                delivery_basis_name=row['Unnamed: 3'],
                delivery_type_id=row['Форма СЭТ-БТ'][-1],
                volume=int(row['Unnamed: 4']),
                total=int(row['Unnamed: 5']),
                count=int(row['Unnamed: 14']),
                date=date,
            )
        )
    async with async_session() as session:
        session.add_all(res)   
        await session.commit()


async def get_traiding_results():
    async with async_session() as session:
        query = select(SpimexTradingResults)
        result = (await session.scalars(query)).all()
        return result



async def main():
    df, date = await to_thread(process_bulletin_data, file_name, file_resolution)
    data = await get_traiding_results()
    for el in data:
        print(
            el.id,
            el.exchange_product_id,
            el.exchange_product_name,
            el.oil_id,
            el.delivery_basis_id,
            el.delivery_basis_name,
            el.delivery_type_id,
            el.volume,
            el.total,
            el.count,
            el.date,
            sep="\n",
            end="\n\n"
        )
    # await upload_traiding_results(df, date)


if __name__ == "__main__":
    asyncio.run(main())