import MetaTrader5 as mt5
import datetime
import time

def getData(symbol, timeframe, candles):

    mt5.initialize()
    USER = 68118260
    PSWD = "Eo01201992"
    SERVER = "RoboForex-Pro"
    mt5.login(USER,PSWD,SERVER)

    # Display dataframe with data
    #         time     open     high      low    close  tick_volume  spread  real_volume
    # 0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            0
    # 1 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            0
    # 2 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            0
    # 3 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            0
    
    data = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1) 
    for row in data:
        print(datetime.datetime.fromtimestamp(row[0]))
        print(row)
    # print(datetime.datetime.fromtimestamp(data[0][0]))
    # print(data[0])
    # return data

if(__name__ == "__main__"):
    SYMBOL = "EURUSD"
    VOLUME = 1.0
    TIMEFRAME = mt5.TIMEFRAME_M1
    CANDLES = 1

    getData(SYMBOL,TIMEFRAME, CANDLES)
    # while True:
    #     getData(SYMBOL,TIMEFRAME, CANDLES)
    #     time.sleep(0.5)