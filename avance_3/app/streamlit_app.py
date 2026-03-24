import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Sistema de Monitoreo de Data Drift", layout="wide")

# Título principal
st.title("Sistema de Monitoreo de Data Drift")
st.markdown("Monitoreo comparativo entre dataset de referencia y dataset actual para detectar cambios relevantes en las variables.")

# Ruta del archivo resumen
root_path = Path(__file__).resolve().parents[2]
file_path = root_path / "avance_3" / "reports" / "drift_summary.csv"

# Sidebar
st.sidebar.header("Opciones de monitoreo")
mostrar_solo_drift = st.sidebar.checkbox("Mostrar solo variables con drift")
ordenar_por_score = st.sidebar.checkbox("Ordenar por mayor drift score")
mostrar_top = st.sidebar.slider("Top variables con mayor drift", min_value=3, max_value=10, value=5)

# Cargar datos
if file_path.exists():
    df = pd.read_csv(file_path)

    total = len(df)
    con_drift = len(df[df["drift_detectado"] == "Sí"])
    sin_drift = len(df[df["drift_detectado"] == "No"])

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("Variables totales", total)
    col2.metric("Variables con drift", con_drift)
    col3.metric("Variables sin drift", sin_drift)

    st.markdown("---")

    # Explicación
    with st.expander("¿Qué significa este análisis?"):
        st.write("""
        Este monitoreo compara un dataset de referencia con un dataset actual.
        El objetivo es identificar cambios en el comportamiento de las variables.
        
        - En variables numéricas se comparó la media.
        - En variables categóricas se comparó la distribución proporcional.
        - Se considera drift cuando el cambio supera el 10%.
        """)

    # Preparar datos para visualización
    df_vista = df.copy()

    if mostrar_solo_drift:
        df_vista = df_vista[df_vista["drift_detectado"] == "Sí"]

    if ordenar_por_score:
        df_vista = df_vista.sort_values(by="drift_score", ascending=False)

    st.subheader("Tabla de resultados")
    st.dataframe(df_vista, width="stretch")

    st.markdown("---")

    # Top variables con mayor drift
    st.subheader("Top variables con mayor drift score")
    top_drift = df.sort_values(by="drift_score", ascending=False).head(mostrar_top)

    st.bar_chart(
        top_drift.set_index("columna")["drift_score"]
    )

    st.markdown("---")

    # Hallazgos principales
    st.subheader("Hallazgos principales")

    variables_drift = df[df["drift_detectado"] == "Sí"]["columna"].tolist()

    if con_drift > 0:
        st.warning(f"""
Se detectaron {con_drift} variables con drift.

Esto indica que existen cambios entre los datos actuales y los datos de referencia.
Las variables más sensibles deben revisarse antes de utilizar el modelo en producción.
""")

        st.write("**Variables con drift detectado:**")
        for var in variables_drift:
            st.write(f"- {var}")

    else:
        st.success("No se detectó drift significativo. Los datos actuales mantienen un comportamiento similar al dataset de referencia.")

    st.markdown("---")

    # Conclusión final
    with st.expander("Conclusión del monitoreo"):
        st.write("""
        El análisis realizado permite anticipar posibles desvíos en los datos antes de que impacten el rendimiento del modelo.
        Este tipo de monitoreo es importante dentro de un flujo de MLOps porque ayuda a detectar cambios en producción y decidir si es necesario reentrenar, ajustar o revisar el modelo.
        """)

else:
    st.error("No se encontró el archivo drift_summary.csv. Ejecuta primero el script drift.py.")