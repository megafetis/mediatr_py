import asyncio
import unittest

from mediatr import Mediator
from tests.example_handlers import (
    common_log_behavior,
    get_array_handler,
    GetArrayQueryHandler,
)
from tests.example_queries import GetArrayQuery, GetArrayQuery1


class MultipleSendTest(unittest.TestCase):
    def setUp(self):
        self.ioloop = asyncio.get_event_loop()

    def tearDown(self):
        self.ioloop.close()

    def test_1(self):
        Mediator.register_handler(get_array_handler)
        Mediator.register_handler(GetArrayQueryHandler)
        Mediator.register_behavior(common_log_behavior)
        mediator = Mediator()
        query1 = GetArrayQuery(5)
        result1 = self.ioloop.run_until_complete(mediator.send_async(query1))
        self.assertEqual(len(result1), 5)
        self.assertIsNotNone(query1.updated_at)
        query2 = GetArrayQuery1(4)
        result2 = self.ioloop.run_until_complete(mediator.send_async(query2))
        self.assertEqual(len(result2), 4)
        self.assertIsNotNone(query2.updated_at)
