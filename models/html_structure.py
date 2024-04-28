from copy import copy
from typing import Optional, Any


class HtmlStructure:
    """
    Data Model for recreating the HTML hierarchy to the element.

    Usage:
        - Initialize the class
        - add `tag:value` pairs calling add_tag_val method, which will store them in the `self.container` list as a
            dictionary, following the pattern `{'tag': tag, 'value': value}`.
            In this way you have a list of dictionaries left to right representing HTML code depth from top to bottom
        - get the container using `structure` getter, which will also clear `self.container`
    """

    _sample = lambda _, tag, value: {'tag': tag, 'value': value}

    def __init__(self):
        self._container = []
        self.initialized = True

    def add_tag_val(self, tag: str, value: Optional[Any] = None):
        html_tags: dict = self._sample(tag=tag, value=value)
        self._container.append(html_tags)
        return self

    @property
    def structure(self) -> list | list[dict[str:str, str:Any]] | list[dict[str:str, str:None]]:
        container: list = copy(self._container)
        self._container.clear()
        return container
