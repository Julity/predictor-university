import sys

class FullNumpyStub:
    def __init__(self):
        self.multiarray = self
        self._multiarray_umath = self
        self._dtype_ctypes = self
        self.umath = self
        self._dtype = self
        self.fromnumeric = self
        self.arrayprint = self
        self.defchararray = self
        self.records = self
        self.memmap = self
        self.function_base = self
        self.shape_base = self
        self._exceptions = self
        self.__all__ = []
        self.__path__ = []
        self.__file__ = "__fake__.py"
    
    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return FullNumpyStub()
    
    def __call__(self, *args, **kwargs):
        return FullNumpyStub()
    
    def __iter__(self):
        return iter([])
    
    def __len__(self):
        return 0
    
    def __getitem__(self, key):
        return FullNumpyStub()
    
    def __setitem__(self, key, value):
        pass
    
    def __repr__(self):
        return "<numpy.core.stub>"

# РЕГИСТРИРУЕМ ЗАГЛУШКУ СРАЗУ ПРИ ИМПОРТЕ ЭТОГО ФАЙЛА
stub = FullNumpyStub()
sys.modules['numpy._core'] = stub
sys.modules['numpy.core'] = stub
sys.modules['numpy._core.multiarray'] = stub
sys.modules['numpy._core._multiarray_umath'] = stub
sys.modules['numpy._core.umath'] = stub
sys.modules['numpy._core._dtype'] = stub
sys.modules['numpy._core.fromnumeric'] = stub
sys.modules['numpy.core.multiarray'] = stub
sys.modules['numpy.core._multiarray_umath'] = stub

print("✅ numpy_patch.py: заглушка зарегистрирована")