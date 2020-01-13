import constants
from helpers import normalize_search_term, get_object_ids, get_list_of_object_names


class SearchEntities():
    def __init__(self, category, search_term):
        self.category = category
        self.search_term = search_term

    def search(self):
        normalized_search_term = normalize_search_term(self.search_term)
        list_of_objects = get_object_ids(normalized_search_term, self.category)

        if not list_of_objects:
            print(constants.INVALID_SEARCH)
            return []

        list_of_names = get_list_of_object_names(list_of_objects)

        print(list_of_names)
        print(list_of_objects)

        return list_of_names


class SearchPhones(SearchEntities):
    def __init__(self, search_term):
        super().__init__(constants.MOBILE_PHONES, search_term)
        super().search()


class SearchCases(SearchEntities):
    def __init__(self, search_term):
        super().__init__(constants.MOBILE_CASES, search_term)
        super().search()


class SearchGeneric(SearchEntities):
    def __init__(self, search_term):
        super().__init__(constants.GENERIC, search_term)
        super().search()
