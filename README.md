# mediatr_py

[![PyPI](https://img.shields.io/pypi/v/mediatr)](https://pypi.org/project/mediatr)
[![Python](https://img.shields.io/pypi/pyversions/mediatr)](https://pypi.org/project/mediatr) 
[![Downloads](https://img.shields.io/pypi/dm/mediatr)](https://pypi.org/project/mediatr) 

This is an async implementation of Mediator pattern with pipline behaviors.

It is a port of [Mediatr](https://github.com/jbogard/MediatR) from .Net C#

Requirements:
* Python >= 3.5

## Usage:

install [mediatr](https://pypi.org/project/mediatr/):

`pip install mediatr`

### Define your request class

```py

class GetArrayQuery():
    def __init__(self,items_count:int):
        self.items_count = items_count

```

### Define your handler class or function

```py
import Mediator from mediatr

@Mediator.handler
async def get_array_handler(request:GetArrayQuery):
    items = list()
    for i in range(0, request.items_count):
        items.append(i)
    return items
    
# or just Mediator.register_handler(get_array_handler)
    
```

or class:

```py
@Mediator.handler
class GetArrayQueryHandler():
    def handle(self,request:GetArrayQuery):
        items = list()
        for i in range(0, request.items_count):
            items.append(i)
        return items
        
# or just Mediator.register_handler(GetArrayQueryHandler)
```

### Run mediator

```py
import Mediator from mediatr

mediator = Mediator()

request = GetArrayQuery(5)

result = await mediator.send_async(request)

# result = mediator.send(request) in synchronous mode

print(result) // [0,1,2,3,4]

```

> If you are using synchronous `mediator.send(request)` method, try to define synchronous handlers and behaviors
>
> In another case use `asyncio` module for manual manage of event loop in synchronous code


### Run mediator statically, without instance

```py
import Mediator from mediatr

request = GetArrayQuery(5)

result = await Mediator.send_async(request)
# or:
result = Mediator.send(request) #in synchronous mode. Async handlers and behaviors will not blocking!

print(result) // [0,1,2,3,4]

```

Note that instantiation of `Mediator(handler_class_manager = my_manager_func)` is useful if you have custom handlers creation. For example using an injector.
By default class handlers are instantiated with simple init:  `SomeRequestHandler()`. handlers or behaviors as functions are executed directly. 


## Using behaviors
You can define behavior class with method 'handle' or function:

```py
@Mediator.behavior
async def get_array_query_behavior(request:GetArrayQuery, next): #behavior only for GetArrayQuery or derived classes
    array1 = await next()
    array1.append(5)
    return array1

@Mediator.behavior
def common_behavior(request:object, next): #behavior for all requests because issubclass(GetArrayQuery,object)==True
    request.timestamp = '123'
    return next()

# ...

mediator = Mediator()
request = GetArrayQuery(5)
result = await mediator.send_async(request)
print(result) // [0,1,2,3,4,5]
print(request.timestamp) // '123'

```

## Using custom handler (behavior) factory for handlers (behaviors) as classes

If your handlers or behaviors registered as functions, it just executes them.

In case with handlers or behaviors, declared as classes with method `handle` Mediator uses function, that instantiates handlers or behaviors:

```py
def default_handler_class_manager(HandlerCls:type,is_behavior:bool=False):
    return HandlerCls()

```


For example, if you want to instantiate them with dependency injector or custom, pass your own factory function to Mediator:

```py
def my_class_handler_manager(handler_class, is_behavior=False):
    
    if is_behavior:
        # custom logic
        pass

    return injector.get(handler_class)

mediator = Mediator(handler_class_manager=my_class_handler_manager)

```
PS:


The `next` function in behavior is `async`, so if you want to take results or if your behavior is async, use `middle_results = await next()`


Handler may be async too, if you need.

## Using with generic typing support (version >= 1.2):

```py

from mediatr import Mediator, GenericQuery


class UserModel(BaseModel): # For example sqlalchemy ORM entity
    id = Column(String,primary_key=True)
    name = Column(String)


class FetchUserQuery(GenericQuery[UserModel])
    def __init__(self,user_id:str):
        self.user_id = user_id


mediator = Mediator()

request = FetchUserQuery(user_id = "123456")

user = mediator.send(request) # type of response will be a UserModel


# -------------------------------------------------------------


class FetchUserQueryHandler():

    def handle(self, request:FetchUserQuery):
        db_session = Session() #sqlalchemy session
        return db_session.query(UserModel).filter(UserModel.id == request.user_id).one()

# or handler as simple function:

def fetch_user_query_handler(request:FetchUserQuery):
    db_session = Session() #sqlalchemy session
    return db_session.query(UserModel).filter(UserModel.id == request.user_id).one()


```