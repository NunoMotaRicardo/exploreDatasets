import pandas as pd
import numpy as np
import backtrader as bt

import sys
import os

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from ApiClient import ApiClient
api_client = ApiClient()

startDate = '2011-01-03'
endDate = '2025-06-13'
baseSymbol= '^GSPC'


### prepare datasets
fearAndGreed=pd.read_csv('./datasets/fearAndGreed.csv', sep=',')
vix= pd.read_csv('./datasets/vixHistoryData.csv', sep=',')

codeBaseSymbol, baseSymbolData = api_client.get("getIndexHistory", {'tickerSymbol':baseSymbol})
if codeBaseSymbol == 0:
    baseSymbolData = pd.DataFrame(baseSymbolData)
    baseSymbolData['Date'] = pd.to_datetime(baseSymbolData['Date'], unit='ms')
    baseSymbolData = baseSymbolData[
        (baseSymbolData['Date'] >= pd.Timestamp(startDate)) &
        (baseSymbolData['Date'] <= pd.Timestamp(endDate))
    ]
    baseSymbolData['Date'] = baseSymbolData['Date'].dt.strftime('%Y-%m-%d')
    baseSymbolData = baseSymbolData[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    baseSymbolData.to_csv('./datasets/baseSymbolData.csv', sep=',', index=False)
    # Merge baseSymbolData, fearAndGreed, and vix on date columns
    merged_df = baseSymbolData.merge(
        fearAndGreed,
        on='Date',
        how='left'
    ).merge(
        vix,
        on='Date',
        how='left'
    )

    merged_df = merged_df[[
        'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'FearGreed', 'VIX'
    ]]

    merged_df.to_csv('./datasets/combinedData.csv', sep=',', index=False)
else:
    print("Error fetching base symbol history data:", codeBaseSymbol, baseSymbolData)