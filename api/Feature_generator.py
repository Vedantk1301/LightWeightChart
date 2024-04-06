import pandas as pd
import pandas_ta as ta
import numpy as np

def calculate_indicators(df):
    # Calculate EMA, MACD, and RSI for the stock
    df['EMA12'] = df['Close'].ta.ema(length=12)
    df['EMA26'] = df['Close'].ta.ema(length=26)
    df['EMA50'] = df['Close'].ta.ema(length=50)
    df['ATR'] = df.ta.atr(length=14)
    df['ROC'] = df['Close'].ta.roc(length=12)
    df['MACD'] = df['Close'].ta.macd(fast=12, slow=26, signal=9)
    df['RSI'] = df['Close'].ta.rsi(length=14)
    bb_bands = df['Close'].ta.bbands(length=20, std=2)
    df['BB_upper'] = bb_bands['BBU_20_2.0']
    df['BB_lower'] = bb_bands['BBL_20_2.0']
    df['DI_pos'] = df.ta.dpo(length=14)
    df['SMA'] = df['Close'].ta.sma(length=20)
    df['TSF'] = df['Close'].ta.tsf(length=14)
    df['WCP'] = df.ta.wcp()
    df['WMA'] = df['Close'].ta.wma(length=20)
    df['SAR'] = df.ta.sar(acceleration=0.02, maximum=0.2)
    df['OBV'] = df.ta.obv()
    df.dropna(axis=0, inplace=True)
    
    return df
