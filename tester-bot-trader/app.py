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
    with open(ruta_6,"r") as file:
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

    pass

def handSecuenseShSl(array):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    lenght = len(array)
    if(lenght > 1 and array[lenght - 1][0] == "sl" and array[lenght - 2][0] == "sh" ):
        sl_l=array[lenght - 1][5]
        sh_h=array[lenght - 2][4]
        print(f"Dentro de handSecuenseShSl sh_h {sh_h} sl_l {sl_l}")
        return (True,sl_l,sh_h)
    return (False,0,0)

def handSecuenseSlSh(array):
    """
    hay que tener en cuenta que los datos de prueba varían
    a los datos reales, puesto que los de prueba tienen un campo mas
    se deben ajustar las posiciones el pasar de back-testing a producción
    """
    lenght = len(array)
    if(lenght > 1 and array[lenght - 1][0] == "sh" and array[lenght - 2][0] == "sl" ):
        sl_l=array[lenght - 2][5]
        sh_h=array[lenght - 1][4]
        print(f"Dentro de handSecuenseSlSh sh_h {sh_h} sl_l {sl_l}")
        return (True,sl_l,sh_h)
    return (False,0,0)

def handWaitForBreak(ss1,ss2,sl_l,sh_h,candles,i_list_candles,candles_array,array_ss):
    candles_array = candles_array
    array_ss = array_ss
    print("Esperando el primer rompimiento o un nuevo swing (sh o sl)")
    flag = True
    while(flag):
        candle, i_list_candles= getCandle(candles,i_list_candles)
        flag_candles_array,candles_array = setCandlesArray(candle,candles_array)
        if ( flag_candles_array and len(candles_array) == 3):
            candle_sh, flag_sh = getSwingHigh(candles_array)
            candle_sl, flag_sl = getSwingLow(candles_array)
            if(flag_sh):
                array_ss = handSetArraySS("sh",candle_sh,array_ss)
            if(flag_sl):
                array_ss = handSetArraySS("sl",candle_sl,array_ss)
            if(flag_sh or flag_sl):
                print("hubo un cambio en los swings")
                
                candles_array.pop(0)
                flag = False
                return True, False, candles, i_list_candles, candles_array, array_ss
            candles_array.pop(0)
        pass
    pass

def run():
    i_list_candles = 0
    candles_array = []
    array_ss = []
    array_break=[]
    candles_all = getListCandles()
    sh_b = "0"
    sl_b = "0"
    i = 0
    while i < len(candles_all):
        if i == 19:
            pass
        candle, i_list_candles= getCandle(candles_all,i_list_candles)
        flag_candles_array,candles_array = setCandlesArray(candle,candles_array)
        if (flag_candles_array and (len(candles_array) == 3 or len(candles_array) == 4 or len(candles_array) == 5)):
            candle_sh, flag_sh, flag_sh_2 = getSwingHigh(candles_array)
            candle_sl, flag_sl, flag_sl_2 = getSwingLow(candles_array)
            if(flag_sh):
                array_ss = handSetArraySS("sh",candle_sh,array_ss)
            if(flag_sl):
                array_ss = handSetArraySS("sl",candle_sl,array_ss)
            (flag_secuense_Sh, sl_l, sh_h) = handSecuenseShSl(array_ss)
            if(flag_secuense_Sh and candles_array[2][3] > sh_h):#candles_array[2][3] --> high ult. vela
                print("primer rompimiento -- rompimiento en el high")
                print("vela que rompió")
                print(candles_array[2])
                sh_b = sh_h
                sl_b = sl_l
                print(f"sh_b {sh_b};  sl_b {sl_b}")
                aux = {
                    "sh_b":sh_b,
                    "sl_b":sl_b,
                    "wait":"low"
                }
                if len(array_break) == 0:
                    array_break.append(aux)
                else:
                    array_break.pop(0)
                    array_break.append(aux)
                pass
                # if(candles_array[2][5] < sl_b):#candles_array[2][4] --> closed ult. vela
                #     for e in array_ss:
                #         print(e)
                #     print("segundo rompimiento -- rompiendo el low")
                #     print(f"swing low a romper con cuerpo {sl_b}")
                #     print("vela que rompe ese valor ")
                #     print(candles_array[2])
                #     print(f"cierre de la vela {candles_array[2][5]}")
                #     print("Enviar orden -- 1 !!!")
                #     break
            (flag_secuense_Sl, sl_l, sh_h) = handSecuenseSlSh(array_ss)
            if(flag_secuense_Sl and candles_array[2][4] < sl_l):
                print("primer rompimiento -- rompimiento en el low")
                print("vela que rompió")
                print(candles_array[2])
                sh_b = sh_h
                sl_b = sl_l
                print(f"sh_b {sh_b};  sl_b {sl_b}")
                aux = {
                    "sh_b":sh_b,
                    "sl_b":sl_b,
                    "wait":"high"
                }
                if len(array_break) == 0:
                    array_break.append(aux)
                else:
                    array_break.pop(0)
                    array_break.append(aux)
                pass
                # if(candles_array[2][5] > sh_b):
                #     for e in array_ss:
                #         print(e)
                #     print("segundo rompimiento -- rompiendo el high")
                #     print(f"swing high a romper con cuerpo {sh_b}")
                #     print("vela que rompe ese valor ")
                #     print(candles_array[2])
                #     print(f"cierre de la vela {candles_array[2][5]}")
                #     print("Enviar orden  -- 2 !!!")
                #     break
            if len(array_break) != 0:
                if array_break[0]["wait"] == "high":
                    if(candles_array[2][5] > sh_b):
                        for e in array_ss:
                            print(e)
                        print("segundo rompimiento -- rompiendo el high")
                        print(f"swing high a romper con cuerpo {sh_b}")
                        print("vela que rompe ese valor ")
                        print(candles_array[2])
                        print(f"cierre de la vela {candles_array[2][5]}")
                        print("Enviar orden  -- 2 !!!")
                        break
                if array_break[0]["wait"] == "low":
                    if(candles_array[2][5] < sl_b):#candles_array[2][4] --> closed ult. vela
                        for e in array_ss:
                            print(e)
                        print("segundo rompimiento -- rompiendo el low")
                        print(f"swing low a romper con cuerpo {sl_b}")
                        print("vela que rompe ese valor ")
                        print(candles_array[2])
                        print(f"cierre de la vela {candles_array[2][5]}")
                        print("Enviar orden -- 1 !!!")
                        break
            if( not (flag_sh_2 or flag_sl_2) ):
                # print(candles_array)
                candles_array.pop(0)
                # print("ultimo candles array")
                # print(candles_array)
        i = i + 1
    print("##########################################")
    print("########## fin de la ejecución ###########")
    print("##########################################")
    
    print("array_ss")
    for e in array_ss:
        print(e)
    print(f"sh_b {sh_b};  sl_b {sl_b}")
        
        
        
        
        

if __name__ == "__main__":
    
    run()