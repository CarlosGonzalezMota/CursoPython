print('*** Calculadora de impuestos ***')

def calcular_total_pago(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)

pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione la cantidad del impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)

print(f'Pago con impuesto: {pago_con_impuesto}')