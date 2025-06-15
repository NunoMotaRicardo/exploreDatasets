import backtrader as bt
import datetime 

class TradeStrategy(bt.Strategy):

    def __init__(self):
        self.fear_greed = self.datas[0].fear_greed
        self.vix = self.datas[0].vix
        self.close = self.datas[0].close

    def next(self):
        price = self.close[0]
        size = int(self.broker.getcash() / price)
        #print(f"Current cash: {self.broker.getcash()}, buy: {size*price}, Fear & Greed Index: {self.fear_greed[0]}, VIX: {self.vix[0]}")
        #if self.fear_greed[0] < 0.2 and not self.position:
        #    self.buy(size=size)
        #if self.fear_greed[0] > 0.9 and self.position.size > 0:
        #    self.sell(size=self.position.size)
        if self.vix[0] < 0.7 and not self.position:
            self.buy(size=size/ 2)  # Buy half the size if VIX is high
            print(f"Buying at {price*size/2}, position: {self.position}")
        if self.vix[0] > 1.25 and self.position.size > 0:
            self.sell(size=self.position.size)