from typing import Generic
from mediatr import GenericQuery
class GetArrayQuery():
    def __init__(self, items_count: int):
        self.items_count = items_count

    items_count = 0


class BaseQuery():
    pass


class GetArrayQuery1():
    def __init__(self, items_count: int):
        self.items_count = items_count

    items_count = 0
    common_bahavior_handled = False


class GetArrayQueryWithConstructor():
    def __init__(self, items_count: int):
        self.items_count = items_count

    items_count = 0
    common_bahavior_handled = False


class GetArrayQueryWithAnnotations():
    def __init__(self, items_count: int):
        self.items_count = items_count

    items_count = 0
    common_bahavior_handled = False


class SomeQueryResponseModel():
    def __init__(self,name:str) -> None:
        self.some_name = name
    

class QueryWithTypedResponse(GenericQuery[SomeQueryResponseModel]):
    def __init__(self,name:str) -> None:
        self.some_name = name
    