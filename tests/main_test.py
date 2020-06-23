import unittest
import inspect
from mediator import Mediator,__handlers__,__behaviors__
from .test_handlers import get_array_handler,get_array_query_behavior,get_array_query_behavior_3,get_array_query_behavior_6,get_array_handler_sync
from .test_classes import GetArrayQuery
import asyncio
class MainMediatorTest(unittest.TestCase):

    def test_get_array_query_handler(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        mediator = Mediator()
        query = GetArrayQuery(5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        ioloop.close()
        array_count = len(result)
        self.assertEqual(5,array_count)

    def test_get_array_query_handler_with_behavior(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        Mediator.register_behavior(get_array_query_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        mediator = Mediator()
        query = GetArrayQuery(5)
        self.assertEqual(query.items_count,5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        self.assertEqual(query.items_count,3)
        ioloop.close()
        array_count = len(result)
        self.assertEqual(3,array_count)

    def test_get_array_query_handler_with_behavior_post(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        Mediator.register_behavior(get_array_query_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        Mediator.register_behavior(get_array_query_behavior_6)
        mediator = Mediator()
        query = GetArrayQuery(5)
        self.assertEqual(query.items_count,5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        self.assertEqual(query.items_count,3)
        ioloop.close()
        array_count = len(result)
        self.assertEqual(6,array_count)

    def test_get_array_query_handler_sync_with_behavior_post(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler_sync)
        Mediator.register_handler(get_array_handler)
        Mediator.register_behavior(get_array_query_behavior)
        Mediator.register_behavior(get_array_query_behavior_3)
        Mediator.register_behavior(get_array_query_behavior_6)
        mediator = Mediator()
        query = GetArrayQuery(5)
        self.assertEqual(query.items_count,5)
        result = ioloop.run_until_complete(mediator.send_async(query))
        self.assertEqual(query.items_count,3)
        ioloop.close()
        array_count = len(result)
        self.assertEqual(6,array_count)