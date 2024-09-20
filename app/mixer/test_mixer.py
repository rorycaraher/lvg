import pytest

def test_choose_stems():
    stems = choose_stems(stems_directory)
    assert isinstance(stems, list)
