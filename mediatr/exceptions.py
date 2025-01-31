import inspect


def raise_if_handler_not_found(handler,request):
    if not handler:
        raise HandlerNotFoundError(request)


def raise_if_request_none(request):
    if request == None:
        raise InvalidRequest()


def raise_if_handler_is_invalid(handler):
    isfunc = inspect.isroutine(handler)

    func = None
    if isfunc:
        func = handler
    else:
        if hasattr(handler, 'handle'):
            if inspect.isroutine(handler.handle):
                func = handler.handle
            elif inspect.ismethod(handler.handle):
                func = handler.__class__.handle

    if not func:
        raise InvalidHandlerError(func)
    sign = inspect.signature(func)
    params_l = len(sign.parameters.keys())
    if params_l != (1 if isfunc else 2):
        raise InvalidHandlerError(handler)


def raise_if_behavior_is_invalid(behavior):
    isfunc = inspect.isroutine(behavior)
    func = behavior if isfunc else (behavior.handle if hasattr(behavior, 'handle') else None)
    if not func or not inspect.isroutine(func):
        raise InvalidHandlerError(func)
    sign = inspect.signature(func)
    params_l = len(sign.parameters.keys())
    if params_l != (2 if isfunc else 3):
        raise InvalidBehaviorError(behavior)


class HandlerNotFoundError(Exception):
    def __init__(self, request):
        self.request = request
        super().__init__("Handler for request '{}' is not registered".format(request))


class InvalidRequest(Exception):
    def __init__(self):
        super().__init__("Request must be an object of defined class")


class InvalidHandlerError(Exception):
    def __init__(self, handler):
        self.handler = handler
        super().__init__("Incorrect handler: '{}'. Handler must be a class, that contains 'handle' method with args:(self,request:SomeRequestType) \
            or must be a function with args:(request:SomeRequestType) \
             where 'request' is object of request class. See examples on git".format(handler))


class InvalidBehaviorError(Exception):
    def __init__(self, behavior):
        self.behavior = behavior
        super().__init__("Incorrect behavior: '{}'. Behavior must be a class, that contains 'handle' method with args:(self,request:SomeRequestTypeOrObject,next) \
            or must be a function with args:(request:SomeRequestTypeOrObject,next) \
             where 'next' is coroutine function. See examples on git".format(behavior))
