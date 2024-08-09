import pyautogui
import pyperclip
import time
from openai import OpenAI
import re

client = OpenAI(
    api_key="your_api_key", #enter your api key here
)

def is_last_message_from_other_user(chat_log, sender_name = "your_other_contacts"): #enter the person you are chatting with here
    messages = chat_log.strip().split("/2024]")[-1]

    if sender_name in messages:
        return True
    return False


pyautogui.click()

# Click on the icon at (921, 1047)
pyautogui.click(921, 1047)

# Short pause to ensure the click action is registered
time.sleep(2)

while True:
    def remove_username_from_message(message, username="Hussnain"):
        pattern = rf'^{username}: '
        return re.sub(pattern, '', message)

    # Drag from (892, 243) to (1820, 920)
    pyautogui.moveTo(913, 265)
    pyautogui.dragTo(1723, 907, duration=1)  # Adjust duration as needed

    # Copy the selected content to clipboard
    pyautogui.hotkey('ctrl', 'c')

    # Click to unselect
    pyautogui.click(1641, 879)

    # Short pause to ensure the copy action is completed
    time.sleep(2)

    # Get the clipboard content and store it in a variable
    chat_history = pyperclip.paste()
    cleaned_message = remove_username_from_message(chat_history)

    print("Copied text: ", chat_history)
    print(is_last_message_from_other_user(chat_history))
    # Pass both arguments to the function
    if is_last_message_from_other_user(chat_history):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Hussnain, affectionately known as Deej. At 14 years old and currently in grade 9, you are diving into the world of AI engineering. As a bright and enthusiastic young girl, you are funny, confident, and extroverted. You have a deep love for anime and the ability to analyze chat history and respond just like Hussnain would. Output should be the next chat response as Hussnain. Don't mention stuff like date stamps and Hussnain: e.t.c"},
                {"role": "user", "content": cleaned_message}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Click at the coordinates (1364, 978)
        pyautogui.click(1364, 978)

        # Short pause to ensure the click action is registered
        time.sleep(1)

        # Paste the text from the clipboard
        pyautogui.hotkey('ctrl', 'v')

        # Short pause to ensure the paste action is completed
        time.sleep(1)

        # Press Enter
        pyautogui.press('enter')
