import sys
from time import sleep
from datetime import datetime, time
from logging import INFO

from quant.event import EventEngine
from quant.trader.setting import SETTINGS
from quant.trader.engine import MainEngine

from quant.gateway.binances import BinancesGateway
from quant.gateway.binance import BinanceGateway

from quant.app.cta_strategy import CtaStrategyApp
from quant.app.cta_strategy.base import EVENT_CTA_LOG


SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True

binance_settings = {
    "key": "",
    "secret": "",
    "session_number": 3,
    "proxy_host": "",
    "proxy_port": 0
}


binances_setting = {
        "key": "",
        "secret": "",
        "�Ự��": 3,
        "������": "REAL",
        "��Լģʽ": "����",
        "�����ַ": "",
        "����˿�": 0,
    }


def run():
    """
    Running in the child process.
    """
    SETTINGS["log.file"] = True

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(BinancesGateway)
    main_engine.add_gateway(BinanceGateway)
    cta_engine = main_engine.add_app(CtaStrategyApp)
    main_engine.write_log("�����洴���ɹ�")

    log_engine = main_engine.get_engine("log")
    event_engine.register(EVENT_CTA_LOG, log_engine.process_log_event)
    main_engine.write_log("ע����־�¼�����")

    main_engine.connect(binances_setting, "BINANCES")
    main_engine.write_log("����BINANCES�ӿ�")

    sleep(10)

    cta_engine.init_engine()
    main_engine.write_log("CTA���Գ�ʼ�����")

    cta_engine.add_strategy('MA10_MA20_15MINStrategy', 'btcusdt_spot', 'btcusdt.BINANCE', {}) #������ĳ��Լ��Ĳ���

    cta_engine.init_all_strategies()
    sleep(60)   # Leave enough time to complete strategy initialization
    main_engine.write_log("CTA����ȫ����ʼ��")

    cta_engine.start_all_strategies()
    main_engine.write_log("CTA����ȫ������")

    while True:
        sleep(10)

if __name__ == "__main__":
    run()
