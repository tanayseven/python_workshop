import logging
from typing import Dict, Union


def create_new_list() -> Dict:
    logging.log(logging.INFO, f"Called function create_new_list()")
    return {'auto_increment_counter': 0, 'items': []}


def add_to_list(list_: Dict, text: str):
    logging.log(logging.INFO, f"Called function add_to_list() with arguments [list_: '{list_}', text: '{text}']")
    list_['auto_increment_counter'] += 1
    id_ = list_['auto_increment_counter']
    list_['items'].append(
        {'id': id_, 'text': text}
    )


def remove_from_list(list_: Dict, id_: int) -> bool:
    logging.log(logging.INFO, f"Called function remove_from_list() with arguments [list_: '{list_}', id_: '{id_}']")
    success = False
    for index, element in enumerate(list_['items']):
        if element['id'] == id_:
            del list_['items'][index]
            success = True
            break
    return success


def total_items_in(list_: Dict) -> int:
    logging.log(logging.INFO, f"Called function total_items_in() with arguments [list_: '{list_}']")
    return len(list_['items'])


def get_id_for(list_: Dict, item_text: str) -> Union[int, None]:
    logging.log(logging.INFO, f"Called function get_id_for() with arguments [list_: '{list_}', item_text: '{item_text}']")
    for element in list_['items']:
        if element['text'] == item_text:
            return element['id']
