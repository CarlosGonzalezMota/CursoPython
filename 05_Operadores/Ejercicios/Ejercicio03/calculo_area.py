print('*** Cálculo Área y Perímetro de un Rectángulo ***')

valor_base = float(input('Ingrese el valor base: '))
valor_altura= float(input('Ingrese el valor del área: '))

resultado_area = valor_base * valor_altura
print(f'El valor del área es de: {resultado_area:.2f}')

resultado_perimetro = 2 * (valor_base + valor_altura)
print(f'El valor del perimetro es de: {resultado_perimetro:.2f}')