import csv
import datetime



def getListCandles():
    '''
    se debe tener el cuidado al pasar a producción el codigo puesto que en caliente el campo DATE y TIME son uno solo
    '''
    array = []
    ruta = "D:/Documents/python-metatrader5/tester-bot-trader/prueba-datos.csv"
    ruta_2 = "EURUSD1.csv"
    ruta_3 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD1.csv"
    ruta_4 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD_M1_HIGH_3.csv"
    ruta_5 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD_M1_LOW_3.csv"
    ruta_6 = "D:/Documents/python-metatrader5/tester-bot-trader/BCHUSD_M1_DOS_ROMP.csv"
    ruta_7 = "D:/Documents/python-metatrader5/tester-bot-trader/.US30Cash_M1_ROMP.csv"
    ruta_8 = "D:/Documents/python-metatrader5/tester-bot-trader/BCHUSD_M1.csv"
    ruta_9 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD_M1_SALIDA.csv"
    with open(ruta_9,"r") as file:
        reader = csv.reader(file)
        for e in reader:
            aux = {
                "DATE":datetime.datetime.strptime(e[0], '%Y.%m.%d').date(),
                "TIME":datetime.datetime.strptime(e[1], "%H:%M:%S").time(),
                "OPEN":float(e[2]),
                "HIGH":float(e[3]),
                "LOW":float(e[4]),
                "CLOSE":float(e[5]),
                "TICKVOL":float(e[6]),
                "VOL":float(e[7]),
                "SPREAD":float(e[8])
            }
            array.append(aux)
        return array

def getCandle(array,i):
    len(array)
    for e in range(i,i+1):
        n_i =i + 1
        return array[e],n_i
    pass

def setCandlesArray(data,array):
    array.append(data)
    return True, array

