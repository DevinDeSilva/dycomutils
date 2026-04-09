from pathlib import Path
import sys
import types


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _install_fake_tqdm():
    fake_tqdm = types.ModuleType("tqdm")

    def tqdm(iterable, *args, **kwargs):
        return iterable

    fake_tqdm.tqdm = tqdm
    sys.modules["tqdm"] = fake_tqdm


def _install_fake_pynput():
    fake_pynput = types.ModuleType("pynput")
    fake_keyboard = types.ModuleType("pynput.keyboard")

    class Controller:
        def press(self, key):
            pass

        def release(self, key):
            pass

        def type(self, text):
            pass

    class Key:
        enter = "<ENTER>"

    fake_keyboard.Controller = Controller
    fake_keyboard.Key = Key
    fake_pynput.keyboard = fake_keyboard

    sys.modules["pynput"] = fake_pynput
    sys.modules["pynput.keyboard"] = fake_keyboard


_install_fake_tqdm()
_install_fake_pynput()
