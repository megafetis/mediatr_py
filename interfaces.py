from abc import ABCMeta, abstractmethod, abstractproperty,ABC
from typing import Callable


class AbstractHandler(ABC):
    @abstractmethod
    def handle(self,request):
        return NotImplemented


class AbstractBehavior(ABC):
    @abstractmethod
    def handle(self,request,next:Callable):
        return next()