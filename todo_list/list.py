from typing import List, Dict, Union


def create_new_list() -> Dict:
    return {'auto_increment_counter': 0, 'items': []}


def add_to_list(list_: Dict, text: str):
    list_['auto_increment_counter'] += 1
    id_ = list_['auto_increment_counter']
    list_['items'].append(
        {'id': id_, 'text': text}
    )


def remove_from_list(list_: Dict, id_: int) -> bool:
    success = False
    for index, element in enumerate(list_['items']):
        if element['id'] == id_:
            del list_['items'][index]
            success = True
            break
    return success


def total_items_in(list_: Dict) -> int:
    return len(list_['items'])


def get_id_for(list_: Dict, item_text: str) -> Union[int, None]:
    for element in list_['items']:
        if element['text'] == item_text:
            return element['id']
