import dataclasses
from typing import Dict, List
import threading
import time
import datetime as dt
from src.domain.abstractions.abstract_trading import Abstract_Trading
from src.domain.decorators import check_api_key
from src. infrastructure.mt5 import dwx_client
from time import sleep
from src.application.base_logger import logger
from os.path import join, exists

@check_api_key(
    [
        "MTX_HOST",
        "CLIENT_IF",
        "PUSH_PORT",
        "DATA_DIR",
    ]
)
def get_client(conf_port):
    """Get MetaTrader client.

    Returns
    -------
    Client
      MetaTrader client.
    """
    logger.info("Connecting to MetaTrader")
    client = dwx_client(metatrader_dir_path=conf_port['DATA_DIR'])

    return client


class Trading(Abstract_Trading):
    """Class for trading on MetaTrader

    Attributes
    ----------
    client: Client
        MetaTrader client.
    """

    def __init__(self, send_orders_status: bool = True, exchange_or_broker='', config_broker: Dict = ..., config_brokermq: Dict = ...):
        super().__init__(send_orders_status, exchange_or_broker, config_broker, config_brokermq)