import MetaTrader5 as mt5
from datetime import date
import datetime
import time
import os




def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def getData(symbol, timeframe):
    # Display dataframe with data
    #         time     open     high      low    close  tick_volume  spread  real_volume
    # 0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            0
    # 1 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            0
    # 2 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            0
    # 3 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            0
    
    data = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1)#ultima barra
    #print(data[0][0])
    return data[0]

def setCandlesArray(data, comparison_candles_array,candles_array):
    if( len(comparison_candles_array) <= 1 ):
            comparison_candles_array.append(data)
            
    else:            
        comparison_candles_array.pop(0)
        comparison_candles_array.append(data)
        last = comparison_candles_array[0][0]
        now = comparison_candles_array[1][0]
        
        if( now - last == 60 ):
            candles_array.append(comparison_candles_array[0])
            print("candles_array")
            for e in candles_array:
                print(e)
            return True,comparison_candles_array,candles_array
        
        return False,comparison_candles_array,candles_array
    
    return False,comparison_candles_array,candles_array

def getSwingHigh(data):
    if( len(data)==3 ):
        if(data[1][2] > data[0][2] and data[1][2] > data[2][2]):
            print("SIWNG HIGH!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            print(data[1])
            # array_sh.append(data[1])
            # candles_array.pop(0)
            return data[1],True
        elif( data[0][2] == data[1][2] and data[1][2] > data[2][2]):
            print("SIWNG HIGH!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            print(data[1])
            # array_sh.append(data[1])
            # candles_array.pop(0)
            return data[1],True
        else:
            return (), False

def getSwingLow(data):
    if(len(data)==3):
        if(data[1][3] < data[0][3] and data[1][3] < data[2][3]):
            print("SIWNG LOW!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            print(data[1])
            # array_sl.append(data[1])
            # candles_array.pop(0)
            return data[1],True
        elif(data[0][3] == data[1][3] and data[1][3] < data[2][3]):
            print("SIWNG LOW!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            print(data[1])
            # array_sl.append(data[1])
            # candles_array.pop(0)
            return data[1],True
        else:
            return (), False


def handSetArraySS(marker,candle,array):
    aux_candle = [marker]
    aux_candle.extend(candle)
    array.append(aux_candle)
    return array

    pass

def breakingSwingHigh(candle):
    lenght = len(array_ss)
    if(array_ss[lenght-2][3]<candle[4]):
        print("rompió con cuerpo en el sh")
        print(f"{array_ss[lenght-2]} < {candle}")
        return True
    return False

def breakingSwingLow(candle):
    lenght = len(array_ss)
    if(array_ss[lenght-2][4]> candle[4]):
        print("rompió con cuerpo en el sl")
        print(f"{array_ss[lenght-2]} > {candle}")
        return True
    return False

def handSecuenseShSl(array):
    lenght = len(array)
    if(lenght > 1 and array[lenght - 1][0] == "sl" and array[lenght - 2][0] == "sh" ):
        print("secuencia sh - sl encontrada")
        sl_l=array[lenght - 1][4]
        sh_h=array[lenght - 2][3]
        return (True,sl_l,sh_h)
    return (False,0,0)

def handSecuenseSlSh(array):
    lenght = len(array)
    if(lenght > 1 and array[lenght - 1][0] == "sh" and array[lenght - 2][0] == "sl" ):
        print("secuencia sl - sh encontrada")
        sl_l=array[lenght - 2][4]
        sh_h=array[lenght - 1][3]
        return (True,sl_l,sh_h)
    return (False,0,0)

def findSwingLow(array):
    flag_r = False
    for e in reversed(array):
        if(e[0]=="sl"):
            flag_r = True
            return e
        if(flag_r):
            break
        pass
    pass

def findSwingHigh(array):
    flag_r = False
    for e in reversed(array):
        if(e[0]=="sh"):
            flag_r = True
            return e
        if(flag_r):
            break
        pass
    pass

def requestOrderSendBuy(high,low, take_p):
    lot = 0.01
    # point = mt5.symbol_info(symbol).point
    # price = mt5.symbol_info_tick(SYMBOL).ask
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": SYMBOL,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY_LIMIT,
        "price": high,
        "sl": low,
        "tp": take_p,
        "deviation": deviation,
        "magic": 1234,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_DAY,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    return request

def requestOrderSendSell(high,low, take_p):
    lot = 0.01
    # point = mt5.symbol_info(symbol).point
    # price = mt5.symbol_info_tick(SYMBOL).ask
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": SYMBOL,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL_LIMIT,
        "price": low,
        "sl": high,
        "tp": take_p,
        "deviation": deviation,
        "magic": 1234,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_DAY,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    return request


def run():
        ##############################################
    ############# VARIABLES GLOBALES #############
    ##############################################

    array_ss = []
    comparison_candles_array = []
    candles_array = []
    flag_secuense_Sh = True 
    sl_l= 0 
    sh_h = 0

    ##############################################
    # loop principal. ejecucuión continua del script
    while ( True ):
        candle = getData(SYMBOL,TIMEFRAME)
        flag_candles_array,comparison_candles_array, candles_array = setCandlesArray(candle,comparison_candles_array,candles_array)
        if ( flag_candles_array and ( len(candles_array) == 3 or len(candles_array) == 4) ):
            candle_sh, flag_sh = getSwingHigh(candles_array)
            candle_sl, flag_sl = getSwingLow(candles_array)
            if(flag_sh):
                array_ss = handSetArraySS("sh",candle_sh,array_ss)
            if(flag_sl):
                array_ss = handSetArraySS("sl",candle_sl,array_ss)
            (flag_secuense_Sh, sl_l, sh_h) = handSecuenseShSl(array_ss)
            if(flag_secuense_Sh and candles_array[2][2] > sh_h):#candles_array[2][2] --> high ult. vela
                print("primer rompimiento -- rompimiento en el high")
                print("vela que rompió")
                print(candles_array[2])
                sh_b = sh_h
                sl_b = sl_l
                print(f"valores a romper low: {sl_b} ; high:{sh_h}")
                pass
                if(candles_array[2][4] < sl_b):#candles_array[2][4] --> closed ult. vela
                    for e in array_ss:
                        print(e)
                    print("segundo rompimiento -- rompiendo el low")
                    print(f"swing low a romper con cuerpo {sl_b}")
                    print("vela que rompe ese valor ")
                    print(candles_array[2])
                    print(f"cierre de la vela {candles_array[2][5]}")
                    print("Enviar orden -- 1 !!!")
                    break
            (flag_secuense_Sl, sl_l, sh_h) = handSecuenseSlSh(array_ss)
            if(flag_secuense_Sl and candles_array[2][3] < sl_l):
                print("primer rompimiento -- rompimiento en el low")
                print("vela que rompió")
                print(candles_array[2])
                sh_b = sh_h
                sl_b = sl_l
                print(f"valores a romper low: {sl_b} ; high:{sh_h}")
                pass
                if(candles_array[2][4] > sh_b):
                    for e in array_ss:
                        print(e)
                    print("segundo rompimiento -- rompiendo el high")
                    print(f"swing high a romper con cuerpo {sh_b}")
                    print("vela que rompe ese valor ")
                    print(candles_array[2])
                    print(f"cierre de la vela {candles_array[2][5]}")
                    print("Enviar orden  -- 2 !!!")
                    break
            candles_array.pop(0)
        pass

if __name__ == "__main__":


    ##############################################
    ######## PARAMETROS DE LA ESTRATEGIA #########
    ##############################################
    SYMBOL = "EURUSD"
    VOLUME = 1.0
    TIMEFRAME = mt5.TIMEFRAME_M1
    #DEVIATION = 20
    ##############################################
    
    ##############################################
    ############ CREDENCIALES LOGING #############
    ##############################################
    mt5.initialize()
    USER = 68118260
    PSWD = "Eo01201992"
    SERVER = "RoboForex-Pro"
    mt5.login(USER,PSWD,SERVER)
    ##############################################   
    run()
    mt5.shutdown()