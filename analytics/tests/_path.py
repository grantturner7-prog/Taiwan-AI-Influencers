"""Puts analytics/ on sys.path so the tests can import the modules whichever way they are launched."""
import sys
from pathlib import Path

ANALYTICS = Path(__file__).resolve().parent.parent
if str(ANALYTICS) not in sys.path:
    sys.path.insert(0, str(ANALYTICS))
