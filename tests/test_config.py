import pytest

from dycomutils.config import ConfigDict


def test_config_dict_supports_attribute_access():
    cfg = ConfigDict({"model": {"name": "baseline"}, "epochs": 3})

    assert cfg.model.name == "baseline"
    assert cfg.epochs == 3


def test_config_dict_recursively_converts_nested_values():
    cfg = ConfigDict(
        {
            "items": [{"name": "a"}, {"name": "b"}],
            "pair": ({"value": 1}, {"value": 2}),
        }
    )

    assert cfg["items"][0].name == "a"
    assert cfg["items"][1].name == "b"
    assert cfg.pair[0].value == 1
    assert cfg.pair[1].value == 2


def test_config_dict_allows_setting_attributes():
    cfg = ConfigDict()

    cfg.train = {"batch_size": 32}

    assert cfg["train"].batch_size == 32


def test_config_dict_deletes_attributes():
    cfg = ConfigDict({"name": "demo"})

    del cfg.name

    with pytest.raises(AttributeError):
        _ = cfg.name


def test_config_dict_missing_attribute_raises_attribute_error():
    cfg = ConfigDict()

    with pytest.raises(AttributeError):
        _ = cfg.missing


def test_config_dict_rejects_multiple_positional_args():
    with pytest.raises(TypeError):
        ConfigDict({}, {})
