import sys

import pyautogui

import screen
import mouse

if __name__ == '__main__':
    print("hello, world! launcher begin!")
    
    print("### screen ###")
    screen.get_screen_size()
    screen.test_size()
    print(screen.test_on_screen())
    screen.get_platform_module_size()

    print("### mouse func ###")
    mouse.get_mouse_pos()
    # mouse.moveto_mouse(0, 0)
    # mouse.move_some_offset_of_mouse(100, 0)
    # mouse.mouse_drag_to(900, 600, pyautogui.LEFT)
    mouse.drag_some_offset_of_mouse(100, 0, 0.5)
