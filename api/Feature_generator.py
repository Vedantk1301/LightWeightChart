import pandas as pd
import pandas_ta as ta
import numpy as np
from io import BytesIO  # Import BytesIO class from io module

def calculate_indicators(df):
    # Calculate EMA, MACD, and RSI for the stock
    df['EMA12'] = df.ta.ema(close='Close', length=12)
    df['EMA26'] = df.ta.ema(close='Close', length=26)
    df['EMA50'] = df.ta.ema(close='Close', length=50)
    df['ATR'] = df.ta.atr(high='High', low='Low', close='Close', length=14)
    df['ROC'] = df.ta.roc(close='Close', length=12)
    macd = ta.macd(df['Close'], fast=12, slow=26, signal=9)
    df['MACD'] = macd.iloc[:, 0]  # Accessing the MACD values from the DataFrame
    df['MACD_signal'] = macd.iloc[:, 1]  # Accessing the MACD signal line values
    df['RSI'] = df.ta.rsi(close='Close', length=14)
    bb_bands = ta.bbands(df['Close'], length=20, std=2)
    df['BB_upper'] = bb_bands['BBU_20_2.0']
    df['BB_lower'] = bb_bands['BBL_20_2.0']
    df['DI_pos'] = df.ta.dpo(close='Close', length=14)
    df['SMA'] = df.ta.sma(close='Close', length=20)
    df['TSF'] = df['Close'].rolling(window=14).mean()  # Calculate TSF manually
    df['WCP'] = df.ta.wcp(close='Close')
    df['WMA'] = df.ta.wma(close='Close', length=20)
    
    # Calculate SAR manually
    initial_sar = df.iloc[0]['High'] if df.iloc[0]['Close'] > df.iloc[1]['Close'] else df.iloc[0]['Low']
    sar = [initial_sar]
    for i in range(1, len(df)):
        if sar[i - 1] < df.iloc[i]['High']:
            sar.append(min(sar[i - 1] + df.iloc[i]['ATR'], df.iloc[i]['Low']))
        else:
            sar.append(max(sar[i - 1] - df.iloc[i]['ATR'], df.iloc[i]['High']))
    df['SAR'] = sar
    
    df['OBV'] = df.ta.obv(close='Close', volume='Volume')
    df.dropna(axis=0, inplace=True)
    
    return df
