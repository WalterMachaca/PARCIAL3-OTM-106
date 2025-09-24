import pandas as pd
from matplotlib import pyplot as plt
import os

#Crear carpeta de salida
os.makedirs("Generados",exist_ok=True)

#Leer archivo excel
archivo_excel="DATOS/ejemplo.xlsx"

# Definir las hojas por tipo
hojas_barras = ["BARRAS1", "BARRAS2", "BARRAS3"]
hojas_pastel = ["PASTEL1", "PASTEL2", "PASTEL3"]

# Gráfico de barras 
for hoja in hojas_barras:
    data_hoja = pd.read_excel(archivo_excel, sheet_name=hoja, engine="openpyxl")
    print(f"Datos leídos de la hoja {hoja}")
    
    eje_x = data_hoja.iloc[:, 0]  
    eje_y = data_hoja.iloc[:, 1] 
          
        
    fig, ax = plt.subplots()
    ax.bar(eje_x, eje_y, color="orange", label=f"Datos de {hoja}")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_xticks(range(len(eje_x)))
    ax.set_xticklabels(eje_x, rotation=45)
    ax.set_title(f"Gráfica de {hoja}(barras)")
    fig.savefig(f"Generados/grafica_{hoja}.png", bbox_inches="tight")
    plt.close(fig)
    
# Gráfico de pastel   
for hoja in hojas_pastel: 
    data_hoja= pd.read_excel(archivo_excel, sheet_name=hoja, engine="openpyxl")
    print(f"Datos leídos de la hoja {hoja}") 
    
    eje_x = data_hoja.iloc[:, 0]  
    eje_y = data_hoja.iloc[:, 1]
        
    fig, ax = plt.subplots()
    ax.pie(eje_y, labels=eje_x,autopct="%1.1f%%", startangle=90)
    ax.set_title(f"Gráfica de {hoja}(pastel)")
    fig.savefig(f"Generados/grafica_{hoja}.png", bbox_inches="tight")
    plt.close(fig)
    
    
print("Gráficas generadas y guardadas en la carpeta 'Generados'.")