import pandas as pd

df = pd.read_csv("out.csv")

productosDF = df[df["Rack"] == "S1"]

print(productosDF[productosDF["Producto"] == "PAPEL ENCERADO PERSONALIZADO (Paquete de 1 kg)"]["Cantidad"][0])