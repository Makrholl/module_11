def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = getattr(obj, '__module__', 'built-in')

    result = {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
        "repr": repr(obj)
    }

    return result


class Class:
    def __init__(self, value):
        self.value = value

    def method(self):
        return f"Value is {self.value}"


number_info = introspection_info(42)
print("Интроспекция числа:", number_info)

example_obj = Class(10)
example_info = introspection_info(example_obj)
print("Интроспекция объекта класса ExampleClass:", example_info)

