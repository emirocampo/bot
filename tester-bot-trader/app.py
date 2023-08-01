import csv
import time

def getListCandles():
    array = []
    ruta = "D:/Documents/python-metatrader5/tester-bot-trader/prueba-datos.csv"
    ruta_2 = "EURUSD1.csv"
    ruta_3 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD1.csv"
    ruta_4 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD_M1_HIGH_3.csv"
    ruta_5 = "D:/Documents/python-metatrader5/tester-bot-trader/EURUSD_M1_LOW_3.csv"
    ruta_6 = "D:/Documents/python-metatrader5/tester-bot-trader/BCHUSD_M1_DOS_ROMP.csv"
    ruta_7 = "D:/Documents/python-metatrader5/tester-bot-trader/.US30Cash_M1_ROMP.csv"
    ruta_8 = "D:/Documents/python-metatrader5/tester-bot-trader/BCHUSD_M1.csv"
    with open(ruta_8,"r") as file:
        reader = csv.reader(file)
        for e in reader:
            array.append(e)
        return array
    pass

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
        if(data[1][3] > data[0][3] and data[1][3] > data[2][3]):
            print("SIWNG HIGH!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            return data[1],True,False
        elif(data[1][3] == data[2][3]):
            return (), False, True
        else:
            return (), False, False
    if( len(data)==4 ):
        if(data[1][3] > data[0][3] and data[2][3] > data[3][3]):
            print("SIWNG HIGH!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(f"vela 3 {data[3]}")
            data.pop(0)
            return data[1],True,False
        elif(data[2][3] == data[3][3]):
            return (), False, True
        else:
            return (), False, False
    if(len(data) == 5):
        if(data[1][3] > data[0][3] and data[3][3] > data[4][3]):
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
            return (), False, False

def getSwingLow(data):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    if( len(data)==3 ):
        if(data[1][4] < data[0][4] and data[1][4] < data[2][4]):
            print("SIWNG LOW!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            return data[1],True,False
        elif((data[1][4] == data[2][4]) and (data[1][4] < data[0][4])):
            return (), False, True
        else:
            return (), False, False
    if( len(data)==4 ):
        if(data[1][4] < data[0][4] and data[2][4] < data[3][4]):
            print("SIWNG LOW!!!")
            print(f"vela 0 {data[0]}")
            print(f"vela 1 {data[1]}")
            print(f"vela 2 {data[2]}")
            print(f"vela 3 {data[3]}")
            data.pop(0)
            return data[1],True,False
        elif(data[2][4] == data[3][4]):
            return (), False, True
        else:
            data.pop(0)
            return (), False, False
    if( len(data)==5 ):
        if(data[1][4] < data[0][4] and data[3][4] < data[4][4]):
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
            return (), False, False

def handSetArraySS(marker,candle,array):
    aux_candle = [marker]
    aux_candle.extend(candle)
    array.append(aux_candle)
    return array


def handSecuenseShSl(array):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    lenght = len(array)
    if(lenght > 1 and array[lenght - 2][0] == "sh" and array[lenght - 1][0] == "sl" ):
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
    if(lenght > 1  and array[lenght - 2][0] == "sl" and array[lenght - 1][0] == "sh" ):
        sl=array[lenght - 2]
        sh=array[lenght - 1]
        print(f"Dentro de handSecuenseSlSh")
        return (True,sl,sh)
    return (False,0,0)

# def requestOrderSendBuy(high,low, take_p):
#     lot = 0.01
#     # point = mt5.symbol_info(symbol).point
#     # price = mt5.symbol_info_tick(SYMBOL).ask
#     deviation = 20
#     request = {
#         "action": mt5.TRADE_ACTION_PENDING,
#         "symbol": SYMBOL,
#         "volume": lot,
#         "type": mt5.ORDER_TYPE_BUY_LIMIT,
#         "price": high,
#         "sl": low,
#         "tp": take_p,
#         "deviation": deviation,
#         "magic": 1234,
#         "comment": "python script open",
#         "type_time": mt5.ORDER_TIME_DAY,
#         "type_filling": mt5.ORDER_FILLING_RETURN,
#     }
#     return request

# def requestOrderSendSell(high,low, take_p):
#     lot = 0.01
#     # point = mt5.symbol_info(symbol).point
#     # price = mt5.symbol_info_tick(SYMBOL).ask
#     deviation = 20
#     request = {
#         "action": mt5.TRADE_ACTION_PENDING,
#         "symbol": SYMBOL,
#         "volume": lot,
#         "type": mt5.ORDER_TYPE_SELL_LIMIT,
#         "price": low,
#         "sl": high,
#         "tp": take_p,
#         "deviation": deviation,
#         "magic": 1234,
#         "comment": "python script open",
#         "type_time": mt5.ORDER_TIME_DAY,
#         "type_filling": mt5.ORDER_FILLING_RETURN,
#     }
#     return request

def run():
    i_list_candles = 0
    candles_array = []
    array_ss = []
    array_pair=[]
    first_break=[[False,"0","0","ss"]]
    candles_all = getListCandles()
    highest_high = "0"
    lowest_low = "0"
    sh_b = "0"
    sl_b = "0"
    j = 0
    while j < len(candles_all):
        if j == 21:
            pass
        candle, i_list_candles= getCandle(candles_all,i_list_candles)
        flag_candles_array,candles_array = setCandlesArray(candle,candles_array)
        if (flag_candles_array and (len(candles_array) == 3 or len(candles_array) == 4 or len(candles_array) == 5)):
            candle_sh, flag_sh, flag_sh_2 = getSwingHigh(candles_array)
            candle_sl, flag_sl, flag_sl_2 = getSwingLow(candles_array)
            if(flag_sh):
                array_ss = handSetArraySS("sh",candle_sh,array_ss)
                if candle_sh[3] > highest_high:
                    highest_high = candle_sh[3]
            if(flag_sl): 
                array_ss = handSetArraySS("sl",candle_sl,array_ss)
                if candle_sl[4] < lowest_low:
                    lowest_low = candle_sh[4]
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
                            if candles_array[2][2] < e[0][4] and candles_array[2][5] > e[0][4] :
                                print("primer rompimiento -- rompió en el high con cuerpo")
                                print(f" high roto {e[0][4]}")
                                print("vela que rompió")
                                print(candles_array[2])
                                first_break.pop(0)
                                first_break.append([True,e[0][4],e[1][5],"low"])
                                l = len(array_pair)
                                for i in range(l):
                                    array_pair.pop(0)
                                # first_break = [indica un primer rompimiento,guarda el high roto,guarda el low a romper,indica el siguiente rompimiento]
                                break
                        if e[2][0] == "low" :
                            if candles_array[2][5] < e[0][5] and candles_array[2][2] > e[0][5]:
                                print("primer rompimiento -- rompió con cuerpo en el low")
                                print(f" low roto {e[0][5]}")
                                print("vela que rompió")
                                print(candles_array[2])
                                first_break.pop(0)
                                first_break.append([True,e[1][4],e[0][5],"high"])
                                l = len(array_pair)
                                for i in range(l):
                                    array_pair.pop(0)
                                # first_break = [indica un primer rompimiento,guarda el high a romper,guarda el low roto,indica el siguiente rompimiento]
                                break
            else:
                print("buscando segundo rompimiento")
                if first_break[0][3] == "low":
                    if candles_array[2][5] > highest_high:
                        #en caso de romper en el mas alto (highest_high) mientras esperaba romper en el low
                        #mi nuevo primer rompimiento (first_break) será la tupla (highest_high - sl-siguiente)
                        #y buscar el segundo rompimiento
                        pass
                    else: 
                        if candles_array[2][5] < first_break[0][2]:
                            print("segundo rompimiento -- rompió con cuerpo en el low")
                            print(f" low roto {first_break[0][2]}")
                            print("vela que rompió")
                            print(candles_array[2])
                            print("enviar orden 1")
                            # request = requestOrderSendSell(candle_high,candle_low, take_profit)
                            # result = mt5.order_send(request)
                            pass
                        pass
                if first_break[0][3] == "high":
                    if candles_array[2][5] < lowest_low:
                        pass
                    else:
                        if candles_array[2][5] > first_break[0][1]:
                            print("segundo rompimiento -- rompió con cuerpo en el high")
                            print(f" low roto {first_break[0][1]}")
                            print("vela que rompió")
                            print(candles_array[2])
                            print("enviar orden 2")
                            # request = requestOrderSendBuy(candle_high,candle_low, take_profit)
                            # result = mt5.order_send(request)
                            pass
                        pass
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
    print(f"sh_b {sh_b};  sl_b {sl_b}")
        
        
        
        
        

if __name__ == "__main__":
    
    run()