import unittest

from mediatr import Mediator
from tests.example_handlers import get_array_handler, GetArrayQueryHandler, common_log_behavior, get_array_handler_sync
from tests.example_queries import GetArrayQuery, GetArrayQuery1


class SendSyncTest(unittest.TestCase):
    async def test_dispatch_sync(self):
        Mediator.register_handler(get_array_handler_sync)
        Mediator.register_handler(GetArrayQueryHandler)
        Mediator.register_behavior(common_log_behavior)
        mediator = Mediator()
        query1 = GetArrayQuery(5)
        result1 = mediator.send(query1)
        self.assertEqual(len(result1), 5)
        self.assertIsNotNone(query1.updated_at)
        query2 = GetArrayQuery1(4)
        result2 = mediator.send(query2)
        self.assertEqual(len(result2), 4)
        self.assertIsNotNone(query2.updated_at)

    def test_dispatch_sync_without_behavior(self):
        Mediator.register_handler(get_array_handler_sync)
        Mediator.register_handler(GetArrayQueryHandler)
        mediator = Mediator()
        query1 = GetArrayQuery(5)
        result1 = mediator.send(query1)
        self.assertEqual(len(result1), 5)
