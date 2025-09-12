import webbrowser
import time
import pygetwindow as gw
import pyautogui


def open_tabs_in_corners(url, num_tabs=4):
    """
    Open multiple browser tabs and arrange them in monitor corners
    """
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()
    half_width = screen_width // 2
    half_height = screen_height // 2

    # Open first tab
    webbrowser.open_new_tab(url)
    time.sleep(2)  # Wait for browser to open

    # Get browser window
    browser_windows = gw.getWindowsWithTitle('Chrome') or gw.getWindowsWithTitle('Firefox') or gw.getWindowsWithTitle(
        'Edge')

    if not browser_windows:
        print("Browser window not found")
        return

    browser = browser_windows[0]


    # Arrange first window in top-left
    browser.resizeTo(half_width, half_height)
    browser.moveTo(0, 0)

    # Open additional tabs and arrange them
    for i in range(1, num_tabs):
        # Open new tab (Ctrl+T)
        browser.activate()
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)

        # Navigate to URL (Ctrl+L, then type URL, then Enter)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)
        pyautogui.write(url)
        pyautogui.press('enter')
        time.sleep(2)

        # Arrange window based on corner
        if i == 1:  # Top-right
            browser.moveTo(half_width, 0)
        elif i == 2:  # Bottom-left
            browser.moveTo(0, half_height)
        elif i == 3:  # Bottom-right
            browser.moveTo(half_width, half_height)


if __name__ == "__main__":
    url = input("Enter URL to open: ") or "https://www.google.com"
    num_tabs = int(input("Number of tabs (1-4): ") or "4")

    open_tabs_in_corners(url, min(max(num_tabs, 1), 4))
