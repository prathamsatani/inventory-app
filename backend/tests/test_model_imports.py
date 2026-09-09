import importlib

def test_models_module_imports_from_src_package():
    module = importlib.import_module("src.models")
    assert hasattr(module, "Base")
