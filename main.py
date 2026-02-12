import tkinter as tk
import keyboard
import win32gui
import win32con

OVERLAY_ALPHA = 0.85
HOTKEY = "alt+`"

# Create window
overlay = tk.Tk()
overlay.withdraw()  # start hidden
overlay.overrideredirect(True)  # remove border
overlay.attributes("-topmost", True)
overlay.attributes("-alpha", OVERLAY_ALPHA)
overlay.configure(bg="#050505")

# Manually set fullscreen size
screen_width = overlay.winfo_screenwidth()
screen_height = overlay.winfo_screenheight()
overlay.geometry(f"{screen_width}x{screen_height}+0+0")

overlay.update_idletasks()

# Make click-through
hwnd = win32gui.GetParent(overlay.winfo_id())
styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)

visible = False

def toggle_overlay():
    global visible
    if visible:
        overlay.withdraw()
        visible = False
    else:
        overlay.deiconify()
        visible = True

keyboard.add_hotkey(HOTKEY, toggle_overlay)

print(f"Press {HOTKEY} to toggle dark eye protection overlay.")
overlay.mainloop()
