import pandas as pd
import numpy as np
import backtrader as bt
import matplotlib.pyplot as plt

import sys
import os

from TradeStrategy import TradeStrategy

#dataFolder = "./datasets/"
dataFolder = "./processedDatasets/"

combined_csv_file = os.path.join(dataFolder, "combinedData.csv")
vix_csv_file = os.path.join(dataFolder, "vixHistoryData.csv")
fear_greed_csv_file = os.path.join(dataFolder, "fearAndGreed.csv")

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

class combinedData(bt.feeds.GenericCSVData):
    lines = ('fear_greed', 'vix')
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('fear_greed', 6),
        ('vix', 7)
    )
class FearGreedData(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('close', 1),
        ('open', -1),
        ('high', -1),
        ('low', -1),
        ('volume', -1),
        ('openinterest', -1)
    )

class VIXData(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('close', 1),
        ('open', -1),
        ('high', -1),
        ('low', -1),
        ('volume', -1),
        ('openinterest', -1)
    )

combinedFeed = combinedData(dataname=combined_csv_file)
fearGreedFeed = FearGreedData(dataname=fear_greed_csv_file)
vixFeed = VIXData(dataname=vix_csv_file)

cerebro.adddata(combinedFeed)
cerebro.adddata(fearGreedFeed)
cerebro.adddata(vixFeed)

cerebro.addstrategy(TradeStrategy)
cerebro.run()
cerebro.plot(volume=False)