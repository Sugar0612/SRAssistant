import sys
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
    # getScreen()