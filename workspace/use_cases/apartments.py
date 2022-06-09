import matplotlib.pyplot as plt
import seaborn as sns

from src import load_apartments

apartments = load_apartments()

apartments['Year & month'] = apartments['Date'].dt.strftime('%Y-%m')
m = apartments.groupby(['Year & month'])['Price'].median()
print(m.index, m.values)


sns.scatterplot(data=apartments, x="Date", y="Price")
plt.show()
sns.barplot(x=m.index, y=m.values, data=m)
plt.show()
