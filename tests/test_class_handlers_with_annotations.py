import sys
import asyncio
import unittest

from mediatr import Mediator
from tests.example_handlers_annotations import GetArrayQueryHandlerWithAnnotations
from tests.example_queries import GetArrayQueryWithAnnotations


class ClassHandlersTest(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator()
        self.ioloop = asyncio.get_event_loop()
        return super().setUp()

    @unittest.skipUnless(sys.version_info >= (3,7), "requires 3.7+")
    def test_1(self):
        Mediator.register_handler(GetArrayQueryHandlerWithAnnotations)
        query = GetArrayQueryWithAnnotations(5)
        self.assertEqual(query.items_count, 5)
        result = self.ioloop.run_until_complete(self.mediator.send_async(query))
        self.assertEqual(query.items_count, 5)
        array_count = len(result)
        self.assertEqual(5, array_count)
