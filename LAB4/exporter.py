import pandas as pd
import matplotlib.pyplot as plt


def save_dataframe(df: pd.DataFrame, base_filename: str) -> None:
    """
    Сохраняет DataFrame в CSV и Excel
    """
    df.to_csv(f"{base_filename}.csv", index=False, encoding="utf-8")
    df.to_excel(f"{base_filename}.xlsx", index=False)


def save_plot(plot: plt.Figure, filename: str, dpi: int = 300) -> None:
    """
    Сохраняет график в файл
    """
    plot.savefig(filename, dpi=dpi, bbox_inches="tight")

