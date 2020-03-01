from todo_list.list import create_new_list, add_to_list, remove_from_list, total_items_in, get_id_for


def test_newly_created_list_is_empty():
    list_ = create_new_list()

    assert total_items_in(list_) == 0


def test_adding_items_to_list_increases_its_size():
    list_ = create_new_list()

    add_to_list(list_, 'Prepare for the coding test')

    assert total_items_in(list_) == 1


def test_adding_items_to_list_get_ids_assigned_in_sequence():
    list_ = create_new_list()
    add_to_list(list_, 'Prepare for the coding test')
    add_to_list(list_, 'Buy milk')
    add_to_list(list_, 'Doctor\'s appointment')

    id_1 = get_id_for(list_, 'Prepare for the coding test')
    id_2 = get_id_for(list_, 'Buy milk')
    id_3 = get_id_for(list_, 'Doctor\'s appointment')

    assert id_1 == 1
    assert id_2 == 2
    assert id_3 == 3


def test_removal_of_item_from_a_list_decreases_its_size():
    list_ = create_new_list()
    add_to_list(list_, 'Prepare for the coding test')
    id_to_be_deleted = get_id_for(list_, 'Prepare for the coding test')

    success = remove_from_list(list_, id_to_be_deleted)

    assert success
    assert total_items_in(list_) == 0


def test_items_can_be_deleted_from_in_between():
    list_ = create_new_list()
    add_to_list(list_, 'Prepare for the coding test')
    add_to_list(list_, 'Buy milk')
    add_to_list(list_, 'Doctor\'s appointment')
    id_to_be_deleted = get_id_for(list_, 'Buy milk')

    success = remove_from_list(list_, id_to_be_deleted)

    assert success
    assert total_items_in(list_) == 2


def test_removal_of_item_that_does_not_exist_should_not_succeed():
    list_ = create_new_list()
    add_to_list(list_, 'Prepare for the coding test')

    success = remove_from_list(list_, 12345)

    assert not success
    assert total_items_in(list_) == 1
