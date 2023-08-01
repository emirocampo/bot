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
    # print(data[0])
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
            return data[1],True,False
        elif( data[1][2] == data[2][2]):
            return (), False, True
        else:
            return (), False, False
    if( len(data)==4 ):
        if(data[1][2] > data[0][2] and data[2][2] > data[3][2]):
            print("SIWNG HIGH!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            data.pop(0)
            print(data[1])
            return data[1],True,False
        elif(data[2][2] == data[3][2]):
            return (), False, True
        else:
            return (), False, False
    if(len(data) == 5):
        if(data[1][2] > data[0][2] and data[3][2] > data[4][2]):
            print("SIWNG HIGH!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            data.pop(0)
            data.pop(0)
            print(data[1])
            return data[1],True,False
        else:
            return (), False, False

def getSwingLow(data):
    if(len(data)==3):
        if(data[1][3] < data[0][3] and data[1][3] < data[2][3]):
            print("SIWNG LOW!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            print(data[1])
            return data[1],True, False
        elif((data[1][3] == data[2][3]) and (data[1][3] < data[0][3])):
            return (), False, True
        else:
            return (), False, False
    if( len(data)==4 ):
        if(data[1][3] < data[0][3] and data[2][3] < data[3][3]):
            print("SIWNG LOW!!!")
            data.pop(0)
            print(data[1])
            return data[1],True,False
        elif(data[2][4] == data[3][4]):
            return (), False, True
        else:
            data.pop(0)
            return (), False, False
    if( len(data)==5 ):
        if(data[1][3] < data[0][3] and data[3][3] < data[4][3]):
            print("SIWNG LOW!!!")
            data.pop(0)
            data.pop(0)
            print(data[1])
            return data[1],True,False
        else:
            data.pop(0)
            data.pop(0)
            return (), False, False

def handSetArraySS(marker,candle,array):
    aux_candle = [marker]
    aux_candle.extend(candle)
    array.append(aux_candle)
    return array

def handSecuenseShSl(array):
    lenght = len(array)
    if(lenght > 1 and array[lenght - 2][0] == "sh" and array[lenght - 1][0] == "sl"  ):
        print("secuencia sh - sl encontrada")
        sl=array[lenght - 1]
        sh=array[lenght - 2]
        return (True,sl,sh)
    return (False,[],[])

def handSecuenseSlSh(array):
    lenght = len(array)
    if(lenght > 1 and array[lenght - 2][0] == "sl"  and array[lenght - 1][0] == "sh" ):
        print("secuencia sl - sh encontrada")
        sl=array[lenght - 2]
        sh=array[lenght - 1]
        return (True,sl,sh)
    return (False,[],[])

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
    comparison_candles_array = []
    flag_secuense_Sh = True 
    array_pair=[]
    first_break=[[False,"0","0","ss"]]
    

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

    ##############################################
    # loop principal. ejecucuión continua del script
    while ( True ):
        candle = getData(SYMBOL,TIMEFRAME)
        flag_candles_array,comparison_candles_array, candles_array = setCandlesArray(candle,comparison_candles_array,candles_array)
        if ( flag_candles_array and ( len(candles_array) == 3 or len(candles_array) == 4) or len(candles_array) == 5 ):
            candle_sh, flag_sh, flag_sh_2 = getSwingHigh(candles_array)
            candle_sl, flag_sl, flag_sl_2 = getSwingLow(candles_array)
            if(flag_sh):
                array_ss = handSetArraySS("sh",candle_sh,array_ss)
            if(flag_sl):
                array_ss = handSetArraySS("sl",candle_sl,array_ss)
            (flag_secuense_Sh, sl, sh) = handSecuenseShSl(array_ss)
            if(flag_secuense_Sh):
                aux = [sh,sl,["high"]]
                if len(array_pair) != 0:
                    tamano = len(array_pair)
                    if( not (array_pair[tamano - 1] [0] == sh and array_pair[tamano - 1] [1] == sl) ):
                        array_pair.append(aux)
                else:
                    array_pair.append(aux)
            (flag_secuense_Sl, sl, sh) = handSecuenseSlSh(array_ss)
            if(flag_secuense_Sl):
                aux = [sl,sh,["low"]]
                if len(array_pair) != 0:
                    tamano = len(array_pair)
                    if( not (array_pair[tamano -1] [0] == sl and array_pair[tamano - 1] [1] == sh) ):
                        array_pair.append(aux)
                else:
                    array_pair.append(aux)
            if(not first_break[0][0]):
                if len(array_pair) != 0:
                    for e in reversed(array_pair):
                        if e[2][0] == "high":
                            if candles_array[2][1] < e[0][3] and candles_array[2][4] > e[0][3] :
                                print("primer rompimiento -- rompió en el high con cuerpo")
                                print(f" high roto {e[0][3]}")
                                print("vela que rompió")
                                print(candles_array[2])
                                first_break.pop(0)
                                first_break.append([True,e[0][3],e[1][4],"low"])
                                l = len(array_pair)
                                for k in range(l):
                                    array_pair.pop(0)
                                # first_break = [indica un primer rompimiento,guarda el high roto,guarda el low a romper,indica el siguiente rompimiento]
                                break
                        if e[2][0] == "low" :
                            if candles_array[2][4] < e[0][4] and candles_array[2][1] > e[0][4]:
                                print("primer rompimiento -- rompió con cuerpo en el low")
                                print(f" low roto {e[0][4]}")
                                print("vela que rompió")
                                print(candles_array[2])
                                first_break.pop(0)
                                first_break.append([True,e[1][3],e[0][4],"high"])
                                l = len(array_pair)
                                for k in range(l):
                                    array_pair.pop(0)
                                # first_break = [indica un primer rompimiento,guarda el high a romper,guarda el low roto,indica el siguiente rompimiento]
                                break
            else:
                print("buscando segundo rompimiento")
                if first_break[0][3] == "low":
                    if False:
                        #en caso de romper en el alto mas alto que haya entre el primer rompimiento y la vela actual mientras esperaba romper en el low
                        #mi nuevo primer rompimiento (first_break) será la tupla (alto_mas_alto -- sl_siguiente)
                        #y a buscar el segundo rompimiento.
                        pass
                    else: 
                        if candles_array[2][4] < first_break[0][2]:
                            print("segundo rompimiento -- rompió con cuerpo en el low")
                            print(f" low roto {first_break[0][2]}")
                            print("vela que rompió")
                            print(candles_array[2])
                            print("enviar orden 1")
                            candle_sh_nerby = findSwingHigh(array_ss)
                            candle_high = candle_sh_nerby[3]
                            candle_low = candle_sh_nerby[4]
                            take_profit = candle_low - (candle_high - candle_low)*2
                            request = requestOrderSendSell(candle_high,candle_low, take_profit, SYMBOL)
                            result = mt5.order_send(request)
                            print(f"result: {result}")
                            pass
                        pass
                if first_break[0][3] == "high":
                    if False:
                        pass
                    else:
                        if candles_array[2][4] > first_break[0][1]:
                            print("segundo rompimiento -- rompió con cuerpo en el high")
                            print(f" high roto {first_break[0][1]}")
                            print("vela que rompió")
                            print(candles_array[2])
                            print("enviar orden 2")
                            candle_sl_nerby=findSwingLow(array_ss)
                            candle_high = candle_sl_nerby[3]
                            candle_low = candle_sl_nerby[4]
                            take_profit = candle_high + (candle_high - candle_low)*2
                            request = requestOrderSendBuy(candle_high,candle_low, take_profit, SYMBOL)
                            result = mt5.order_send(request)
                            print(result)
                            pass
                        pass
            if( not (flag_sh_2 or flag_sl_2) ):
                # print(candles_array)
                candles_array.pop(0)
                # print("ultimo candles array")
                # print(candles_array)
        

if __name__ == "__main__":

    run()
    mt5.shutdown()