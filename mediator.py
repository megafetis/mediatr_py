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

class Mediator():
    def __init__(self,handler_class_manager:Callable = None):
        if not handler_class_manager:
            self.handler_class_manager = lambda X: X()
    
    handler_class_manager = None

    async def send(self,request):
        if not request:
            raise ValueError("request is none")
        handler  = __handlers__[request.__class__] if __handlers__.has_key(request.__class__) else None
        if not handler:
            raise HandlerNotFoundError("Handler Not found for request {request}".format(request = request.__class__))
        handler_func = handler if inspect.isfunction(handler) else handler.handle

        behaviors = __behaviors__[request.__class__] if __behaviors__.has_key(request.__class__) else []

        def next_func(request,next:Callable):
            return next(request)
        for b in behaviors:
            next_func(request,)

        
            




        result = handler_func(request)

        if inspect.isawaitable(result):
            return await result
        else:
            return result

    
    @staticmethod
    def register_handler(handler):
        request_type = __extract_request_type__(handler)
        
        if not __handlers__.has_key(request_type):
            __handlers__[request_type] = handler


    @staticmethod
    def register_behavior(behavior):
        pass

    