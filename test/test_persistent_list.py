import json
from os import path
from tempfile import TemporaryDirectory

from todo_list.persistent_list import persistent_list


def test_persistent_list_should_be_created_as_empty_list_when_file_does_not_exist():
    with TemporaryDirectory() as temp:

        # when
        with persistent_list(f'{temp}/list.json') as list_:
            assert list_ == {}

        # then
        assert path.exists(f'{temp}/list.json')


def test_persistent_list_once_modified_should_be_reflected_when_read_next_time():
    with TemporaryDirectory() as temp:

        # given
        list_path = f'{temp}/list.json'
        with open(list_path, 'w') as f:
            json.dump({}, f)

        # when
        with persistent_list(list_path) as list_:
            list_['id'] = 1234

        # then
        with persistent_list(list_path) as list_:
            assert list_['id'] == 1234
