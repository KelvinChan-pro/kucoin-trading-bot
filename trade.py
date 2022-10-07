from ast import Or
from datetime import datetime
from time import sleep
import threading
import os

import asyncio
from kucoin_futures.client import WsToken
from kucoin_futures.ws_client import KucoinFuturesWsClient


from constants import KU_KEY, KU_PASS, KU_SECRET, SYMBOL, ORDERSIZE, THREADCYCLINGTIME,TRADINGACCOUNTID, AMOUNT, EPS, LIMITHOLDS
import threading
import asyncio

api_key = KU_KEY
api_secret = KU_SECRET
api_passphrase = KU_PASS

async def main():
    global loop
    async def deal_msg(msg):
        if msg['topic'] == '/contractMarket/tickerV2:XBTUSDM':
            print(f'Get XBTUSDM Ticker price:{msg["data"]}')
        elif msg['topic'] == '/contractMarket/level3:XBTUSDTM':
            print(f'Get XBTUSDTM level3:{msg["data"]}')

    # is public
    # client = WsToken()
    # is private
    client = WsToken(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KucoinFuturesWsClient.create(loop, client, deal_msg, private=False)
    await ws_client.subscribe('/contractMarket/level3:XBTUSDTM')
    while True:
        await asyncio.sleep(60, result=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
