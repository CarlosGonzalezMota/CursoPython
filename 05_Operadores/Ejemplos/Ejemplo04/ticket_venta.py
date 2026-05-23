print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga =  float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platanos: '))
descuento_porcentaje = int(input('Aplicar algún descuento (%)? '))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje / 100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Cálculo con impuestos (%4)
impuesto = subtotal_con_descuento * 0.04

# Cálculo total de la compra (con impuestos)
coste_total_compra = subtotal_con_descuento + impuesto
print(f'''
    Subtotal: ${subtotal:.2f}
    Descuento: ${descuento:.2f}
    Sutotal con descuento: ${subtotal_con_descuento:.2f}
    Impuesto (4%): ${impuesto:.2f}
    Coste total de la compra: ${coste_total_compra:.2f} 
''')