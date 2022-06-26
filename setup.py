from json import dump
import os
import re
from shutil import rmtree

from setuptools import find_packages, setup


def get_long_description() -> str:
    """
    Return the README.
    """
    return open("README.md", "r", encoding="utf8").read()


def get_install_requires():
    return open("requirements.txt").read().splitlines()


setup(
    name="canvas-task",
    version="v0.0.1",
    url="https://github.com/Gorgeous-Patrick/canvas_task.git",
    license="MIT",
    description="A handy tool to download the assignments from Canvas",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="PatrickLi",
    author_email="patrickli@sjtu.edu.cn",
    maintainer="PatrickLi",
    maintainer_email="patrickli@sjtu.edu.cn",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["canvas-task=canvas_task:main"]},
    install_requires=get_install_requires(),
)
