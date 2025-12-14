import argparse
import os

from file_processor import get_file_paths
from data_processor import (
    create_dataframe,
    sort_dataframe,
    filter_dataframe,
    get_dataframe_info
)
from visualizer import plot_rgb_ranges
from exporter import save_dataframe, save_plot


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Анализ диапазона яркости изображений (RGB)"
    )
    parser.add_argument(
        "--images_path",
        required=True,
        help="Путь к папке с изображениями"
    )

    args = parser.parse_args()
    root_directory = args.images_path

    if not os.path.exists(root_directory):
        print("Указанная папка не существует!")
        return

    print("Сбор файлов...")
    absolute_paths, relative_paths = get_file_paths(root_directory)

    if not absolute_paths:
        print("Изображения не найдены")
        return

    print(f"Найдено изображений: {len(absolute_paths)}")

    df = create_dataframe(absolute_paths, relative_paths)

    print("\nИнформация о DataFrame:")
    get_dataframe_info(df)

    df_sorted = sort_dataframe(df, "brightness_range_r")

    filtered_df = filter_dataframe(df_sorted, "brightness_range_r", 100)
    print(f"\nФайлов с диапазоном R > 100: {len(filtered_df)}")

    print("\nСоздание графика...")
    plot = plot_rgb_ranges(df_sorted)
    save_plot(plot, "rgb_brightness_ranges.png")

    print("Сохранение DataFrame...")
    save_dataframe(df_sorted, "image_brightness_data")

    print("\nРезультаты сохранены:")
    print("- image_brightness_data.csv")
    print("- image_brightness_data.xlsx")
    print("- rgb_brightness_ranges.png")


if __name__ == "__main__":
    main()
