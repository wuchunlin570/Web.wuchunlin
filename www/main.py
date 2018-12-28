import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time, SQLUitl
from datetime import datetime
from aiohttp import web

async def index(request):
    return web.Response(body='<h1>你好世界</h1>')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'0.0.0.0',80)
    logging.info('服务器 启动 http://0.0.0.0:80...')
    return srv
user = User(id=10000,name='伍春林')
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()