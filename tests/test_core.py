tests/test_core.py
import sys
sys.path.append('../src')
from core import some_function

import pytest

@pytest.mark.parametrize('input, expected', [
    ('', 'Hello, World!')
])
def test_some_function(input, expected):
    assert some_function(input) == expected