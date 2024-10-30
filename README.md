This project is a basic keylogger that records and logs keystrokes.
It captures each key press, logs it to a file for later review, and displays the keystrokes on the screen in real-time.
This project uses Python’s `pynput` library to manage keyboard input and is intended for **educational purposes only**.

Disclaimer:
This tool is designed for educational and ethical purposes.
Unauthorized use of keyloggers to track keystrokes or capture private data without explicit permission is illegal and punishable by law.
Use this tool responsibly.

## Project Overview
Features
- **Real-Time Key Capture:** Records each key press in real-time, displaying it on the screen.
- **Logging to a File:** Saves all captured keystrokes to a text file for later review.
- **Educational Use:** Demonstrates the basics of handling keyboard events in Python using the `pynput` library.

How It Works
The keylogger listens to each key event and logs it in the specified text file.
Each key press is captured and printed to the console, while certain keys (e.g., `Enter`, `Space`) are recorded with readable tags (e.g., `[ENTER]`, `[SPACE]`).

Prerequisites
This project requires Python and the `pynput` library. Install `pynput` by running:

```bash
pip install pynput
