# -*- coding: utf-8 -*-
"""Modulo con operaciones de finanzas"""
import pandas as pd
import matplotlib.pyplot as plt

# Intenta abrir el fichero de Datos
def load_data(file):
    """Se encarga de abrir el archivo de datos 'file' 
    y devuelve una referencia a el si lo consigue"""
    try:
        
        datos = pd.read_csv(file, sep = '\t')
        
    except Exception as e:
        
       print('No se puede abrir el fichero de datos: ' + str(e))
       
       
    else:
         # comprueba que hay 12 meses
        assert(len(datos.columns) == 12)
        
        # comprueba los datos
        for c in datos.columns:
            
            assert(len(datos[c]) > 0)
            
            for r in datos.index:
                try:
                    datos.at[r, c] = int(datos.at[r, c])
                    
               
                except ValueError:
                    try:
                        datos.at[r, c] = int(datos.at[r, c].replace("'", ""))
                    
                    except ValueError:
                        datos.at[r, c] = float('NaN')
    return datos
                    
def get_gasto(datos, opt = ''):
    """Con los datos de finzanzas del archivo 'datos' devuelve información
    relativa a los gastos. Opciones = [min, total, mean, '']"""
    auxGasto = datos[datos <= 0]
    auxGasto = auxGasto.sum()
    if opt == 'min': # mes que mas se ha gastado
        return auxGasto[lambda d: d == min(auxGasto)]
    
    elif opt == 'total': # total gastos
        return auxGasto.sum()
    
    elif opt == 'mean': # media gastos
        return auxGasto.mean()
        
    elif opt == '': #gastos de cada mes
        return auxGasto
    
    print('Opcion no valida')

def get_ingreso(datos, opt = ''):
    """Con los datos de finzanzas del archivo 'datos' devuelve información
    relativa a los ingresos. Opciones = [max, total, mean, '']"""
    auxIngreso = datos[datos >= 0]
    auxIngreso = auxIngreso.sum()
    if opt == 'max': # mes que mas se ha ingresado
        return auxIngreso[lambda d: d == max(auxIngreso)]
    
    elif opt == 'total': # total ingresos
        return auxIngreso.sum()
    
    elif opt == 'mean': # media ingresos
        return auxIngreso.mean()
        
    elif opt == '': #ingresos de cada mes
        return auxIngreso
    
    print('Opcion no valida')

def get_ahorro(datos, opt = ''):
    """Con los datos de finzanzas del archivo 'datos' devuelve información
    relativa al ahorro. Opciones = [min, max, total, mean, '']"""
    auxAhorro = get_gasto(datos) + get_ingreso(datos)
    if opt == 'max': # mes que mas se ha ahorrado
        return auxAhorro[lambda d: d == max(auxAhorro)]
    
    elif opt == 'min': # mes que menos se ha ahorrado
        return auxAhorro[lambda d: d == min(auxAhorro)]
    
    elif opt == 'total': # total ahorro
        return auxAhorro.sum()
    
    elif opt== 'mean': # media ahorro
        return auxAhorro.mean()
        
    elif opt == '': #ahorro de cada mes
        return auxAhorro
    
    print('Opcion no valida')

if __name__ == '__main__':
    datos = load_data('finanzas2020[1].csv')
    
    gasto = abs(get_gasto(datos, 'min'))
    print(f'Se ha gastado mas en {gasto.index[0]} ({gasto[0]:.0f})')
    
    totalGasto = abs(get_gasto(datos, 'total'))
    print(f'Se ha gastado {totalGasto:.0f} en total')
    
    meanGasto = abs(get_gasto(datos, 'mean'))
    print(f'Se ha gastado {meanGasto:.0f} de media')
    
    ingreso = get_ingreso(datos, 'max')
    print(f'Se ha ingresado mas en {ingreso.index[0]} ({ingreso[0]:.0f})')
    
    totalIngreso = get_ingreso(datos, 'total')
    print(f'Se ha ingresado {totalIngreso:.0f} en total')
    
    ahorro = get_ahorro(datos, opt = 'max')
    print(f'Se ha ahorrado mas en {ahorro.index[0]} ({ahorro[0]:.0f})')
    
    get_ingreso(datos).plot()
    plt.show()