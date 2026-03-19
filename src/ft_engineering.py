import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


def create_financial_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea variables derivadas financieras.
    """
    df = df.copy()

    df["ratio_deuda"] = df["total_otros_prestamos"] / (df["salario_cliente"] + 1)
    df["capacidad_pago"] = df["salario_cliente"] - df["cuota_pactada"]
    df["ratio_credito_salario"] = df["capital_prestado"] / (df["salario_cliente"] + 1)

    return df


def remove_high_corr_leakage(
    df: pd.DataFrame,
    target_col: str,
    threshold: float = 0.9
) -> tuple[pd.DataFrame, list[str]]:
    """
    Elimina variables numéricas con alta correlación respecto al target.
    """
    df = df.copy()

    corr_target = df.corr(numeric_only=True)[target_col]
    leakage_cols = corr_target[abs(corr_target) > threshold].index.tolist()

    if target_col in leakage_cols:
        leakage_cols.remove(target_col)

    df = df.drop(columns=leakage_cols, errors="ignore")

    return df, leakage_cols


def drop_datetime_columns(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    datetime_cols: list[str] | None = None
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Elimina columnas datetime de train y test.
    """
    X_train = X_train.copy()
    X_test = X_test.copy()

    if datetime_cols is None:
        datetime_cols = X_train.select_dtypes(include=["datetime64[ns]"]).columns.tolist()

    X_train = X_train.drop(columns=datetime_cols, errors="ignore")
    X_test = X_test.drop(columns=datetime_cols, errors="ignore")

    return X_train, X_test


def get_feature_types(X_train: pd.DataFrame) -> tuple[list[str], list[str]]:
    """
    Devuelve listas de variables numéricas y categóricas.
    """
    numeric_features = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X_train.select_dtypes(include=["object"]).columns.tolist()

    return numeric_features, categorical_features


def cast_categorical_to_string(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    categorical_features: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Convierte columnas categóricas a string para evitar errores con OneHotEncoder.
    """
    X_train = X_train.copy()
    X_test = X_test.copy()

    for col in categorical_features:
        X_train[col] = X_train[col].astype(str)
        X_test[col] = X_test[col].astype(str)

    return X_train, X_test


def build_preprocessor(
    numeric_features: list[str],
    categorical_features: list[str]
) -> ColumnTransformer:
    """
    Construye el pipeline de preprocesamiento.
    """
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    return preprocessor