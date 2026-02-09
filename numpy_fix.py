# numpy_patch.py - ПОЛНАЯ ЗАГЛУШКА
import sys

class FullNumpyStub:
    """Полноценная заглушка для numpy._core и numpy.core"""
    def __init__(self):
        # Важные атрибуты
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
        
        # Для совместимости с from .core import *
        self.__all__ = []
    
    def __getattr__(self, name):
        # Для специальных случаев
        if name in ['array', 'ndarray', 'dtype', 'ufunc']:
            return self
        
        # Возвращаем новую заглушку для любого атрибута
        return FullNumpyStub()
    
    def __call__(self, *args, **kwargs):
        # Если вызывают как функцию
        return FullNumpyStub()
    
    def __iter__(self):
        # Поддержка итерации (исправляет ошибку 'not iterable')
        return iter([])
    
    def __len__(self):
        return 0
    
    def __getitem__(self, key):
        return FullNumpyStub()
    
    def __setitem__(self, key, value):
        pass
    
    def __repr__(self):
        return "<numpy.core.stub>"
    
    def __str__(self):
        return "numpy.core.stub"

# Создаем и регистрируем заглушку ДО импорта numpy
stub = FullNumpyStub()

# Регистрируем ВСЕ возможные пути
sys.modules['numpy._core'] = stub
sys.modules['numpy.core'] = stub
sys.modules['numpy._core.multiarray'] = stub
sys.modules['numpy._core._multiarray_umath'] = stub
sys.modules['numpy._core.umath'] = stub
sys.modules['numpy._core._dtype'] = stub
sys.modules['numpy._core.fromnumeric'] = stub
sys.modules['numpy.core.multiarray'] = stub
sys.modules['numpy.core._multiarray_umath'] = stub

print("✅ Полная заглушка numpy зарегистрирована")