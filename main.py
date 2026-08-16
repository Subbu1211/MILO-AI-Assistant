from datetime import datetime


def handle_command(command):
    command = command.lower().strip()

    # Remove wake words
    for wake_word in ["hey milo", "milo"]:
        if command.startswith(wake_word):
            command = command[len(wake_word):].strip()
            break

    # App commands
    if "open whatsapp" in command:
        return "OPEN_APP", "whatsapp"

    if "open chrome" in command:
        return "OPEN_APP", "chrome"

    if "open gmail" in command:
        return "OPEN_APP", "gmail"

    if "open youtube" in command:
        return "OPEN_APP", "youtube"

    # Music
    if "play music" in command or "play song" in command:
        return "PLAY_MUSIC", None

    # Time & date
    if "time" in command:
        return "TIME", None

    if "date" in command or "today" in command:
        return "DATE", None

    # Notes
    if command.startswith("take a note"):
        note = command.replace("take a note", "").strip()
        return "NOTE", note

    # Calculator
    if command.startswith("calculate"):
        expression = command.replace("calculate", "").strip()
        return "CALCULATE", expression

    # Help
    if command == "help" or "what can you do" in command:
        return "HELP", None

    # Exit
    if command in ["exit", "quit", "stop", "goodbye"]:
        return "EXIT", None

    return "UNKNOWN", command


def execute_action(intent, data):

    if intent == "OPEN_APP":
        return f"🤖 MILO: Opening {data}..."

    if intent == "PLAY_MUSIC":
        return "🎵 MILO: Playing music..."

    if intent == "TIME":
        return f"🕐 MILO: {datetime.now().strftime('%I:%M %p')}"

    if intent == "DATE":
        return f"📅 MILO: {datetime.now().strftime('%d %B %Y')}"

    if intent == "NOTE":
        if data:
            with open("notes.txt", "a") as file:
                file.write(data + "\n")
            return f"📝 MILO: Note saved — {data}"
        return "MILO: What should I write?"

    if intent == "CALCULATE":
        try:
            result = eval(data, {"__builtins__": {}}, {})
            return f"🧮 MILO: {result}"
        except:
            return "MILO: I couldn't calculate that."

    if intent == "HELP":
        return """
🤖 MILO COMMANDS

📱 Open WhatsApp
🌐 Open Chrome
📧 Open Gmail
▶️ Open YouTube
🎵 Play music
🕐 Tell me the time
📅 Tell me today's date
📝 Take a note
🧮 Calculate something
🛑 Exit
"""

    if intent == "EXIT":
        return "👋 MILO: Goodbye!"

    return f"🤔 MILO: I don't understand '{data}' yet."


def main():

    print("=" * 50)
    print("          🤖 MILO AI ASSISTANT")
    print("=" * 50)

    while True:

        command = input("\nYou: ")

        intent, data = handle_command(command)

        response = execute_action(intent, data)

        print(response)

        if intent == "EXIT":
            break


if __name__ == "__main__":
    main()
