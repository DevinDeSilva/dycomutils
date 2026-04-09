from dycomutils.serialization import (
    file_exist,
    load_json,
    load_jsonl,
    load_jsonl_generator,
    load_pickle,
    load_text,
    save_json,
    save_jsonl,
    save_jsonl_append,
    save_pickle,
    save_text,
)


def test_json_round_trip(tmp_path):
    path = tmp_path / "data.json"
    payload = {"name": "example", "count": 3}

    save_json(payload, str(path))

    assert load_json(str(path)) == payload


def test_text_round_trip(tmp_path):
    path = tmp_path / "notes.txt"

    save_text("hello world", str(path))

    assert load_text(str(path)) == "hello world"


def test_pickle_round_trip(tmp_path):
    path = tmp_path / "data.pkl"
    payload = {"items": [1, 2, 3], "valid": True}

    save_pickle(payload, str(path))

    assert load_pickle(str(path)) == payload


def test_save_jsonl_list_and_load_jsonl(tmp_path):
    path = tmp_path / "records.jsonl"
    records = [{"id": 1}, {"id": 2}]

    save_jsonl(records, str(path))

    assert load_jsonl(str(path)) == records


def test_save_jsonl_dict_appends_record(tmp_path):
    path = tmp_path / "records.jsonl"

    save_jsonl({"id": 1}, str(path))
    save_jsonl({"id": 2}, str(path))

    assert load_jsonl(str(path)) == [{"id": 1}, {"id": 2}]


def test_save_jsonl_append_creates_and_appends(tmp_path):
    path = tmp_path / "records.jsonl"

    save_jsonl_append(str(path), {"id": 1})
    save_jsonl_append(str(path), {"id": 2})

    assert load_jsonl(str(path)) == [{"id": 1}, {"id": 2}]


def test_load_jsonl_generator_streams_records(tmp_path):
    path = tmp_path / "records.jsonl"
    records = [{"id": 10}, {"id": 20}]
    save_jsonl(records, str(path))

    assert list(load_jsonl_generator(str(path))) == records


def test_file_exist_joins_path_segments(tmp_path):
    nested = tmp_path / "nested"
    nested.mkdir()
    path = nested / "file.txt"
    path.write_text("ok")

    assert file_exist(str(tmp_path), "nested", "file.txt") is True
    assert file_exist(str(tmp_path), "nested", "missing.txt") is False
