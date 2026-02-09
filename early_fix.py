# early_fix.py - ИСПРАВЛЕННАЯ ВЕРСИЯ
import sys
import warnings
warnings.filterwarnings('ignore')

class CoreStub:
    """ТОЛЬКО для numpy._core, не для всего numpy"""
    def __init__(self):
        self.multiarray = self
        self._multiarray_umath = self
        self.umath = self
        self._dtype = self
        self.fromnumeric = self
    
    def __getattr__(self, name):
        # Возвращаем заглушку для любого атрибута
        return CoreStub()
    
    def __call__(self, *args, **kwargs):
        return CoreStub()
    
    def __iter__(self):
        return iter([])
    
    def __getitem__(self, key):
        return CoreStub()
    
    def __setitem__(self, key, value):
        pass
    
    def __repr__(self):
        return "<numpy._core stub>"

# ПАТЧИМ ТОЛЬКО numpy._core, оставляя остальной numpy нетронутым
core_stub = CoreStub()

# Важно: патчим ТОЛЬКО _core модули
sys.modules['numpy._core'] = core_stub
sys.modules['numpy._core.multiarray'] = core_stub
sys.modules['numpy._core._multiarray_umath'] = core_stub
sys.modules['numpy._core.umath'] = core_stub
sys.modules['numpy._core._dtype'] = core_stub

# НЕ патчим numpy.core (нужен для pandas)
# sys.modules['numpy.core'] = core_stub  # ЗАКОММЕНТИРОВАТЬ!

print("✅ early_fix: numpy._core заглушен (но numpy.core остался)")