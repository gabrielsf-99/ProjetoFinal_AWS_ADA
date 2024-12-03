import boto3
import random
import io

numero_aleatorio = random.randint(1,100)
lista_numeros = list(range (1,numero_aleatorio+1))

arquivo_txt = io.StringIO()

for numero in lista_numeros:
    arquivo_txt.write(f'{numero}\n')

arquivo_final = arquivo_txt.getvalue()
arquivo_txt.close()

print (arquivo_final)
