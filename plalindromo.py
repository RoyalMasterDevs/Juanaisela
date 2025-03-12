
text1 = input("ingrese una palabra palindroo")
text1= input("i")

def palindromo(text):
    reverse =str(text).lower().replace(' ',' ') #convierte la palabra en mayuscula# 
    print(reverse[::-1])
    if reverse == reverse[::-1]:
        return True
    else:
        return False
        
                
print(palindromo(text1))




#algoritmo
#1 pide una palabra
#2 invierte la palabra
#3 verifica la comparacion
#4 si es igual , muetra true
#5 si no es igual, muestra False
#6 fin ####
# primer cambio ##
#se cambia texto a texto1 ejemplo de testing#