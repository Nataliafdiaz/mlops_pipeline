import pandas as pd
from pathlib import Path

# Rutas
root_path = Path(__file__).resolve().parents[2]

reference_path = root_path / "avance_3" / "data" / "referencia.csv"
current_path = root_path / "avance_3" / "data" / "actual.csv"
output_path = root_path / "avance_3" / "reports" / "drift_summary.csv"

# Cargar datos
reference_df = pd.read_csv(reference_path)
current_df = pd.read_csv(current_path)

results = []

for col in reference_df.columns:
    if col not in current_df.columns:
        continue

    ref_col = reference_df[col].dropna()
    cur_col = current_df[col].dropna()

    # Variables numéricas
    if pd.api.types.is_numeric_dtype(ref_col):
        ref_mean = ref_col.mean()
        cur_mean = cur_col.mean()

        if ref_mean != 0:
            drift_score = abs(cur_mean - ref_mean) / abs(ref_mean)
        else:
            drift_score = 0

        drift_detected = "Sí" if drift_score > 0.10 else "No"

        results.append({
            "columna": col,
            "tipo": "numérica",
            "media_referencia": round(ref_mean, 4),
            "media_actual": round(cur_mean, 4),
            "drift_score": round(drift_score, 4),
            "drift_detectado": drift_detected
        })

    # Variables categóricas
    else:
        ref_dist = ref_col.astype(str).value_counts(normalize=True)
        cur_dist = cur_col.astype(str).value_counts(normalize=True)

        categorias = set(ref_dist.index).union(set(cur_dist.index))
        max_diff = 0

        for cat in categorias:
            ref_prop = ref_dist.get(cat, 0)
            cur_prop = cur_dist.get(cat, 0)
            diff = abs(ref_prop - cur_prop)
            if diff > max_diff:
                max_diff = diff

        drift_detected = "Sí" if max_diff > 0.10 else "No"

        results.append({
            "columna": col,
            "tipo": "categórica",
            "media_referencia": "",
            "media_actual": "",
            "drift_score": round(max_diff, 4),
            "drift_detectado": drift_detected
        })

results_df = pd.DataFrame(results)
results_df.to_csv(output_path, index=False, encoding="utf-8-sig")

print("Resumen de drift generado correctamente en:")
print(output_path)
print(results_df)