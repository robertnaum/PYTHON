import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name='Data')


days = data["Days"]
cars = data["Cars on Street"]

plt.figure()
plt.plot(days,cars)
plt.title("My Plot")
plt.show()




