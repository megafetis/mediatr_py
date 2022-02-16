import unittest

from mediatr import __behaviors__, __handlers__, Mediator
from tests.example_handlers import QueryWithTypedResponseHandler
from tests.example_queries import QueryWithTypedResponse


class SendGenericRequestTest(unittest.TestCase):
    def setUp(self):
        __handlers__.clear()
        __behaviors__.clear()

    def tearDown(self):
        __handlers__.clear()
        __behaviors__.clear()

    def test_first(self):
        mediator = Mediator()
        Mediator.register_handler(QueryWithTypedResponseHandler)

        genericQuery = QueryWithTypedResponse(name="mediatr 123")
        respModel = mediator.send(genericQuery)
        self.assertEqual(genericQuery.some_name, respModel.some_name)
