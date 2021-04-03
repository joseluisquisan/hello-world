def run():
   mi_dic = {
       'a' : 1000,
       'b' : 2000,
       'c' : 3000,
   }
   poblacion_paises = {
        'Venezuela' : 1000000,
        'Chile' : 2000000,
        'Colombia' : 300000,
        'Argentina' : 500000,
   }

   for pais in poblacion_paises.keys():
       print(pais)
   
   for pais in poblacion_paises.values():
       print(pais)

   for pais, poblacion in poblacion_paises.items():
       print('El pais ' + pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()