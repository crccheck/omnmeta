import os
import sys

__all__ = []

# cheat to make imports work without needed to change path,
paths = [
    os.path.join(os.path.dirname(__file__), '..', '..'),
]
sys.path = paths + sys.path
del paths
