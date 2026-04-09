import pytest

from dycomutils.concurrancy import concurrent_dict_execution


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def test_concurrent_dict_execution_with_list_params_thread():
    jobs = {
        "first": [1, 2],
        "second": [3, 4],
    }

    results = dict(concurrent_dict_execution(add, jobs, executor="thread", num_max_workers=2))

    assert results == {"first": 3, "second": 7}


def test_concurrent_dict_execution_with_dict_params_thread():
    jobs = {
        "first": {"a": 2, "b": 5},
        "second": {"a": 4, "b": 6},
    }

    results = dict(concurrent_dict_execution(multiply, jobs, executor="thread", num_max_workers=2))

    assert results == {"first": 10, "second": 24}


def test_concurrent_dict_execution_with_list_params_process():
    jobs = {
        "first": [2, 3],
        "second": [4, 5],
    }

    results = dict(concurrent_dict_execution(add, jobs, executor="process", num_max_workers=2))

    assert results == {"first": 5, "second": 9}


def test_concurrent_dict_execution_rejects_invalid_executor():
    with pytest.raises(NotImplementedError):
        list(concurrent_dict_execution(add, {"job": [1, 2]}, executor="invalid"))


def test_concurrent_dict_execution_rejects_invalid_param_shape():
    with pytest.raises(RuntimeError):
        list(concurrent_dict_execution(add, {"job": 123}, executor="thread"))
