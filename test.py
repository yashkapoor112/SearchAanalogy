import pytest

from main import instantiate_search


class Tests():

    @pytest.mark.parametrize("search_string", "search_filter", [("Red", "Generic")])
    def test_get_search_parameters(self, search_string, search_filter):
        names = instantiate_search(search_string, search_filter)

        assert names[0] == "Red Case Oneplus"