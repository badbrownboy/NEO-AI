import pyautogui
import subprocess

def perform_action(plan):
    if "open chrome" in plan:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "type" in plan:
        text = plan.replace("type", "").strip()
        pyautogui.write(text)
    elif "click" in plan:
        pyautogui.click()
