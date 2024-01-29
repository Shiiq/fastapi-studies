import asyncio

from redis.asyncio.client import Redis

r = Redis(host="localhost", port=6379)

data_st = [f"{i}_data" for i in range(1, 21)]


async def run_set():
    # res1 = await r.sadd("bikes:racing:france", "bike:123")
    # print(res1)
    # res2 = await r.sadd("bikes:racing:france", "bike:2", "bike:3")
    # print(res2)
    # await r.srem("bikes:racing:france", "bike:4", "bike:5", "bike:6")
    # res3 = await r.sadd("bikes:racing:france", "bike:4", "bike:5", "bike:6")
    # print(res3)
    # items = await r.smembers("bikes:racing:france")
    # print(items)
    # ia = await r.smembers("bikes:racing")
    # print(ia)
    pass


async def run_list():
    # ins = await r.rpush("movie:comedyactionadventureanimationchildren20062007", *data_st)
    # await r.rpush("data:movies:1", *data_st)
    # await r.rpush("data:movies:2", *data_st)
    print(await r.llen("data:movies:1"))
    print(await r.llen("data:movies"))
    print(await r.llen("data"))
    # res1 = await r.lrange("data:list", 0, 4)
    # print(res1)
    # await r.ltrim("data:list", 1, 0)
    # await r.ltrim("movie:comedyactionadventureanimationchildren20062007", 1, 0)
    # res2 = await r.lrange("data:list", 5, 9)
    # print(res2)
    # res3 = await r.lrange("data:list", 5, 9)
    # print(res3)
    # res4 = await r.lrange("data:list", 5, 9)
    # print(res4)
    # ex = await r.llen("data:list")
    # print(ex)
    # xe = await r.llen("movie:comedyactionadventureanimationchildren20062007")
    # print(xe)
    x = await r.exists("data:movies:1", "data:movies:2")
    print(x, type(x))

asyncio.run(run_list())
