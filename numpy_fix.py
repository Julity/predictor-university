# numpy_fix.py - ДОЛЖЕН БЫТЬ ИМПОРТИРОВАН ПЕРВЫМ!
import sys

# Создаём полную заглушку ДО любого импорта numpy
class NumpyCoreStub:
    """Полная заглушка для numpy._core"""
    def __init__(self):
        self.multiarray = self
        self._multiarray_umath = self
        self._dtype_ctypes = self
        self.umath = self
        self._dtype = self
        self.fromnumeric = self
    
    def __getattr__(self, name):
        # Возвращаем пустую функцию для любого вызова
        if name.startswith('__'):
            raise AttributeError(name)
        return lambda *args, **kwargs: None
    
    def __call__(self, *args, **kwargs):
        return None

# Создаём и регистрируем заглушки
stub = NumpyCoreStub()
sys.modules['numpy._core'] = stub
sys.modules['numpy.core'] = stub
sys.modules['numpy._core.multiarray'] = stub
sys.modules['numpy._core._multiarray_umath'] = stub
sys.modules['numpy._core.umath'] = stub
sys.modules['numpy._core._dtype'] = stub
sys.modules['numpy._core.fromnumeric'] = stub

print("✅ Патч numpy._core применён (ранняя загрузка)")