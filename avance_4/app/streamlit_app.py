import streamlit as st
import requests

st.set_page_config(page_title="Predicción de Pago", layout="centered")

st.title("Predicción de Estado de Pago")
st.write("Completa los datos para obtener una predicción.")

edad_cliente = st.number_input("Edad del cliente", min_value=18.0, value=35.0)
salario_cliente = st.number_input("Salario del cliente", min_value=0.0, value=500000.0)
cant_creditosvigentes = st.number_input("Cantidad de créditos vigentes", min_value=0.0, value=2.0)
total_otros_prestamos = st.number_input("Total otros préstamos", min_value=0.0, value=150000.0)
capital_prestado = st.number_input("Capital prestado", min_value=0.0, value=200000.0)
cuota_pactada = st.number_input("Cuota pactada", min_value=0.0, value=25000.0)
plazo_meses = st.number_input("Plazo en meses", min_value=1.0, value=12.0)
capacidad_pago = st.number_input("Capacidad de pago", min_value=0.0, value=0.45)
ratio_deuda = st.number_input("Ratio deuda", min_value=0.0, value=0.30)
ratio_credito_salario = st.number_input("Ratio crédito/salario", min_value=0.0, value=0.40)
tendencia_ingresos = st.number_input("Tendencia ingresos", value=1.0)
creditos_sectorReal = st.number_input("Créditos sector real", min_value=0.0, value=1.0)
creditos_sectorFinanciero = st.number_input("Créditos sector financiero", min_value=0.0, value=0.0)
creditos_sectorCooperativo = st.number_input("Créditos sector cooperativo", min_value=0.0, value=0.0)
tipo_credito = st.number_input("Tipo crédito (codificado)", min_value=0.0, value=1.0)
tipo_laboral = st.number_input("Tipo laboral (codificado)", min_value=0.0, value=1.0)

if st.button("Predecir"):
    payload = {
        "edad_cliente": edad_cliente,
        "salario_cliente": salario_cliente,
        "cant_creditosvigentes": cant_creditosvigentes,
        "total_otros_prestamos": total_otros_prestamos,
        "capital_prestado": capital_prestado,
        "cuota_pactada": cuota_pactada,
        "plazo_meses": plazo_meses,
        "capacidad_pago": capacidad_pago,
        "ratio_deuda": ratio_deuda,
        "ratio_credito_salario": ratio_credito_salario,
        "tendencia_ingresos": tendencia_ingresos,
        "creditos_sectorReal": creditos_sectorReal,
        "creditos_sectorFinanciero": creditos_sectorFinanciero,
        "creditos_sectorCooperativo": creditos_sectorCooperativo,
        "tipo_credito": tipo_credito,
        "tipo_laboral": tipo_laboral
    }

    try:
        response = requests.post("http://127.0.0.1:8010/predict", json=payload)

        if response.status_code == 200:
            resultado = response.json()["prediccion"]
            st.success(f"La predicción del modelo es: {resultado}")
        else:
            st.error(f"Error en la API: {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error(f"No se pudo conectar con la API: {e}")