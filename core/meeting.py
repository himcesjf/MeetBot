import cv2
import platform
import numpy as np
from PIL import Image
import pyautogui
import os
from datetime import datetime
from playwright.async_api import Page

class MeetingController:
    def __init__(self, page):
        self.page = page

    def toggle_mic(self):
        """Toggles microphone on/off based on the operating system."""
        try:
            if platform.system() == "Darwin":  # macOS
                self.page.keyboard.press('Meta+KeyD')  # 'Meta' for Command key on macOS
            else:  # Windows/Linux
                self.page.keyboard.press('Control+KeyD')
            print("Mic toggled.")
        except Exception as e:
            print(f"Failed to toggle mic: {e}")

    def toggle_video(self):
        """Toggles video on/off based on the operating system."""
        try:
            if platform.system() == "Darwin":  # macOS
                self.page.keyboard.press('Meta+KeyE')  # 'Meta' for Command key on macOS
            else:  # Windows/Linux
                self.page.keyboard.press('Control+KeyE')
            print("Video toggled.")
        except Exception as e:
            print(f"Failed to toggle video: {e}")

    def toggle_chat(self):
        """Toggles chat window by clicking the chat button."""
        try:
            chat_button = self.page.wait_for_selector('button[aria-label="Chat with everyone"]', timeout=5000)
            chat_button.click()
            print("Chat toggled.")
        except Exception as e:
            print(f"Failed to toggle chat: {e}")

    def send_message(self, message):
        """Sends a message in the chat."""
        try:
            self.toggle_chat()
            chat_box = self.page.get_by_placeholder("Send a message")
            if chat_box:
                chat_box.fill(message)
                self.page.get_by_role("button", name="Send a message").click()
                print(f"Message sent: {message}")
            else:
                print("Chatbox not found!")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def request_camera_activation(self, participant_name):
        """Send a message to ask the participant to turn on their camera."""
        try:
            # Check if chat is already open before toggling it
            chat_open = self.page.evaluate('''document.querySelector('button[aria-label="Chat with everyone"][aria-pressed="true"]') !== null;''')

            if not chat_open:
                self.send_message(f"Hi {participant_name}, could you please turn on your camera?")
            else:
                print("Chat is already open, sending message directly")
                chat_box = self.page.get_by_placeholder("Send a message")
                if chat_box:
                    chat_box.fill(f"Hi {participant_name}, could you please turn on your camera?")
                    self.page.get_by_role("button", name="Send a message").click()
                else:
                    print("Chatbox not found!")
                    
            print(f"Request sent to {participant_name} to turn on their camera.")
        except Exception as e:
            print(f"Failed to send camera request to {participant_name}: {e}")

    def capture_and_analyze_screen(self, region=None, save_path="captured_faces"):
        """Capture the screen or a specific region and analyze it for the presence of a human face."""
        try:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Ensure the save directory exists
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            while True:
                # Capture the screen or a specific region
                screenshot = pyautogui.screenshot(region=region)
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                if len(faces) > 0:
                    print("Human detected in the screen capture.")
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                    # Save the resulting frame with faces highlighted
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    file_name = os.path.join(save_path, f"face_capture_{timestamp}.png")
                    cv2.imwrite(file_name, frame)
                    print(f"Face captured and saved to {file_name}")

                    # Display the resulting frame with faces highlighted
                    cv2.imshow('Screen Capture', frame)
                    break  # Stop after detecting a face

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error analyzing screen capture: {e}")


class AsyncMeetingController:
    def __init__(self, page: Page):
        self.page = page

    async def toggle_mic(self):
        """Toggles microphone on/off based on the operating system."""
        try:
            if platform.system() == "Darwin":  # macOS
                await self.page.keyboard.press('Meta+KeyD')  # 'Meta' for Command key on macOS
            else:  # Windows/Linux
                await self.page.keyboard.press('Control+KeyD')
            print("Mic toggled.")
        except Exception as e:
            print(f"Failed to toggle mic: {e}")

    async def toggle_video(self):
        """Toggles video on/off based on the operating system."""
        try:
            if platform.system() == "Darwin":  # macOS
                await self.page.keyboard.press('Meta+KeyE')  # 'Meta' for Command key on macOS
            else:  # Windows/Linux
                await self.page.keyboard.press('Control+KeyE')
            print("Video toggled.")
        except Exception as e:
            print(f"Failed to toggle video: {e}")

    def toggle_chat(self):
        """Toggles chat window by clicking the chat button."""
        try:
            chat_button = self.page.wait_for_selector('button[aria-label="Chat with everyone"]', timeout=5000)
            chat_button.click()
            print("Chat toggled.")
        except Exception as e:
            print(f"Failed to toggle chat: {e}")

    def send_message(self, message):
        """Sends a message in the chat."""
        try:
            self.toggle_chat()
            chat_box = self.page.get_by_placeholder("Send a message")
            if chat_box:
                chat_box.fill(message)
                self.page.get_by_role("button", name="Send a message").click()
                print(f"Message sent: {message}")
            else:
                print("Chatbox not found!")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def request_camera_activation(self, participant_name):
        """Send a message to ask the participant to turn on their camera."""
        try:
            # Check if chat is already open before toggling it
            chat_open = self.page.evaluate('''document.querySelector('button[aria-label="Chat with everyone"][aria-pressed="true"]') !== null;''')

            if not chat_open:
                self.send_message(f"Hi {participant_name}, could you please turn on your camera?")
            else:
                print("Chat is already open, sending message directly")
                chat_box = self.page.get_by_placeholder("Send a message")
                if chat_box:
                    chat_box.fill(f"Hi {participant_name}, could you please turn on your camera?")
                    self.page.get_by_role("button", name="Send a message").click()
                else:
                    print("Chatbox not found!")
                    
            print(f"Request sent to {participant_name} to turn on their camera.")
        except Exception as e:
            print(f"Failed to send camera request to {participant_name}: {e}")

    def capture_and_analyze_screen(self, region=None, save_path="captured_faces"):
        """Capture the screen or a specific region and analyze it for the presence of a human face."""
        try:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Ensure the save directory exists
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            while True:
                # Capture the screen or a specific region
                screenshot = pyautogui.screenshot(region=region)
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                if len(faces) > 0:
                    print("Human detected in the screen capture.")
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                    # Save the resulting frame with faces highlighted
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    file_name = os.path.join(save_path, f"face_capture_{timestamp}.png")
                    cv2.imwrite(file_name, frame)
                    print(f"Face captured and saved to {file_name}")

                    # Display the resulting frame with faces highlighted
                    cv2.imshow('Screen Capture', frame)
                    break  # Stop after detecting a face

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error analyzing screen capture: {e}")
