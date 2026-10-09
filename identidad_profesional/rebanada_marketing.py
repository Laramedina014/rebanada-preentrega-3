import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def ejecutar_rebanada():
    # Obtiene la ruta absoluta de la carpeta donde vive este script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_datos = os.path.join(directorio_actual, "marketing_campaign.csv")

    # Verificación de existencia del archivo
    if not os.path.exists(archivo_datos):
        print(f"Error: No se encontró el archivo en '{archivo_datos}'.")
        print(
            "Verificá que el archivo marketing_campaign.csv esté adentro de la carpeta 'identidad_profesional'."
        )
        return

    print("1. Cargando dataset...")
    df = pd.read_csv(archivo_datos, sep="\t")
    print(f"Dataset cargado con éxito: {df.shape[0]} filas y {df.shape[1]} columnas.")

    # Rebanada delgada (JBGE)
    df_clean = df.dropna(subset=["Income"]).copy()
    columnas_foco = ["Income", "MntWines", "MntMeatProducts", "Response"]
    df_slice = df_clean[columnas_foco]

    # Métricas de negocio
    print("\n2. Calculando métricas de negocio agrupadas...")
    metricas = (
        df_slice.groupby("Response")
        .agg(
            ingreso_promedio=("Income", "mean"),
            gasto_vino_promedio=("MntWines", "mean"),
            gasto_carne_promedio=("MntMeatProducts", "mean"),
            total_clientes=("Income", "count"),
        )
        .reset_index()
    )

    print("--------------------------------------------------")
    print("Resumen de Métricas:")
    print(metricas.to_string(index=False))
    print("--------------------------------------------------")

    # Gráfico
    print("\n3. Generando gráfico comparativo...")
    plt.figure(figsize=(8, 5))

    df_melt = df_slice.melt(
        id_vars="Response",
        value_vars=["MntWines", "MntMeatProducts"],
        var_name="Categoria",
        value_name="Gasto",
    )

    df_melt["Categoria"] = df_melt["Categoria"].map(
        {"MntWines": "Vinos", "MntMeatProducts": "Carnes"}
    )

    sns.barplot(
        data=df_melt,
        x="Categoria",
        y="Gasto",
        hue="Response",
        palette=["#7FA9C6", "#1B4F72"],
        errorbar=None,
    )

    plt.title(
        "Gasto Promedio en Vinos y Carnes según Aceptación de Campaña",
        fontsize=12,
        weight="bold",
    )
    plt.xlabel("Categoría de Producto", fontsize=10)
    plt.ylabel("Gasto Promedio ($)", fontsize=10)
    plt.legend(
        title="Aceptó Campaña",
        labels=["No aceptó (0)", "Aceptó (1)"],
        loc="upper right",
    )

    plt.tight_layout()

    # Guarda la imagen en la misma carpeta del script
    nombre_grafico = os.path.join(directorio_actual, "resultado_rebanada.png")
    plt.savefig(nombre_grafico, dpi=300)
    plt.close()

    print(f"¡Listo! Se guardó la imagen en: '{nombre_grafico}'.")


if __name__ == "__main__":
    ejecutar_rebanada()
