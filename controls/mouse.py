from pyautogui import position

def get_mouse_pos():
    print("--- get mouse pos ---")
    pos = position()
    print(pos.x, pos.y)