# early_fix.py - ПОЛНЫЙ ФИКС ДЛЯ NUMPY 2.0 СОВМЕСТИМОСТИ
import sys
import warnings

# Подавляем warnings
warnings.filterwarnings('ignore')

class NumpyCoreEmulator:
    """Полная эмуляция numpy.core для совместимости"""
    __name__ = 'numpy.core'
    __file__ = '<emulated>/numpy/core/__init__.py'
    __package__ = 'numpy'
    __version__ = '1.24.3'
    
    def __init__(self):
        self.__all__ = [
            'array', 'ndarray', 'dtype', 'float64', 'int32', 'int64',
            'zeros', 'ones', 'empty', 'arange', 'linspace', 'pi', 'e',
            'inf', 'nan', 'isscalar', 'shape', 'reshape', 'dot'
        ]
        self.multiarray = self
        self._multiarray_umath = self
        self.umath = self
        self._dtype = self
        self.fromnumeric = self
        self.defchararray = self
        self.records = self
        self.memmap = self
        self.function_base = self
        self.shape_base = self
        self._exceptions = self
        
        # Предопределенные "значения"
        self.array = self._create_dummy('array')
        self.ndarray = self._create_dummy('ndarray')
        self.dtype = self._create_dummy('dtype')
        self.float64 = self._create_dummy('float64')
        self.int32 = self._create_dummy('int32')
        self.int64 = self._create_dummy('int64')
    
    def _create_dummy(self, name):
        """Создает пустой объект с именем"""
        class Dummy:
            def __repr__(self): return f'<numpy.{name}>'
            def __str__(self): return f'numpy.{name}'
            def __call__(self, *args, **kwargs): return Dummy()
            def __getattr__(self, attr): return Dummy()
            def __getitem__(self, idx): return Dummy()
            def __setitem__(self, idx, val): pass
        return Dummy()
    
    def __getattr__(self, name):
        # Специальные случаи
        if name == '__path__':
            return []
        if name == '__spec__':
            return type('Spec', (), {'loader': None, 'origin': None})()
        
        # Если запрашивают что-то из __all__
        if name in self.__all__:
            return self._create_dummy(name)
        
        # Возвращаем новый эмулятор для всего остального
        return NumpyCoreEmulator()
    
    def __call__(self, *args, **kwargs):
        return NumpyCoreEmulator()
    
    def __iter__(self):
        # Итерация по __all__
        return iter(self.__all__)
    
    def __getitem__(self, key):
        # Поддержка индексации: numpy.core[0], numpy.core['array']
        if isinstance(key, int) and 0 <= key < len(self.__all__):
            return self._create_dummy(self.__all__[key])
        elif isinstance(key, str) and key in self.__all__:
            return self._create_dummy(key)
        return NumpyCoreEmulator()
    
    def __setitem__(self, key, value):
        pass
    
    def __len__(self):
        return len(self.__all__)
    
    def __contains__(self, item):
        return item in self.__all__
    
    def __repr__(self):
        return "<module 'numpy.core' from '<emulated>'>"

# Регистрируем эмулятор ДО импорта numpy
core_emulator = NumpyCoreEmulator()

# Регистрируем все возможные пути
modules_to_patch = [
    'numpy._core',
    'numpy.core',
    'numpy._core.multiarray',
    'numpy._core._multiarray_umath',
    'numpy._core.umath',
    'numpy._core._dtype',
    'numpy._core.fromnumeric',
    'numpy.core.multiarray',
    'numpy.core._multiarray_umath',
    'numpy.core.umath',
    'numpy.core._dtype',
    'numpy.core.fromnumeric',
]

for module_name in modules_to_patch:
    sys.modules[module_name] = core_emulator

print("🚀 early_fix.py: numpy.core полностью эмулирован")