import os

import pytest

from ansiblediscover.entity.role import Meta


@pytest.mark.parametrize('content, expected_dependencies', [
    (None, []),
    ({}, []),
    ({'foobar': None}, []),
    ({'foobar': ['something']}, []),
    ({'dependencies': None}, []),
    ({'dependencies': {}}, []),
    ({'dependencies': []}, []),
    ({'dependencies': None}, []),
    ({'dependencies': [None]}, []),
    ({'dependencies': [{'role': 'dependency1'}]}, ['dependency1']),
    ({'dependencies': [{'non_role': 'ignored'}, {'role': 'dependency1'}]}, ['dependency1']),
    ({'dependencies': ['dependency1']}, ['dependency1']),
    ({'dependencies': ['dependency1', {'role': 'dependency2'}]}, ['dependency1', 'dependency2']),
    ({'dependencies': ['dependency1', 'dependency1']}, ['dependency1']),
    ({'dependencies': [{'role': 'dependency1'}, {'role': 'dependency1'}]}, ['dependency1']),
    ({'dependencies': [{'role': 'dependency1', 'attribute': 'foo'}]}, ['dependency1']),
])
def test_dependencies(content, expected_dependencies):
    meta = Meta(content, 'irrelevant_path')
    assert sorted(expected_dependencies) == sorted(d.name for d in meta.dependencies())


def test_path_main():
    path = os.path.join('path', 'to', 'my', 'role')
    assert os.path.join(path, 'meta', 'main.yml') == Meta.main_path(path)
