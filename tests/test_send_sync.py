import unittest

from mediatr import __behaviors__, __handlers__, Mediator
from tests.example_handlers import (
    GetArrayQueryHandler,
    common_log_behavior,
    get_array_handler_sync,
    print_before,
)
from tests.example_queries import GetArrayQuery, GetArrayQuery1


class SendSyncTest(unittest.TestCase):
    def setUp(self):
        __handlers__.clear()
        __behaviors__.clear()

    def tearDown(self):
        __handlers__.clear()
        __behaviors__.clear()

    def test_dispatch_sync(self):
        Mediator.register_handler(get_array_handler_sync)
        Mediator.register_handler(GetArrayQueryHandler)
        Mediator.register_behavior(common_log_behavior)
        Mediator.register_behavior(print_before)
        mediator = Mediator()
        query1 = GetArrayQuery(5)
        result1 = mediator.send(query1)
        self.assertEqual(len(result1), 5)
        self.assertIsNotNone(query1.updated_at)
        query2 = GetArrayQuery1(4)
        result2 = mediator.send(query2)
        self.assertEqual(len(result2), 4)
        self.assertIsNotNone(query2.updated_at)
        self.assertEqual(query1.updated_at, "123")
        self.assertEqual(query2.updated_at, "123")
        self.assertTrue(query2.common_bahavior_handled)

    def test_dispatch_sync_without_behavior(self):
        Mediator.register_handler(get_array_handler_sync)
        Mediator.register_handler(GetArrayQueryHandler)
        mediator = Mediator()
        query1 = GetArrayQuery(5)
        result1 = mediator.send(query1)
        self.assertEqual(len(result1), 5)
