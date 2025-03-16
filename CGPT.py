import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

def load_and_clean_csv(file_path):
    # Probar diferentes separadores
    try:
        df = pd.read_csv(file_path, sep=',', parse_dates=True, index_col=0)
    except:
        df = pd.read_csv(file_path, sep=';', parse_dates=True, index_col=0)

    # Mostrar información preliminar
    print("\n--- Primeras filas del archivo ---\n")
    print(df.head())
    print("\n--- Información del DataFrame ---\n")
    print(df.info())

    # Convertir columnas a numéricas (forzar)
    df = df.apply(pd.to_numeric, errors='coerce')

    # Eliminar filas con NaN (datos faltantes)
    df.dropna(inplace=True)

    print("\n--- Datos después de limpieza ---\n")
    print(df.head())

    return df

def plot_stock_data(df, title="Stock Data", moving_average=None):
    style.use('ggplot')
    plt.figure(figsize=(12, 6))

    # Graficar columna Close si existe
    if 'Close' in df.columns:
        df['Close'].plot(label='Close Price')
    else:
        df.plot()  # Graficar todo si no hay 'Close'

    # Media móvil opcional
    if moving_average and 'Close' in df.columns:
        df[f'{moving_average}-MA'] = df['Close'].rolling(window=moving_average).mean()
        df[f'{moving_average}-MA'].plot(label=f'{moving_average}-Day MA')

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

### ---------- USO ---------- ###

file_path = 'MMM.csv'  # Cambia por cualquier archivo que tengas

df = load_and_clean_csv(file_path)
plot_stock_data(df, title="MMM Stock Data", moving_average=50)
