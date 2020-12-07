import pytest

import os
import numpy as np
import random
from devai import Path


@pytest.fixture(scope="module")
def test_filter_files_list():
    extensions = ["jpg", "png", "gif", "tiff"]
    temp_dir = "".join([str(np.random.randint(0, 9)) for _ in range(10)])
    file_list = [
        Path(f"fn_{random.randint(0,99)}.{random.choice(extensions)}") for _ in range(1000)]
    return file_list
