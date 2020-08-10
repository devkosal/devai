# from .utils import *
# from .utils_ml import *
# from .basics import *
# from .callbacks import *
# from .optimizers import *
# from .hooks import *
# from .dataloaders import *
# from .metrics import *
# from .loss_funcs import *
# from .activation_funcs import *
# from .text import *
# from .model import *


from pathlib import Path

def filter_files(files, include=[], exclude=[]):
    for incl in include:
        files = [f for f in files if incl in f.name]
    for excl in exclude:
        files = [f for f in files if excl not in f.name]
    return sorted(files)

def ls(x, recursive=False, include=[], exclude=[]):
    if not recursive:
        out = list(x.iterdir())
    else:
        out = [o for o in x.glob('**/*')]
    out = filter_files(out, include=include, exclude=exclude)
    return out

Path.ls = ls
