import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def plot_rgb_ranges(df: pd.DataFrame) -> plt.Figure:
    """
    Строит график диапазона яркости по каналам R, G, B
    """
    plt.figure(figsize=(12, 6))

    x = range(len(df))

    plt.plot(x, df["brightness_range_r"], label="Red channel")
    plt.plot(x, df["brightness_range_g"], label="Green channel")
    plt.plot(x, df["brightness_range_b"], label="Blue channel")

    plt.xlabel("Номер изображения")
    plt.ylabel("Диапазон яркости (max - min)")
    plt.title("Диапазон яркости изображений по RGB каналам")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    return plt.gcf()
