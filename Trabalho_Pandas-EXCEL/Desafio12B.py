import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_excel('desafio12_B.xlsx')
mediadistancia = dataframe['Distancia'].mean()
dpdistancia = dataframe['Distancia'].std()
mediaborg = dataframe['Borg'].mean()
dpborg = dataframe['Borg'].std()

dataframe.hist(column='Borg', bins=10) #para ver se é normal
plt.show() #sim é normal

#18 - sim existe .. o grupo distancia esta bem acima em questao de valores
import numpy as np
x = dataframe['Borg']
y = dataframe['Estatura']
print(x,y)
mod_linear = np.polyfit(x, y, 1)

a = float(mod_linear[0])
b = float(mod_linear[1])

y_mod = a * x + b

import matplotlib.pyplot as plt
plt.plot(x,y, "o", label = "pontos experimentais")
plt.plot(x,y_mod, "-r", label = "modelo")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ajuste de uma reta")
plt.legend()
plt.show()