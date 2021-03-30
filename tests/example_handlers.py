from tests.example_queries import GetArrayQuery, GetArrayQuery1, QueryWithTypedResponse, SomeQueryResponseModel
from mediatr import Mediator
from typing import Callable 
async def get_array_handler(request: GetArrayQuery):
    items = list()

    for i in range(0, request.items_count):
        items.append(i)

    return items


def get_array_handler_sync(request: GetArrayQuery):
    items = list()

    for i in range(0, request.items_count):
        items.append(i)

    return items


def get_array_query_behavior(request: GetArrayQuery, next):
    request.items_count = 4
    return next()


async def get_array_query_behavior_3(request: GetArrayQuery, next):
    request.items_count = 3
    return await next()


async def get_array_query_behavior_6(request: GetArrayQuery, next):
    array1 = await next()
    array1.append(0)
    array1.append(0)
    array1.append(0)
    return array1


class GetArrayQueryHandler():
    def handle(self, request: GetArrayQuery1):
        items = list()

        for i in range(0, request.items_count):
            items.append(i)
        return items


class GetArrayQueryBehavior():
    def handle(self, request: GetArrayQuery1, next):
        request.items_count = 4
        return next()


def common_log_behavior(request: object, next):
    request.updated_at = '123'
    return next()
  


def print_before(request:object,next:Callable):
    print(request.__class__.__name__)
    if hasattr(request,'common_bahavior_handled'):
        request.common_bahavior_handled = True

    print('common_bahavior_handled ')
    return next()



class QueryWithTypedResponseHandler():
    def handle(self, request:QueryWithTypedResponse):
        return SomeQueryResponseModel(request.some_name)
