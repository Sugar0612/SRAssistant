import pyautogui
from pyautogui import position


def get_mouse_pos():
    print("--- get mouse pos ---")
    pos = position()
    print(pos.x, pos.y)


def moveto_mouse(x, y):
    print("--- move to ---")
    pyautogui.moveTo(x, y, 3.0)


def move_some_offset_of_mouse(x, y):
    print("--- move mouse ---")
    pyautogui.move(xOffset=x, yOffset=y)


def mouse_drag_to(x, y, _button):
    print("--- mouse dray to ---")
    pyautogui.dragTo(x, y, 0.5, button=_button)


def drag_some_offset_of_mouse(x, y, time):
    print("--- drag_some_offset_of_mouse ---")
    pyautogui.drag(x, y, time)


def mouse_click(x, y):
    print("--- mouse click ---")
    pyautogui.click(x, y)


def mouse_double_click(x, y):
    print("--- mouse double click ---")
    pyautogui.doubleClick(x, y)


def mouse_down(x, y):
    print("--- mouse_down ---")
    pyautogui.mouseDown(x, y)