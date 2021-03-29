import inspect


def raise_if_handler_not_found(handler, handlers):
    if not handler:
        raise HandlerNotFoundError(handler)


def raise_if_request_invalid(request):
    if not request:
        raise InvalidRequest()


def raise_if_handler_is_invalid(handler):
    isfunc = inspect.isfunction(handler)
    func = handler if isfunc else (handler.__class__.handle if hasattr(handler, 'handle') else None)
    if not func or not inspect.isfunction(func):
        raise InvalidHandlerError()
    sign = inspect.signature(func)
    params_l = len(sign.parameters.keys())
    if params_l != (1 if isfunc else 2):
        raise InvalidHandlerError()


def raise_if_behavior_is_invalid(behavior):
    isfunc = inspect.isfunction(behavior)
    func = behavior if isfunc else (behavior.handle if hasattr(behavior, 'handle') else None)
    if not func or not inspect.isfunction(func):
        raise InvalidHandlerError()
    sign = inspect.signature(func)
    params_l = len(sign.parameters.keys())
    if params_l != (2 if isfunc else 3):
        raise InvalidBehaviorError()


class HandlerNotFoundError(Exception):
    def __init__(self, nandler_name):
        super().__init__("Handler {nandler_name} is not registered".format(nandler_name))


class InvalidRequest(Exception):
    def __init__(self):
        super().__init__("Request object must be a object of defined class")


class InvalidHandlerError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg or "Handler must be a class, that contains 'handle' method with args:(self,request:SomeRequestType) \
            or must be a function with args:(request:SomeRequestType) \
             where 'request' is object of request class. See examples on git")


class InvalidBehaviorError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg or "Behavior must be a class, that contains 'handle' method with args:(self,request:SomeRequestTypeOrObject,next) \
            or must be a function with args:(request:SomeRequestTypeOrObject,next) \
             where 'next' is coroutine function. See examples on git")
