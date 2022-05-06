# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Intenta abrir el fichero de Datos
try:
    
    datos = pd.read_csv('finanzas2020[1].csv', sep = '\t')
    
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
                    
# Cálculos

# mes que mas se ha gastado
auxGasto = datos[datos <= 0]
auxGasto = auxGasto.sum()
gasto = abs(auxGasto[lambda d: d == min(auxGasto)])
print(f'Se ha gastado mas en {gasto.index[0]} ({gasto[0]:.0f})')

# total gastos
totalGasto = abs(auxGasto.sum())
print(f'Se ha gastado {totalGasto:.0f} en total')

# media gastos
meanGasto = abs(auxGasto.mean())
print(f'Se ha gastado {meanGasto:.0f} de media')


# mes que mas se ha ingresado
auxIngreso = datos[datos >= 0]
auxIngreso = auxIngreso.sum()
ingreso = auxIngreso[lambda d: d == max(auxIngreso)]
print(f'Se ha ingresado mas en {ingreso.index[0]} ({ingreso[0]:.0f})')

# totalGastos
totalIngreso = abs(auxIngreso.sum())
print(f'Se ha ingresado {totalIngreso:.0f} en total')

# mes que mas se ha ahorrado
auxAhorro = auxGasto + auxIngreso
ahorro = auxAhorro[lambda d: d == max(auxAhorro)]
print(f'Se ha ahorrado mas en {ahorro.index[0]} ({ahorro[0]:.0f})')

auxIngreso.plot()
plt.show()