def  dividendo(n):
    def divisor(int):
        assert type(int),'solo integer'
        return n/int
    return divisor

dividir185= dividendo(185)
dividir1440= dividendo(1440)
print('185 entre 5 esta ',dividir185(5), ' veces')
print('1440/48 es igual a ',dividir1440(48), ' unds')



