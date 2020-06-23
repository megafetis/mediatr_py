# mediatr_py

This is an async implementation of Mediator pattern with pipline behaviors.

It is a port of Mediatr [Mediatr](https://github.com/jbogard/MediatR) from .Net

## Usage:

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

print(result) // [0,1,2,3,4]

```
### Using behaviors
You can define behavior class with method 'handle' or function:
```py
@Mediator.behavior
async def get_array_query_behavior(request:GetArrayQuery,next): #behavior only for GetArrayQuery or derived classes
    array1 = await next()
    array1.append(5)
    return array1

@Mediator.behavior
def common_behavior(request:object,next): #behavior for all requests because issubclass(GetArrayQuery,object)==True
    request.timestamp = '123'
    return next()

# ...

mediator = Mediator()
request = GetArrayQuery(5)
result = await mediator.send_async(request)
print(result) // [0,1,2,3,4,5]
print(request.timestamp) // '123'

```

#### Create yor own class handler manager function
For example, if you want to instantiate them with dependency injector or custom 
```py
def my_class_handler_manager(handler_class,is_behavior=False):
    return handler_class()


```


