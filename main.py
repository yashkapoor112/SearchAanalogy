import constants
from entities import SearchGeneric, SearchPhones, SearchCases
from helpers import get_search_string, get_search_filter


def instantiate_search(search_term, search_filter):
    if search_filter == constants.GENERIC:
        return SearchGeneric(search_term)
    if search_filter == constants.MOBILE_PHONES:
        return SearchPhones(search_term)
    if search_filter == constants.MOBILE_CASES:
        return SearchCases(search_term)

    print(constants.INVALID_FILTER)
    return "Invalid Search Filter"

def get_search_parameters():
    search_term =  "Red"  #   get_search_string()
    search_filter = constants.GENERIC # get_search_filter()
    # search_filter = get_search_filter()

    if not search_term:
        return "Invalid Search Term"

    return instantiate_search(search_term, search_filter)


if __name__ == '__main__':
    get_search_parameters()