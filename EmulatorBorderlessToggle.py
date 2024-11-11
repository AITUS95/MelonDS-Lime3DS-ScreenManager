import pygetwindow as gw
import keyboard
from screeninfo import get_monitors
import win32gui
import win32con

# Variables to keep track of the state
is_borderless = False
original_styles = {}
original_rects = {}

# Function to get the total dimensions of all screens
def get_total_screen_dimensions():
    monitors = get_monitors()
    min_x = min(monitor.x for monitor in monitors)
    min_y = min(monitor.y for monitor in monitors)
    max_x = max(monitor.x + monitor.width for monitor in monitors)
    max_y = max(monitor.y + monitor.height for monitor in monitors)
    total_width = max_x - min_x
    total_height = max_y - min_y
    return min_x, min_y, total_width, total_height

# Function to make the window borderless
def make_window_borderless(hwnd, window_title):
    # Get the current style of the window
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    original_styles[window_title] = style  # Save the original style

    # Remove borders and title bar
    style &= ~win32con.WS_CAPTION
    style &= ~win32con.WS_THICKFRAME
    style &= ~win32con.WS_MINIMIZE
    style &= ~win32con.WS_MAXIMIZE
    style &= ~win32con.WS_SYSMENU
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
    # Update the window to apply changes
    win32gui.SetWindowPos(hwnd, None, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
                          win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)

# Function to restore the window with borders
def restore_window_style(hwnd, window_title):
    if window_title in original_styles:
        original_style = original_styles[window_title]
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, original_style)
        # Update the window to apply changes
        win32gui.SetWindowPos(hwnd, None, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
                              win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)

# Function to position the emulator windows
def arrange_windows():
    global original_rects
    window_titles = ['melonDS', 'Lime3DS']
    success = False
    for title in window_titles:
        try:
            # Find the window
            target_window = gw.getWindowsWithTitle(title)[0]
            hwnd = target_window._hWnd  # Get the window handle

            # Save the original position and size
            rect = win32gui.GetWindowRect(hwnd)
            original_rects[title] = rect  # (left, top, right, bottom)

            # Make the window borderless
            make_window_borderless(hwnd, title)

            # Get the total dimensions of all screens
            min_x, min_y, total_width, total_height = get_total_screen_dimensions()

            # Move and resize the window to cover all screens
            target_window.moveTo(min_x, min_y)
            target_window.resizeTo(total_width, total_height)

            print(f"Window of {title} positioned without borders")
            success = True
        except IndexError:
            print(f"Window of {title} not found. Make sure it is open.")
    if not success:
        print("No window found for MelonDS or Lime3DS.")

# Function to restore the emulator windows
def restore_windows():
    global original_rects
    window_titles = ['melonDS', 'Lime3DS']
    success = False
    for title in window_titles:
        try:
            # Find the window
            target_window = gw.getWindowsWithTitle(title)[0]
            hwnd = target_window._hWnd  # Get the window handle

            # Restore the window style
            restore_window_style(hwnd, title)

            # Restore the original position and size
            if title in original_rects:
                left, top, right, bottom = original_rects[title]
                width = right - left
                height = bottom - top
                target_window.moveTo(left, top)
                target_window.resizeTo(width, height)

            print(f"Window of {title} restored with borders")
            success = True
        except IndexError:
            print(f"Window of {title} not found. Make sure it is open.")
    if not success:
        print("No window found for MelonDS or Lime3DS.")

# Function to toggle the state
def toggle_windows():
    global is_borderless
    if not is_borderless:
        arrange_windows()
        is_borderless = True
    else:
        restore_windows()
        is_borderless = False

# Configure the F7 key to activate/deactivate the function
keyboard.add_hotkey('F7', toggle_windows)

# Keep the script running
print("Press F7 to toggle the mode of MelonDS or Lime3DS windows")
keyboard.wait('esc')  # Press 'esc' to exit the script
