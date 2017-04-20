############## VERSAO SIMPLIFICADA #################

letras = ('A', 'B','C', 'D', 'E', 'F', 'G' ,'H', 'I', 'J', ' ', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', '.')

def gera_chave1(letras):
    result = []
    for i in range(0,25,5):
        result.append(letras[i:i+5])
        #print (result)
    return tuple(result)

chave = gera_chave1(letras)
#print(chave)

def obtem_codigo1(car,chave):
    for i,elem in enumerate(chave):
        if car in elem:
            return str(i) + str(elem.index(car))
    return ''

#print(obtem_codigo1('Q',chave))

def codifica1(cad,chave):
    result = ""
    for letra in cad:
        result += obtem_codigo1(letra,chave)
    return result

#print(codifica1('FUNDAMENTOS DA PROGRAMACAO',chave))

def obtem_car1(cod,chave):
    return chave[int(cod[0])][int(cod[1])]

#print(obtem_car1('31',chave))

def descodifica1(cad_codificada,chave):
    result = ""
    for i in range(int(len(cad_codificada)/2)):
        #print (cad_codificada[i*2:i*2+2])
        result += obtem_car1(cad_codificada[i*2:i*2+2],chave)
    return result

frase_cod = codifica1('FUNDAMENTOS DA PROGRAMACAO',chave)
#print(descodifica1(frase_cod,chave))

################ VERSAO FINAL #################

letras = ('A', 'B','C', 'D', 'E', 'F', 'G' ,'H', 'I', 'J', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z')

def raiz_menor_quadrado_perfeito(num):
    for i in range (1,100):
        if i*i >= num:
            return i
    return 'MENOR QUADRADO PERFEITO NAO ENCONTRADO'

#print(raiz_menor_quadrado_perfeito(25))

def gera_chaves2(letras):
    n_t = raiz_menor_quadrado_perfeito(len(letras))
    #print("n_tuplos = ",n_t)

    result = []
    for i in range(0, n_t*n_t -n_t, n_t):
        result.append(letras[i:i + 5])
    result.append(letras[n_t*n_t-n_t:])
    return tuple(result)

chave = gera_chaves2(letras)

def obtem_codigo2(car,chave):
    for i,elem in enumerate(chave):
        if car in elem:
            return str(i) + str(elem.index(car))
    return 'XX'

#print(chave)
#print(obtem_codigo2('Q',chave))
#print(obtem_codigo2(':',chave))

def codifica2(cad,chave):
    result = ""
    for letra in cad:
        result += obtem_codigo2(letra, chave)
    return result

#print(codifica2('FUNDAMENTOS DE PROGRAMACAO',chave))

def obtem_car2(cod,chave):
    return chave[int(cod[0])][int(cod[1])] if cod != 'XX' else '?'

#print(obtem_car2('31',chave))
#print(obtem_car2('XX',chave))

def descodifica2(cad_codificada,chave):
    result = ""
    for i in range(int(len(cad_codificada)/2)):
        #print (cad_codificada[i*2:i*2+2])
        result += obtem_car2(cad_codificada[i*2:i*2+2],chave)
    return result

frase_cod = codifica2('FUNDAMENTOS DA PROGRAMACAO',chave)
print(descodifica2(frase_cod,chave))

