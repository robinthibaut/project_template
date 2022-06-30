# Copyright (c) 2022. Robin Thibaut, Ghent University

import os
import platform
from dataclasses import dataclass
from os.path import dirname, join


class Machine(object):
    computer: str = platform.node()


@dataclass
class Directories:
    """Define main directories and file names"""

    # Content directory
    main_dir: str = dirname(os.path.abspath(__file__))
    data_dir: str = join(main_dir, "data")
    results_dir: str = join(main_dir, "outputs")

    package_dir: str = dirname(main_dir)
    latex_dir: str = join(package_dir, "report")


@dataclass
class HyperParameters:
    """Define hyperparameters"""

    ...
