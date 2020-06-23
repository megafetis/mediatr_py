import  unittest
from mediator import Mediator
from tests.test_handlers import get_array_handler,GetArrayQueryHandler,common_log_behavior
from tests.test_classes import GetArrayQuery, GetArrayQuery1
import asyncio


class MultipleSendTest(unittest.TestCase):
    def test_1(self):
        ioloop = asyncio.get_event_loop()
        Mediator.register_handler(get_array_handler)
        Mediator.register_handler(GetArrayQueryHandler)
        Mediator.register_behavior(common_log_behavior)
        mediator = Mediator()
        query1 = GetArrayQuery(5)
        result1 = ioloop.run_until_complete(mediator.send_async(query1))
        self.assertEqual(len(result1),5)
        self.assertIsNotNone(query1.updated_at)
        query2 = GetArrayQuery1(4)
        result2 = ioloop.run_until_complete(mediator.send_async(query2))
        self.assertEqual(len(result2),4)
        self.assertIsNotNone(query2.updated_at)
        ioloop.close()
        