# -*- coding: utf-8 -*-
from bpp_operaciones import es_primo

if __name__ == '__main__':
        print(list(filter(es_primo, [3, 4, 8, 5, 5, 22, 13])))
    