import numpy as np

def read_ir(file_path):
    """
    Lee archivo .asc o .dpt del espectro IR.
    Devuelve arrays (x, y).
    """
    data = np.loadtxt(file_path)
    x = data[:, 0]
    y = data[:, 1]
    return x, y

def read_qms(file_path):
    """
    Lee archivo QMS (.dat) con cabecera de masas y columnas numéricas.
    Devuelve: tiempo (array), datos (2D array), lista de cabeceras.
    """
    with open(file_path, "r") as f:
        header = f.readline().split()
    data = np.loadtxt(file_path, skiprows=1)
    return data[:, 0], data, header