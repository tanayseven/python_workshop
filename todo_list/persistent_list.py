import json
import logging
from contextlib import contextmanager
from json import JSONDecodeError
from os import path


@contextmanager
def persistent_list(list_path: str):
    if not path.exists(list_path):
        with open(list_path, 'x'):
            pass
    list_ = {}
    with open(list_path, 'r') as f:
        try:
            list_ = json.load(f)
        except JSONDecodeError:
            logging.log(logging.INFO, 'File in wrong format')
        yield list_
    with open(list_path, 'w') as f:
        json.dump(list_, f)

