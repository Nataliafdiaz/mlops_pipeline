import pandas as pd
from pathlib import Path

# Ruta raíz del proyecto
root_path = Path(__file__).resolve().parents[2]

# Archivo Excel original
input_file = root_path / "Base_de_datos.xlsx"

# Carpeta de salida
output_dir = root_path / "avance_3" / "data"
output_dir.mkdir(parents=True, exist_ok=True)

# Leer Excel
df = pd.read_excel(input_file)

# Eliminar filas completamente vacías
df = df.dropna(how="all").copy()

# Separar en dos partes
reference_df = df.sample(frac=0.7, random_state=42).copy()
current_df = df.drop(reference_df.index).copy()

# Guardar como CSV
reference_df.to_csv(output_dir / "referencia.csv", index=False)
current_df.to_csv(output_dir / "actual.csv", index=False)

print("Archivos generados correctamente:")
print(output_dir / "referencia.csv")
print(output_dir / "actual.csv")
print("Tamaño referencia:", reference_df.shape)
print("Tamaño actual:", current_df.shape)