# coding=gbk
from quant.event import EventEngine

from quant.trader.engine import MainEngine
from quant.trader.ui import MainWindow, create_qapp

from quant.gateway.binance import BinanceGateway
from quant.gateway.binances import BinancesGateway
from quant.gateway.huobi import HuobiGateway

from quant.app.cta_strategy import CtaStrategyApp
from quant.app.data_manager import DataManagerApp
from quant.app.data_recorder import DataRecorderApp
from quant.app.algo_trading import AlgoTradingApp
from quant.app.cta_backtester import CtaBacktesterApp
from quant.app.risk_manager import RiskManagerApp
from quant.app.spread_trading import SpreadTradingApp


def main():
    """"""

    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(BinanceGateway)
    main_engine.add_gateway(BinancesGateway)
    main_engine.add_gateway(HuobiGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(DataManagerApp)
    main_engine.add_app(AlgoTradingApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(RiskManagerApp)
    main_engine.add_app(SpreadTradingApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    """
     �Ұ��Ľӿ����ֻ��ͺ�Լ�ӿ�֮�֡� ����֮���������ͨ�����׶������ֵġ��ֻ���Сд����Լ�ô�д�� btcusdt.BINANCE ���ֻ���symbol,
     BTCUSDT.BINANCE��Լ�Ľ��׶ԡ� BTCUSD.BINANCE�Ǻ�Լ�ıұ�λ��֤��Ľ��׶�.
    """

    main()