import json
from typing import List

from attr import attrs, attrib, asdict
from cattr import structure


class InvalidJsonException(Exception):
    pass


@attrs
class Item:
    id: str = attrib()


@attrs
class ListResponse:
    items: List[Item] = attrib()

    def to_json(self):
        return json.dumps(asdict(self, filter=lambda key, val: val is not None))


@attrs
class ListsForUsersResponse:
    lists: List[ListResponse] = attrib()

    def to_json(self):
        return json.dumps(asdict(self, filter=lambda key, val: val is not None))


@attrs
class ActiveUsersResponse:
    usernames: List[str] = attrib()

    def to_json(self):
        return json.dumps(asdict(self, filter=lambda key, val: val is not None))


@attrs
class LoginRequest:
    username: str = attrib()
    password: str = attrib()

    @classmethod
    def from_json(cls, json_string: str) -> 'LoginRequest':
        try:
            return structure(json.loads(json_string), cls)
        except (TypeError, AttributeError):
            raise InvalidJsonException()


@attrs
class ListsForUsersRequest:
    username: str = attrib()

    @classmethod
    def from_json(cls, json_string: str) -> 'LoginRequest':
        try:
            return structure(json.loads(json_string), cls)
        except (TypeError, AttributeError):
            raise InvalidJsonException()
