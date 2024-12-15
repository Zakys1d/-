import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("merged_data.csv")

# df['Operating System'].value_counts().plot(kind='pie')

# df['Genre'].value_counts().plot(kind= 'bar')

# df['Original Price'] = df['Original Price'].replace("$","")

#df['All Reviews Summary'].value_counts().plot(kind='pie')



# Побудова графіка
# df.plot(kind='scatter', x='Trip_Distance_km', y='Trip_Price', figsize=(8, 6), color='green', alpha=0.7)
# plt.title('Залежність ціни від відстані', fontsize=14)
# plt.xlabel('Відстань (км)', fontsize=12)
# plt.ylabel('Ціна (грн)', fontsize=12)
# plt.show()

plt.show()