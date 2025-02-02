print (f'__name__:{__name__}')
print (f'__doc__:{__doc__}')
print (f'__package__:{__package__}')
print (f'__loader__:{__loader__}')
print (f'__spec__:{__spec__}')
print (f'__annotations__:{__annotations__}')
print (f'__builtins__:{__builtins__}')
print (f'__cached__:{__cached__}')



class SampleClass:
    def __init__(self):
        print (f'__class__:{self.__class__}')

instance = SampleClass()
