# MeetBot Project

MeetBot is an automated bot project designed to interact with Google Meet. It provides features such as speech recognition, text-to-speech, and meeting control automation.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Acumenllc/temp_google_meet_rnd.git
   cd temp_google_meet_rnd
   ```

2. View all available branches:
   ```
   git branch -a
   ```

3. Check out the desired branch:
   ```
   git checkout <branch-name>
   ```
4. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate 
   ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Set up your Google account credentials in a `.env` file:
   ```
   GOOGLE_EMAIL=your_email@gmail.com
   GOOGLE_PASSWORD=your_password
   ```

## Usage

Run the main bot script (name may vary depending on the branch):

```
python meetbot<version>.py
```

## Project Structure

- `meetbot<version>.py`: Main bot script
- `core/`: Core modules for the bot
  - `authenticate.py`: Handles Google authentication
  - `meeting.py`: Controls meeting interactions
  - `message.py`: Manages message handling
  - `member.py`: Manages member-related functions
  - `event_handler.py`: Handles various events during the meeting
