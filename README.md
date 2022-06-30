![](report/img/repository-template.png)

[//]: # (## Python Scientific Project Template)

Welcome to this Python project template!

This template is designed to help you get started with your Python scientific project. It includes a directory structure, files, and configurations that will help you get up and running quickly.

### How to use?

Simply click on the ["Use this template"](https://github.com/robinthibaut/project_template/generate) button above to start using this template. You can then rename the project directory and start working on your project by cloning it to your system.

### Directories
The `project_name` directory is where your project's code will live. The `scripts`, `notebooks`, and `data` directories are where you'll store your project's Python scripts, Jupyter notebooks, and data files, respectively. The `outputs` directory is where your project's output files will be stored (e.g., results, figures...). Finally, the `report` directory contains a LaTeX template for your project's report.

### Files
The `README.md` file contains this information and is intended to help you understand and use the template.

The `LICENSE` file contains the license for this template.

The `.gitignore` file tells git which files to ignore when you're using version control.

The `requirements.txt` file contains a list of Python libraries that your project depends on.

The `config.py` file defines some basic information about the directories used by the project and the hyperparameters used by the project. This is helpful for keeping track of where things are located and what settings are being used.

```python
# config.py

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

```

You can then access the information in this file using the `config` object in your scripts:

```python
# example_script.py

from project_name.config import Directories, HyperParameters

main_dir = Directories.main_dir
```

### More Information
Check this [tutorial](https://medium.com/python-in-plain-english/a-gentle-introduction-to-python-with-pycharm-367f6b73364a) for a gentle introduction to Python, Pycharm, and VCS.

I hope you find this template helpful!