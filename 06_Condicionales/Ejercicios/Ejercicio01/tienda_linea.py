print(f'*** Sistema de descuentos ***')

MONTO_COMPRA_DESC = 1000

compra_total = int(input('¿Cuál fue el monto de la compra? '))
es_miembro = input('¿Eres miembro de la tienda? (Si/no) ')

descuento = 0

es_miembro = es_miembro.strip().lower()

if compra_total >= MONTO_COMPRA_DESC and es_miembro == 'si':
    descuento = 0.1
elif compra_total < MONTO_COMPRA_DESC and es_miembro == 'si':
    descuento = .05
elif compra_total >= MONTO_COMPRA_DESC:
    descuento = .03
else:
    descuento = 0

if descuento != 0:
    compra_descuento = compra_total * descuento
    monto_final = compra_total - compra_descuento
    print(f'\n Felicidades, has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra: ${compra_total:.2f}')
    print(f'Monto del descuento: ${compra_descuento:.2f}')
    print(f'Monto final de la compra con descuento: ${monto_final:.2f}')
else:
    print('\nNo obtuviste ningún tipo de descuento')
    print(f'Monto de la compra: ${compra_total:.2f}')

#if compra_total >= MONTO_COMPRA_DESC and es_miembro == 'si':
#    subtotal_con_descuento = compra_total * 0.10
#    print(f'Felicidades, has obtenido un descuento del 10%')
#    print(f'Monto de la compra: ${compra_total:.2f}')
#    print(f'Monto del descuento: ${subtotal_con_descuento:.2f}')
#    print(f'Monto final de la compra con descuento: ${compra_total - subtotal_con_descuento:.2f}')
#elif compra_total < MONTO_COMPRA_DESC and es_miembro == 'si':
#    subtotal_con_descuento = compra_total * 0.05
#    print(f'Felicidades, has obtenido un descuento del 5%')
#    print(f'Monto de la compra: ${compra_total:.2f}')
#    print(f'Monto del descuento: ${subtotal_con_descuento:.2f}')
#    print(f'Monto final de la compra con descuento: ${compra_total - subtotal_con_descuento:.2f}')
#elif compra_total < MONTO_COMPRA_DESC and es_miembro == 'no':
#    print(f'No obtuviste ningún tipo de descuento')
#   print(f'Monto de la compra: ${compra_total:.2f}')