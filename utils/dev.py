from asyncio import Queue, create_task
import json


class DatabaseManager:
    filename = 'db.json'

    @classmethod
    async def _read_db(cls):
        async with open(cls.filename, 'r') as json_db:
            return json.load(json_db)

    @classmethod
    async def _write_db(cls, content: dict):
        async with open(cls.filename, 'w') as json_db:
            json.dump(content, json_db, indent=4)

    @classmethod
    async def _reset_db(cls):
        """Resets the values in cache to None"""
        cache = await cls._read_db()
        for key in cache:
            cache[key] = None
        await cls._write_db(content=cache)

    @classmethod
    async def _update_data(cls, key: str, value: list):
        """Saves data to cache"""
        cache = await cls._read_db()
        cache[key] = value
        await cls._write_db(content=cache)

    @classmethod
    async def _find_data(cls, giveaway_identifier: str) -> None | list:
        cache = await cls._read_db()
        return cache.get(giveaway_identifier)


class AsyncDatabase(DatabaseManager):
    queue = Queue()

    # don't need to be in queue
    @classmethod
    async def read_db(cls):
        async with open(cls.filename, 'r') as json_db:
            return json.load(json_db)

    @classmethod
    async def find_data(cls, giveaway_identifier: str) -> None | list:
        cache = await cls.read_db()
        return cache.get(giveaway_identifier)

    @classmethod
    async def write_db(cls, content: dict):
        await cls.queue.put(('write', content))

    @classmethod
    async def reset_db(cls):
        await cls.queue.put(('reset', None))

    @classmethod
    async def update_data(cls, key: str, value: list):
        await cls.queue.put(('update', (key, value)))

