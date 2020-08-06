import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### Dataset que vamos a utilizar en formato csv
dataset = pd.read_csv("nombre_del_dataset.csv")

###Cómo obtener información del dataset, descomentar para visualizarlo o hacerlo en un script a parte
#print(surveys_df.head())
#print(surveys_df.dtypes)
#print(surveys_df.columns)

### Una vez tenemos los datos del dataset.
### Array con la columna de datos que nos interese
base = pd.unique(dataset['columna'])

### Array vacío para añadir el primer dígito de cada elemento de la columna
simple = []

### Recorremos la columna que hemos elegido, seleccionamos sólo el primer dígito y lo añadimos a nuestro nuevo array
for i in base:
	num = int(str(i)[0])
	simple.append(num)

### Info a mostrar
# Total de elementos en la columna
total = len(simple)
print("Total=",total)

# Lley de Benford para esa columna, guardando info para la gráfica
grafica = []
repeticion = 1
while repeticion <= 9:
	grafica.append(float("{0:.2f}".format(simple.count(repeticion)*100/total)))
	print(repeticion,("{0:.2f}".format(simple.count(repeticion)*100/total),"%"))
	repeticion = repeticion + 1

### Gráfica
numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
y_pos = np.arange(len(numeros))

plt.bar(y_pos, grafica, align='center', alpha=0.5)
plt.xticks(y_pos, numeros)
plt.ylabel('Veces')
plt.xlabel('contacta@noguerad.es')
plt.title('Ley de Benford para datasets')
plt.show()

