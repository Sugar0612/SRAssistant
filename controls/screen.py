import collections
import pyautogui


def get_screen_size():
    print("--- get screen size ---")
    Size = collections.namedtuple("Size", "width height")
    screen_size = Size(1920, 1080)
    print(screen_size)
    print(screen_size.width, screen_size.height)


def test_size():
    print("---- test_size ----")
    size = pyautogui.size()
    print(size)


def test_on_screen():
    print("--- test_onScreen ---")
    return pyautogui.onScreen(1000, 500)


def get_platform_module_size():
    print("--- get_platformModule_size ---")
    width, height = pyautogui.platformModule._size()
    print(width, height)
