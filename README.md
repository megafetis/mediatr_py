# mediatr_py

This is an implementation of Mediator pattern with pipline behaviors.

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
### Using behavoirs

```py


```


