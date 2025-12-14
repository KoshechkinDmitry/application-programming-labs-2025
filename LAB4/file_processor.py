from pathlib import Path
from typing import List, Tuple

import numpy as np
from PIL import Image


def get_file_paths(root_directory: str) -> Tuple[List[str], List[str]]:
    """
    Получает абсолютные и относительные пути изображений
    """
    absolute_paths: List[str] = []
    relative_paths: List[str] = []

    root_path = Path(root_directory)

    for file in root_path.rglob("*"):
        if file.suffix.lower() in {".jpg", ".jpeg", ".png", ".bmp"}:
            absolute_paths.append(str(file.resolve()))
            relative_paths.append(str(file.relative_to(root_path)))

    return absolute_paths, relative_paths


def calculate_rgb_brightness_ranges(image_path: str) -> tuple[int, int, int]:
    """
    Вычисляет диапазон яркости (max - min) по каналам R, G, B
    """
    with Image.open(image_path).convert("RGB") as img:
        pixels = np.array(img)

        r_range = int(pixels[:, :, 0].max() - pixels[:, :, 0].min())
        g_range = int(pixels[:, :, 1].max() - pixels[:, :, 1].min())
        b_range = int(pixels[:, :, 2].max() - pixels[:, :, 2].min())

    return r_range, g_range, b_range