def getSwingHigh(data):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    if( len(data)==3 ):
        if(data[1]["HIGH"] > data[0]["HIGH"] and data[1]["HIGH"] > data[2]["HIGH"]):
            print("SIWNG HIGH!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
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
            data.pop(0)
            data.pop(0)
            return data[1],True,False
        else:
            return {}, False, False

def getSwingLow(data):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    if( len(data)==3 ):
        if(data[1]["LOW"] < data[0]["LOW"] and data[1]["LOW"] < data[2]["LOW"]):
            print("SIWNG LOW!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            return data[1],True,False
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
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    lenght = len(array)
    if(lenght > 1 and array[lenght - 2]["SS"] == "sh" and array[lenght - 1]["SS"] == "sl"):
        sl=array[lenght - 1]
        sh=array[lenght - 2]
        print(f"Dentro de handSecuenseShSl")
        return (True,sl,sh)
    return (False,[],[])

def handSecuenseSlSh(array):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    lenght = len(array)
    if(lenght > 1  and array[lenght - 2]["SS"] == "sl" and array[lenght - 1]["SS"] == "sh"):
        sl=array[lenght - 2]
        sh=array[lenght - 1]
        print(f"Dentro de handSecuenseSlSh")
        return (True,sl,sh)
    return (False,0,0)

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

def requestOrderSendSell(high,low, take_p, SYMBOL):
    lot = 0.01
    # point = mt5.symbol_info(symbol).point
    # price = mt5.symbol_info_tick(SYMBOL).ask
    deviation = 20
    request = {
        "action": "mt5.TRADE_ACTION_PENDING",
        "symbol": SYMBOL,
        "volume": lot,
        "type": "mt5.ORDER_TYPE_SELL_LIMIT",
        "price": low,
        "sl": high,
        "tp": take_p,
        "deviation": deviation,
        "magic": 1234,
        "comment": "python script open",
        "type_time": "mt5.ORDER_TIME_DAY",
        "type_filling": "mt5.ORDER_FILLING_RETURN",
    }
    return request

def requestOrderSendBuy(high,low, take_p, SYMBOL):
    lot = 0.01
    # point = mt5.symbol_info(symbol).point
    # price = mt5.symbol_info_tick(SYMBOL).ask
    deviation = 20
    request = {
        "action": "mt5.TRADE_ACTION_PENDING",
        "symbol": SYMBOL,
        "volume": lot,
        "type": "mt5.ORDER_TYPE_BUY_LIMIT",
        "price": high,
        "sl": low,
        "tp": take_p,
        "deviation": deviation,
        "magic": 1234,
        "comment": "python script open",
        "type_time": "mt5.ORDER_TIME_DAY",
        "type_filling": "mt5.ORDER_FILLING_RETURN",
    }
    return request

def run():
    i_list_candles = 0
    candles_array = []
    array_ss = []
    array_pair = []
    array_operations = []
    first_break=[{"STATE":False,"SH":"0","SL":"0","NEXT":"S_S"}]
    candles_all = getListCandles()

    ##############################################
    ######## PARAMETROS DE LA ESTRATEGIA #########
    ##############################################
    SYMBOL = "EURUSD"
    VOLUME = 1.0
    TIMEFRAME = "mt5.TIMEFRAME_M1"
    #DEVIATION = 20
    ##############################################

    j = 0
    while j < len(candles_all):
        if j == 11:
            pass
        candle, i_list_candles= getCandle(candles_all,i_list_candles)
        flag_candles_array,candles_array = setCandlesArray(candle,candles_array)
        if (flag_candles_array and (len(candles_array) == 3 or len(candles_array) == 4 or len(candles_array) == 5)):
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
            if(not first_break[0]["STATE"]):
                if len(array_pair) != 0:
                    for e in reversed(array_pair):
                        if e[2][0] == "high":
                            if candles_array[2]["OPEN"] < e[0]["HIGH"] and candles_array[2]["CLOSE"] > e[0]["HIGH"] :
                                print("primer rompimiento -- rompió en el high con cuerpo")
                                # print(f" high roto {e[0]['HIGH']}")
                                # print("vela que rompió")
                                # print(candles_array[2])
                                # first_break.pop(0)
                                # #[{"STATE":False,"SH":"0","SL":"0","NEXT":"S_S"}]
                                # # first_break.append([True,e[0][4],e[1][5],"low"])
                                # first_break.append({"STATE":True,"SH":e[0]["HIGH"],"SH_T":e[0]["TIME"],"SL":e[1]["LOW"],"SL_T":e[1]["TIME"],"NEXT":"low"})
                                # # first_break = [indica un primer rompimiento,guarda el high roto,guarda el low a romper,indica el siguiente rompimiento]
                                # l = len(array_pair)
                                # for i in range(l):
                                #     array_pair.pop(0)
                                candle_sl_nerby=findSwingLow(array_ss)
                                candle_high = candle_sl_nerby["HIGH"]
                                candle_low = candle_sl_nerby["LOW"]
                                take_profit = candle_high + (candle_high - candle_low)*2
                                request = requestOrderSendBuy(candle_high,candle_low, take_profit, SYMBOL)
                                # FUNCIÓN QUE CONTROLE UNA OPERACIÓN ABIERTA A LA VEZ
                                break
                        if e[2][0] == "low" :
                            if candles_array[2]["CLOSE"] < e[0]["LOW"] and candles_array[2]["OPEN"] > e[0]["LOW"]:
                                print("primer rompimiento -- rompió con cuerpo en el low")
                                # print(f" low roto {e[0]['LOW']}")
                                # print("vela que rompió")
                                # print(candles_array[2])
                                # first_break.pop(0)
                                # # first_break.append([True,e[1][4],e[0][5],"high"])
                                # first_break.append({"STATE":True,"SL":e[0]["LOW"],"SL_T":e[0]["TIME"],"SH":e[1]["HIGH"],"SH_T":e[1]["TIME"],"NEXT":"high"})
                                # # first_break = [indica un primer rompimiento,guarda el high a romper,guarda el low roto,indica el siguiente rompimiento]
                                # l = len(array_pair)
                                # for i in range(l):
                                #     array_pair.pop(0)
                                candle_sh_nerby = findSwingHigh(array_ss)
                                candle_high = candle_sh_nerby["HIGH"]
                                candle_low = candle_sh_nerby["LOW"]
                                take_profit = candle_low - (candle_high - candle_low)*2
                                request = requestOrderSendSell(candle_high,candle_low, take_profit, SYMBOL)
                                # FUNCIÓN QUE CONTROLE UNA OPERACIÓN ABIERTA A LA VEZ
                                break
            if( not (flag_sh_2 or flag_sl_2) ):
                # print(candles_array)
                candles_array.pop(0)
                # print("ultimo candles array")
                # print(candles_array)
        j = j + 1
    print("##########################################")
    print("########## fin de la ejecución ###########")
    print("##########################################")
    
    print("array_ss")
    for e in array_ss:
        print(e)


if __name__ == "__main__":
    
    run()