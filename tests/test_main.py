import asyncio
import unittest

from mediatr import __behaviors__, __handlers__, Mediator
from tests.example_handlers import (
    get_array_handler,
    get_array_handler_sync,
    get_array_query_behavior,
    get_array_query_behavior_3,
    get_array_query_behavior_6,
)
from tests.example_queries import GetArrayQuery


class MainMediatorTest(unittest.TestCase):
    def setUp(self):
        __handlers__.clear()
        __behaviors__.clear()

    def tearDown(self):
        __handlers__.clear()
        __behaviors__.clear()

    def test_get_array_query_handler(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        mediator = Mediator()
        query = GetArrayQuery(5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        array_count = len(result)
        self.assertEqual(5, array_count)

    def test_get_array_query_handler_with_behavior(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        Mediator.register_behavior(get_array_query_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        mediator = Mediator()
        query = GetArrayQuery(5)
        self.assertEqual(query.items_count, 5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        self.assertEqual(query.items_count, 3)
        array_count = len(result)
        self.assertEqual(3, array_count)

    def test_get_array_query_handler_with_behavior_post(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        Mediator.register_behavior(get_array_query_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        Mediator.register_behavior(get_array_query_behavior_6)
        mediator = Mediator()
        query = GetArrayQuery(5)
        self.assertEqual(query.items_count, 5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        self.assertEqual(query.items_count, 3)
        array_count = len(result)
        self.assertEqual(6, array_count)

    def test_get_array_query_handler_sync_with_behavior_post(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler_sync)
        Mediator.register_handler(get_array_handler)
        Mediator.register_behavior(get_array_query_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        Mediator.register_behavior(get_array_query_behavior_6)
        mediator = Mediator()
        query = GetArrayQuery(5)
        self.assertEqual(query.items_count, 5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        self.assertEqual(query.items_count, 3)
        array_count = len(result)
        self.assertEqual(6, array_count)
