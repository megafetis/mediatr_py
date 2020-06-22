import unittest
import inspect
from mediator import Mediator


class InitMediatorTest(unittest.TestCase):
    def setUp(self):
        self.mediator = Mediator()

    # def test_init_mediator(self):
    #     mediator = Mediator()
    #     self.assertIsNotNone(mediator)

    def test_is_func(self):
        self.assertTrue(inspect.isfunction(self.mediator.register_handler))


    def test_is_func_class_method(self):

        class Class1():
            async def method1(self):
                pass

        self.assertTrue(inspect.isfunction(Class1.method1))

    def test_dict_key(self):

        dict1 = {}

        class Class1():
            pass

        dict1[Class1] = 123

        self.assertEqual(123,dict1[Class1])


    
    def test_class_method_sep(self):

        

        class Class1():
            name='ff'

            def func(self,arg1):
                return self.name+arg1

        obj = Class1()

        meth = obj.func
        self.assertEqual('fff',meth('f'))


       