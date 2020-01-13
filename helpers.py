import inventory
import constants

def get_search_string():
    search_term = input("Enter Search Term")

    if not search_term:
        return None
    return search_term


def get_search_filter():
    search_filter = input("Enter Search Filter")

    if not search_filter:
        return constants.GENERIC
    return search_filter


def get_list_of_mobile():
    return inventory.test_data["Mobile Phones"]


def get_list_of_cases():
    return inventory.test_data["Mobile Cases"]


def get_object_ids(search_term, search_filter):
    data = inventory.test_data[search_filter]
    keywords = list(data.keys())
    list_of_ids = []

    for keyword in keywords:
        if (keyword.find(search_term) != -1):
            list_of_ids.extend(inventory.test_data[search_filter][keyword])

    return list_of_ids


def get_list_of_object_names(ids):
    names = []

    for id in ids:
        names.append(inventory.test_ids[id])

    return names


def normalize_search_term(search_term):
    return search_term
