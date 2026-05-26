"""Import an object from a 'module:attribute' reference string."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


def load_object(ref: str) -> object:
    """Load and return the object at *ref* (``'module:attribute'`` format).

    The current working directory is added to sys.path so that local
    modules (e.g. ``my_agent:agent``) resolve without needing an install.
    """
    if ":" not in ref:
        raise ValueError(f"Invalid reference {ref!r} — expected 'module:attribute'")

    module_path, attr = ref.rsplit(":", 1)
    cwd = str(Path.cwd())
    if cwd not in sys.path:
        sys.path.insert(0, cwd)

    module = importlib.import_module(module_path)
    obj = getattr(module, attr, None)
    if obj is None:
        raise AttributeError(f"Module {module_path!r} has no attribute {attr!r}")
    return obj
