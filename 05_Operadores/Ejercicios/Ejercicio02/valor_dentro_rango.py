print('*** Valor Dentro de Rango ***')

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_ingresado = int(input(f'Ingrese un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

resultado_ingresado = VALOR_MINIMO <= valor_ingresado <= VALOR_MAXIMO # Se valida si valor_ingresado >= VALOR_MINIMO y VALOR_MAXIMO <= valor_ingresado
#resultado_ingresado = valor_ingresado >= VALOR_MINIMO and valor_ingresado <= VALOR_MAXIMO
print(f'¿El valor ingresado se encuentra dentro del rango?: {resultado_ingresado}')