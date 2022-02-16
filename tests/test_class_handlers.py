import asyncio
import unittest

from mediatr import Mediator
from tests.example_handlers import (
    common_log_behavior,
    get_array_query_behavior_3,
    get_array_query_behavior_6,
    GetArrayQueryBehavior,
    GetArrayQueryHandler,
)
from tests.example_queries import GetArrayQuery1


class ClassHandlersTest(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator()
        self.ioloop = asyncio.get_event_loop()
        return super().setUp()

    def test_1(self):
        Mediator.register_handler(GetArrayQueryHandler)
        Mediator.register_behavior(GetArrayQueryBehavior)
        Mediator.register_behavior(common_log_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        Mediator.register_behavior(get_array_query_behavior_6)
        query = GetArrayQuery1(5)
        self.assertEqual(query.items_count, 5)
        result = self.ioloop.run_until_complete(self.mediator.send_async(query))
        self.assertEqual(query.items_count, 4)
        array_count = len(result)
        self.assertEqual(4, array_count)
        self.assertIsNotNone(query.updated_at)

    def test_2(self):
        Mediator.register_handler(GetArrayQueryHandler)
        Mediator.register_behavior(GetArrayQueryBehavior)
        query = GetArrayQuery1(5)
        self.assertEqual(query.items_count, 5)
        result = self.ioloop.run_until_complete(self.mediator.send_async(query))
        self.assertEqual(query.items_count, 4)
        array_count = len(result)
        self.assertEqual(4, array_count)
