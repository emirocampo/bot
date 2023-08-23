import MetaTrader5 as mt5
from datetime import date
import datetime
import time
import os
import credentials as crd




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
    for e in data:
            aux = {
                "TIME":int(e[0]),
                "OPEN":float(e[1]),
                "HIGH":float(e[2]),
                "LOW":float(e[3]),
                "CLOSE":float(e[4]),
                "TICKVOL":float(e[5]),
                "VOL":float(e[6]),
                "SPREAD":float(e[7])
            }
    # print(data[0])
    return aux

def setCandlesArray(data, comparison_candles_array,candles_array):
    if( len(comparison_candles_array) <= 1 ):
            comparison_candles_array.append(data)
            
    else:            
        comparison_candles_array.pop(0)
        comparison_candles_array.append(data)
        last = comparison_candles_array[0]["TIME"]
        now = comparison_candles_array[1]["TIME"]
        
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
        if(data[1]["HIGH"] > data[0]["HIGH"] and data[1]["HIGH"] > data[2]["HIGH"]):
            print("SIWNG HIGH!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            return data[1],True,False
        elif(data[1]["HIGH"] == data[2]["HIGH"]):
            return {}, False, True
        else:
            return {}, False, False
    if( len(data)==4 ):
        if(data[1]["HIGH"] > data[0]["HIGH"] and data[2]["HIGH"] > data[3]["HIGH"]):
            print("SIWNG HIGH!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(f"vela 3 {data[3]}")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            data.pop(0)
            return data[1],True,False
        elif(data[2]["HIGH"] == data[3]["HIGH"]):
            return {}, False, True
        else:
            return {}, False, False
    if(len(data) == 5):
        if(data[1]["HIGH"] > data[0]["HIGH"] and data[3]["HIGH"] > data[4]["HIGH"]):
            print("SIWNG HIGH!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(f"vela 3 {data[3]}")
            print(f"vela 4 {data[4]}")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            data.pop(0)
            data.pop(0)
            print(data[1])
            return data[1],True,False
        else:
            return (), False, False

def getSwingLow(data):
    if(len(data)==3):
        if(data[1]["LOW"] < data[0]["LOW"] and data[1]["LOW"] < data[2]["LOW"]):
            print("SIWNG LOW!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            return data[1],True, False
        elif((data[1]["LOW"] == data[2]["LOW"]) and (data[1]["LOW"] < data[0]["LOW"])):
            return {}, False, True
        else:
            return {}, False, False
    if( len(data)==4 ):
        if(data[1]["LOW"] < data[0]["LOW"] and data[2]["LOW"] < data[3]["LOW"]):
            print("SIWNG LOW!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(f"vela 3 {data[3]}")
            data.pop(0)
            return data[1],True,False
        elif(data[2]["LOW"] == data[3]["LOW"]):
            return {}, False, True
        else:
            data.pop(0)
            return {}, False, False
    if( len(data)==5 ):
        if(data[1]["LOW"] < data[0]["LOW"] and data[3]["LOW"] < data[4]["LOW"]):
            print("SIWNG LOW!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(f"vela 3 {data[3]}")
            print(f"vela 4 {data[4]}")
            data.pop(0)
            data.pop(0)
            return data[1],True,False
        else:
            data.pop(0)
            data.pop(0)
            return {}, False, False

def handSetArraySS(marker,candle,array):
    candle["SS"] = marker
    array.append(candle)
    return array

def handSecuenseShSl(array):
    lenght = len(array)
    if(lenght > 1 and array[lenght - 2]["SS"] == "sh" and array[lenght - 1]["SS"] == "sl"):
        print("secuencia sh - sl encontrada")
        sl=array[lenght - 1]
        sh=array[lenght - 2]
        return True,sl,sh
    return (False,[],[])

def handSecuenseSlSh(array):
    lenght = len(array)
    if(lenght > 1  and array[lenght - 2]["SS"] == "sl" and array[lenght - 1]["SS"] == "sh"):
        print("secuencia sl - sh encontrada")
        sl=array[lenght - 2]
        sh=array[lenght - 1]
        return True,sl,sh
    return False,[],[]

def findSwingHigh(array):
    flag_r = False
    for e in reversed(array):
        if(e["SS"]=="sh"):
            flag_r = True
            return e
        if(flag_r):
            break
        pass
    pass

def findSwingLow(array):
    flag_r = False
    for e in reversed(array):
        if(e["SS"]=="sl"):
            flag_r = True
            return e
        if(flag_r):
            break
        pass
    pass

def requestOrderSendBuy(high,low, take_p, SYMBOL):
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

def requestOrderSendSell(high,low, take_p, SYMBOL):
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

    candles_array = []
    array_ss = []
    array_pair=[]
    comparison_candles_array = []
    flag_secuense_Sh = True 
    first_break=[{"STATE":False,"SH":"0","SL":"0","NEXT":"S_S"}]
    

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
    # USER = 68118260
    # PSWD = "Eo01201992"
    # SERVER = "RoboForex-Pro"
    # Las credenciales de acceso a la cuenta se manejan en un script externo no guardado en git
    # import credentials as crd --> aqui se importan las credenciales
    key = crd.getKeys() # --> aquí se usan las credenciales
    mt5.login(key["USER"],key["PSWD"],key["SERVER"])
    ##############################################  

    ##############################################
    # loop principal. ejecucuión continua del script
    while ( True ):
        candle = getData(SYMBOL,TIMEFRAME)
        flag_candles_array,comparison_candles_array, candles_array = setCandlesArray(candle,comparison_candles_array,candles_array)
        if ( flag_candles_array and ( len(candles_array) == 3 or len(candles_array) == 4) or len(candles_array) == 5 ):
            candle_sh, flag_sh, flag_sh_2 = getSwingHigh(candles_array)
            candle_sh_send = candle_sh.copy()
            candle_sl, flag_sl, flag_sl_2 = getSwingLow(candles_array)
            candle_sl_send = candle_sl.copy()
            if(flag_sh):
                array_ss = handSetArraySS("sh",candle_sh_send,array_ss)
            if(flag_sl):
                array_ss = handSetArraySS("sl",candle_sl_send,array_ss)
            (flag_secuense_Sh, sl, sh) = handSecuenseShSl(array_ss)
            if(flag_secuense_Sh):
                aux = [sh,sl,["high"]] #--> se puede mejorar (?)
                if len(array_pair) != 0:
                    length_pair = len(array_pair)
                    if( not (array_pair[length_pair - 1] [0] == sh and array_pair[length_pair - 1] [1] == sl) ):
                        array_pair.append(aux)
                else:
                    array_pair.append(aux)
            (flag_secuense_Sl, sl, sh) = handSecuenseSlSh(array_ss)
            if(flag_secuense_Sl):
                aux = [sl,sh,["low"]] #--> se puede mejorar (?)
                if len(array_pair) != 0:
                    length_pair = len(array_pair)
                    if( not (array_pair[length_pair -1] [0] == sl and array_pair[length_pair - 1] [1] == sh) ):
                        array_pair.append(aux)
                else:
                    array_pair.append(aux)
            if(not first_break[0]["STATE"]):
                if len(array_pair) != 0:
                    for e in reversed(array_pair):
                        if e[2][0] == "high":
                            if candles_array[2]["OPEN"] < e[0]["HIGH"] and candles_array[2]["CLOSE"] > e[0]["HIGH"] :
                                print("primer rompimiento -- rompió en el high con cuerpo")
                                # print(f" high roto {e[0][3]}")
                                # print("vela que rompió")
                                # print(candles_array[2])
                                # first_break.pop(0)
                                # first_break.append([True,e[0][3],e[1][4],"low"])
                                # l = len(array_pair)
                                # for k in range(l):
                                #     array_pair.pop(0)
                                # first_break = [indica un primer rompimiento,guarda el high roto,guarda el low a romper,indica el siguiente rompimiento]
                                candle_sl_nerby=findSwingLow(array_ss)
                                candle_high = candle_sl_nerby["HIGH"]
                                candle_low = candle_sl_nerby["LOW"]
                                take_profit = candle_high + (candle_high - candle_low)*2
                                request = requestOrderSendBuy(candle_high,candle_low, take_profit, SYMBOL)
                                # FUNCIÓN QUE CONTROLE UNA OPERACIÓN ABIERTA A LA VEZ
                                orders=mt5.orders_get()
                                if orders is None:
                                    result = mt5.order_send(request)
                                    print(f"result: {result}")
                                l = len(array_pair)
                                for k in range(l):
                                    array_pair.pop(0)
                                break
                        if e[2][0] == "low" :
                            if candles_array[2]["CLOSE"] < e[0]["LOW"] and candles_array[2]["OPEN"] > e[0]["LOW"]:
                                # print("primer rompimiento -- rompió con cuerpo en el low")
                                # print(f" low roto {e[0][4]}")
                                # print("vela que rompió")
                                # print(candles_array[2])
                                # first_break.pop(0)
                                # first_break.append([True,e[1][3],e[0][4],"high"])
                                candle_sh_nerby = findSwingHigh(array_ss)
                                candle_high = candle_sh_nerby["HIGH"]
                                candle_low = candle_sh_nerby["LOW"]
                                take_profit = candle_low - (candle_high - candle_low)*2
                                request = requestOrderSendSell(candle_high,candle_low, take_profit, SYMBOL)
                                # FUNCIÓN QUE CONTROLE UNA OPERACIÓN ABIERTA A LA VEZ
                                orders=mt5.orders_get()
                                if orders is None:
                                    result = mt5.order_send(request)
                                    print(f"result: {result}")
                                l = len(array_pair)
                                for k in range(l):
                                    array_pair.pop(0)
                                # first_break = [indica un primer rompimiento,guarda el high a romper,guarda el low roto,indica el siguiente rompimiento]
                                break
            if( not (flag_sh_2 or flag_sl_2) ):
                candles_array.pop(0)

if __name__ == "__main__":

    run()
    mt5.shutdown()