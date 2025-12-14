from typing import List

import pandas as pd

from file_processor import calculate_rgb_brightness_ranges


def create_dataframe(
    absolute_paths: List[str],
    relative_paths: List[str]
) -> pd.DataFrame:
    """
    Создаёт DataFrame и добавляет диапазоны яркости по RGB
    """
    df = pd.DataFrame({
        "absolute_file_path": absolute_paths,
        "relative_file_path": relative_paths
    })

    rgb_ranges = df["absolute_file_path"].apply(calculate_rgb_brightness_ranges)

    df["brightness_range_r"] = rgb_ranges.apply(lambda x: x[0])
    df["brightness_range_g"] = rgb_ranges.apply(lambda x: x[1])
    df["brightness_range_b"] = rgb_ranges.apply(lambda x: x[2])

    return df


def sort_dataframe(
    df: pd.DataFrame,
    column: str,
    ascending: bool = True
) -> pd.DataFrame:
    """
    Сортировка DataFrame по выбранной колонке
    """
    return df.sort_values(by=column, ascending=ascending)


def filter_dataframe(
    df: pd.DataFrame,
    column: str,
    threshold: int
) -> pd.DataFrame:
    """
    Фильтрация DataFrame по порогу
    """
    return df[df[column] > threshold]


def get_dataframe_info(df: pd.DataFrame) -> None:
    """
    Вывод общей информации о DataFrame
    """
    print(f"Всего изображений: {len(df)}")
    print("Колонки:")
    for col in df.columns:
        print(f" - {col}")
