import pytest
import os
from devai import Config, filter_files
import numpy as np


def test_config():
    config = Config(key1="value1")
    config.key2 = "value2"
    assert config.key1 == "value1" and config.key2 == "value2"


def test_file_filtering_on_extensions(test_filter_files_list):
    files = test_filter_files_list
    png_files = filter_files(files, include=["png"], extension_filtering=True)
    assert len(png_files) > 0
    assert all([str(f).split(".")[-1] == "png" for f in png_files])
