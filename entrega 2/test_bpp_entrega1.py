# -*- coding: utf-8 -*-
import pytest
import numbers
import pandas as pd
from funciones import *
test_file = 'finanzas2020[1].csv'
datos = ''

def test_load_data():
    
    global datos
    datos = load_data(test_file)


def test_gastos():
    
    aux1 = lambda d: isinstance(d[0], numbers.Number) and d[0] <= 0 # is series to get the name 
    aux2 = lambda d: isinstance(d, numbers.Number) and d <= 0
    aux3 = lambda d: isinstance(d, pd.Series) and len(d) == 12
    entries = ['min', 'total', 'mean', '', None]
    expected = [aux1, aux2, aux2, aux3, lambda d: d is None]
    
    for x, fun in zip(entries, expected):
        
        assert fun(get_gasto(datos, x))
    
def test_ingresos():
    
    aux1 = lambda d: isinstance(d[0], numbers.Number) and d[0] >= 0 # is series to get the name 
    aux2 = lambda d: isinstance(d, numbers.Number) and d >= 0
    aux3 = lambda d: isinstance(d, pd.Series) and len(d) == 12
    entries = ['max', 'total', 'mean', '', None]
    expected = [aux1, aux2, aux2, aux3, lambda d: d is None]
    
    for x, fun in zip(entries, expected):
        
        assert fun(get_ingreso(datos, x))
        
def test_ahorros():
    
    aux1 = lambda d: isinstance(d[0], numbers.Number) # is series to get the name 
    aux2 = lambda d: isinstance(d, numbers.Number)
    aux3 = lambda d: isinstance(d, pd.Series) and len(d) == 12
    entries = ['max', 'min', 'total', 'mean', '', None]
    expected = [aux1, aux1, aux2, aux2, aux3, lambda d: d is None]
    
    for x, fun in zip(entries, expected):
        
        assert fun(get_ahorro(datos, x))