from dotenv import load_dotenv
import os

load_dotenv()
ENV = os.environ.get("ENV") or "development"
IS_PROD = True if ENV == "production" else False
KU_KEY = os.environ.get("KU_KEY")
KU_SECRET = os.environ.get("KU_SECRET")
KU_PASS = os.environ.get("KU_PASS")
KU_URL = os.environ.get("KU_URL")
TRADINGACCOUNTID = os.environ.get("TRADINGACCOUNTID")
# Symbols
BTCUSDT = "BTC-USDT"
ETHUSDT = "ETH-USDT"
SHIBBUSD = "SHIBBUSD"
NANOBUSD = "NANOBUSD"
SOLBNB = "SOLBNB"
BTCSTUSD = "BTCSTUSD"
BTCBUSD = "BTCBUSD"
ADABUSD = "ADABUSD"
DARBUSD = "DARBUSD"

ETH3SUSDT = "ETH3S-USDT"
ETH3LUSDT = "ETH3L-USDT"

# Main symbol to use
SYMBOL = ETH3SUSDT

# Trading constants
EPS = 1e-8
AMOUNT = 2.0
ORDERSIZE = 10
LIMITHOLDS = 300.0
THREADCYCLINGTIME = 15.0

