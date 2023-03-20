import pandas as pd




path = r'Supplier.xlsx'
df = pd.read_excel(path)
supplier = df.iloc[:, 1].tolist()
print(supplier)