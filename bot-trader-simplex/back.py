import MetaTrader5 as mt5
import app as app

##############################################
############# VARIABLES GLOBALES #############
##############################################

array_sh = []
array_sl = []
candles_array = []
#DIFERENCE = 0
# candles_array = []

##############################################

def getData(symbol, timeframe):

    # Display dataframe with data
    #         time     open     high      low    close  tick_volume  spread  real_volume
    # 0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            0
    # 1 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            0
    # 2 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            0
    # 3 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            0
    
    data = mt5.copy_rates_from_pos(symbol, timeframe, 0, 96)#ultima barra
    # print(data[0][0]) 
    # for row in data:
    #     print(row)
    return data

def toSwing(data):
    i = 0
    while( i < len(data) ):
        print("iteracion: ",i)
        if( i < 3 ):
            candles_array.append(data[i])            
        else:
            #print("tamaño candles_array ",len(candles_array))
            candle_sh, flag_sh = app.getSwingHigh(candles_array)
            candle_sl, flag_sl = app.getSwingLow(candles_array)
            if(flag_sh):
                array_sh.append(candle_sh)
                app.breakingSwingHigh(array_sh)
            if(flag_sl):
                array_sl.append(candle_sl)
            
            candles_array.pop(0)
            candles_array.append(data[i])
        i += 1
    # print("iterador: ", i)
    # print("comparison_candles_array ", comparison_candles_array)
    # print("data[29] ", data[29])
    # print("array_sh \n",array_sh)

def run():
    

    candle_data = getData(SYMBOL,TIMEFRAME)
    toSwing(candle_data)
    
    pass

if(__name__ == "__main__"):

    ##############################################
    ######## PARAMETROS DE LA ESTRATEGIA #########
    ##############################################
    SYMBOL = "AUDCAD"
    VOLUME = 1.0
    TIMEFRAME = mt5.TIMEFRAME_M2
    DIFERENCE = 60*15
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
    pass