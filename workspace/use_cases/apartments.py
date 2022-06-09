from src import load_apartments, generate_regression_problem

apartments = load_apartments()

apartments['Year & month'] = apartments['Date'].dt.strftime('%Y-%m')
m = apartments.groupby(['Year & month'])['Price'].median()
print(m.index, m.values)
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=apartments, x="Date", y="Price")
plt.show()
sns.barplot(x=m.index, y=m.values, data=m)
plt.show()
