from distutils.core import setup

setup(name="base_code",
    author="Dev Sharma",
    author_email="devkosal@gmail.com",
    url="https://github.com/devkosal/base_code",
    packages=["base_code"])

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="base_code", # Replace with your own username
    version="0.0.1",
    author="Dev Sharma",
    author_email="devkosal@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devkosal/base_code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)