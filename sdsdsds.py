import win32api
import win32gui


def setRussLayout():
    # переключение на рускую раскладку
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050,0,0x04190419)
    return(result)

def setEngLayout():
    # переключение на английскую раскладку
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050,0,0x04090409)
    return(result)

#setEngLayout()


setRussLayout()