import types

from dycomutils.automation import get_random_val_0_20, write_from_file
from dycomutils.automation import keystrokes


def test_get_random_val_0_20_clamps_random_value(monkeypatch):
    args = types.SimpleNamespace(random=15)
    calls = []

    def fake_randint(start, end):
        calls.append((start, end))
        return end

    monkeypatch.setattr(keystrokes.random, "randint", fake_randint)

    assert get_random_val_0_20(args) == 1.9
    assert calls == [(1, 19)]


def test_write_from_file_types_characters_and_enters(tmp_path, monkeypatch):
    path = tmp_path / "notes.txt"
    path.write_text("ab\nc")

    events = []

    class FakeKeyboard:
        def press(self, key):
            events.append(("press", key))

        def release(self, key):
            events.append(("release", key))

        def type(self, text):
            events.append(("type", text))

    args = types.SimpleNamespace(
        file_path=str(path),
        delay_line=0.5,
        delay_char=0.1,
        random=3,
    )

    monkeypatch.setattr(keystrokes, "Controller", lambda: FakeKeyboard())
    monkeypatch.setattr(keystrokes, "get_random_val_0_20", lambda args: 1)
    monkeypatch.setattr(keystrokes.time, "sleep", lambda seconds: None)

    write_from_file(args)

    assert events == [
        ("type", "a"),
        ("type", "b"),
        ("press", keystrokes.Key.enter),
        ("release", keystrokes.Key.enter),
        ("type", "c"),
    ]
