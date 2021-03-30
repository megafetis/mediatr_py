from tests.example_queries import GetArrayQueryWithConstructor
from mediatr import Mediator
from typing import Callable 

def setup_class_handler_manager(handler_class: type, is_behavior=False):
    if is_behavior:
        # custom logic
        pass

    return handler_class

class GetArrayQueryHandlerWithConstructor():
    def __init__(self, client):
        self.client = client

    def handle(self, request: GetArrayQueryWithConstructor):
        items = list()

        for i in range(0, request.items_count):
            items.append(i)
            
        return items