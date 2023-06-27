import MetaTrader5 as mt5
from datetime import date
import datetime
import time
import os



##############################################
############# VARIABLES GLOBALES #############
##############################################

array_sh = []
array_sl = []
array_ss = []
comparison_candles_array = []
candles_array = []

##############################################
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

def setCandleArray(data):
    if( len(comparison_candles_array) <= 1 ):
            comparison_candles_array.append(data)
            
    else:            
        comparison_candles_array.pop(0)
        comparison_candles_array.append(data)
        last = comparison_candles_array[0][0]
        now = comparison_candles_array[1][0]
        
        if( now - last == 60 ):
            candles_array.append(comparison_candles_array[0])
            return True
        
        return False
    
    return False

def getSwingHigh(data):
    if( len(data)==3 ):
        if(data[1][2] > data[0][2] and data[1][2] > data[2][2]):
            print("SIWNG HIGH!!!")
            print(datetime.datetime.fromtimestamp(data[1][0]))
            print(data[1])
            # array_sh.append(data[1])
            # candles_array.pop(0)
            return data[1],True
        else:
            return (), False
        
def getSwingLow(data):
    if(data[1][3] < data[0][3] and data[1][3] < data[2][3]):
        print("SIWNG LOW!!!")
        print(datetime.datetime.fromtimestamp(data[1][0]))
        print(data[1])
        # array_sl.append(data[1])
        # candles_array.pop(0)
        return data[1],True
    else:
        return (), False

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
        # print("Esperar rompimiento del sh")
        # print("array_ss: ",array_ss)
        return True
    return False

def handSecuenseSlSh(array):
    lenght = len(array)
    if(lenght > 1 and array[lenght - 1][0] == "sh" and array[lenght - 2][0] == "sl" ):
        # print("Esperar rompimiento del sl")
        # print("array_ss: ",array_ss)
        return True
    return False
def run():
    # loop principal. ejecucuión continua del script
    while ( True ):
        candle = getData(SYMBOL,TIMEFRAME)
        flag_candle_array = setCandleArray(candle)
        if ( flag_candle_array ):# control de nueva vela en el arreglo de 3
            if(len(candles_array) == 3):# control de 3 velas en el arreglo
                candle_sh, flag_sh = getSwingHigh(candles_array)
                candle_sl, flag_sl = getSwingLow(candles_array)
                if(flag_sh):
                    
                    aux_list = list(candle_sh)
                    aux_candle = ["sh"]

                    for e in aux_list:
                        aux_candle.append(e)
                    tup_candle = tuple(aux_candle)
                    array_ss.append(tup_candle)

                if(flag_sl):
                    
                    aux_list = list(candle_sl)
                    aux_candle = ["sl"]

                    for e in aux_list:
                        aux_candle.append(e)
                    tup_candle = tuple(aux_candle)
                    array_ss.append(tup_candle)

                candles_array.pop(0)
        flag_secuense_Sh = handSecuenseShSl(array_ss)
        flag_secuense_Sl = handSecuenseSlSh(array_ss)
        if(flag_secuense_Sh):
            lenght = len(candles_array)
            flag_bsh = breakingSwingHigh(candles_array[lenght - 1])
            if(flag_bsh):
                break
        if(flag_secuense_Sl):
            flag_bsl=breakingSwingLow(candles_array[lenght - 1])
            if(flag_bsl):
                break

if __name__ == "__main__":
    ##############################################
    ######## PARAMETROS DE LA ESTRATEGIA #########
    ##############################################
    SYMBOL = "AUDCAD"
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