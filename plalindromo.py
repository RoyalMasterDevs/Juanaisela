
text = input("ingrese una palabra")

def palindromo(text):
    reverse =str(text).lower().replace(' ',' ') #convierte la palabra en mayuscula# 
    print(reverse[::-1])
    if reverse == reverse[::-1]:
        return True
    else:
        return False
        
print(palindromo(text))




#algoritmo
#1 pide una palabra
#2 invierte la palabra
#3 verifica la comparacion
#4 si es igual , muetra true
#5 si no es igual, muestra False
#6 fin #