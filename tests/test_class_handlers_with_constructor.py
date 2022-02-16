import asyncio
import unittest

from mediatr import Mediator
from tests.example_handlers_constructur import (
    setup_class_handler_manager,
    GetArrayQueryHandlerWithConstructor,
)
from tests.example_queries import GetArrayQueryWithConstructor


class ClassHandlersTest(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator(setup_class_handler_manager)
        self.ioloop = asyncio.get_event_loop()
        return super().setUp()

    def test_1(self):
        class Client:
            def test_1(self):
                return "test_3"

        get_array_query_handler_with_constructor = GetArrayQueryHandlerWithConstructor(
            Client
        )
        Mediator.register_handler(get_array_query_handler_with_constructor)
        query = GetArrayQueryWithConstructor(5)
        self.assertEqual(query.items_count, 5)
        result = self.ioloop.run_until_complete(self.mediator.send_async(query))
        self.assertEqual(query.items_count, 5)
        array_count = len(result)
        self.assertEqual(5, array_count)
