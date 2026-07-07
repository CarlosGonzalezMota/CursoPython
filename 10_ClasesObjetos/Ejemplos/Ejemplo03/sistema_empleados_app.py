from Ejemplo03.empleado import Empleado
from Ejemplo03.empresa import Empresa

print('*** Sistema de Empleados ***')

# Creamos una instancia de una empresa
empresa1 = Empresa('Global Mentoring')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'RR.HH')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el nº de empleados en el dpt de ventas
print(f'Empleados en el departamento de Ventas: '
      f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')

# Mostrar todos los empleados de la empresa1
empresa1.obtener_total_empleados()