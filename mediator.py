from typing import Callable
import inspect
from exceptions import HandlerNotFoundError
__handlers__ = {}
__behaviors__ = {}

def __extract_request_type__(handler) ->type:
    isfunc = inspect.isfunction(handler)
    func = handler if isfunc else (handler.handle if hasattr(handler,'handle') else None)
    if not func or not inspect.isfunction(func):
        raise Exception("handler must be a function or a class, that has 'handle' method")
    sign = inspect.signature(func)
    items = list(sign.parameters)
    return sign.parameters.get(items[0]).annotation if isfunc else sign.parameters.get(items[1]).annotation


async def __return_await__(result):
    return await result if inspect.isawaitable(result) or inspect.iscoroutine(result) else result

class Mediator():
    def __init__(self,handler_class_manager:Callable = None):
        if not handler_class_manager:
            self.handler_class_manager = lambda X: X()
    
    handler_class_manager = None

    async def send(self,request):
        if not request:
            raise ValueError("request is none")
        handler  = __handlers__[request.__class__] if __handlers__.get(request.__class__) else None
        if not handler:
            raise HandlerNotFoundError("Handler Not found for request {request}".format(request = request.__class__))
        handler_func = None
        handler_obj=None
        if inspect.isfunction(handler):
            handler_func = handler
        else:
            handler_obj = self.handler_class_manager(handler)
            handler_func = handler_obj.handle

        behaviors = __behaviors__[request.__class__] if __behaviors__.get(request.__class__) else []
        gen = None
        def start_func():
            for behavior in behaviors:
                yield behavior(request,next_func)
            yield handler_func(request)
        
        gen = start_func()
       
        async def next_func():
            return await __return_await__(next(gen))

        result = await next_func()
        
        return await __return_await__(result)
       

    @staticmethod
    def register_handler(handler):
        request_type = __extract_request_type__(handler)
        if not __handlers__.get(request_type):
            __handlers__[request_type] = handler


    @staticmethod
    def register_behavior(behavior):
        request_type = __extract_request_type__(behavior)

        if not __behaviors__.get(request_type):
            __behaviors__[request_type] = []

        if not any( x==behavior for x in __behaviors__[request_type]):
            __behaviors__[request_type].append(behavior)


    