from __future__ import annotations
from tests.example_queries import GetArrayQueryWithAnnotations


class GetArrayQueryHandlerWithAnnotations():
    def handle(self: GetArrayQueryHandlerWithAnnotations, request: GetArrayQueryWithAnnotations) -> list:
        items = list()

        for i in range(0, request.items_count):
            items.append(i)
        
        return items
