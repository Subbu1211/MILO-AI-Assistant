"""
MILO - AI Voice & Text Assistant
Version 2.0
"""

def main():
    print("=" * 45)
    print("        MILO - AI ASSISTANT v2.0")
    print("=" * 45)
    print("MILO is starting...")
    print("Text mode is ready.")
    print("Type 'exit' to close MILO.\n")

    while True:
        command = input("You: ").strip()

        if command.lower() == "exit":
            print("MILO: Goodbye! 👋")
            break

        if not command:
            continue

        print(f"MILO: I received your command: {command}")


if __name__ == "__main__":
    main()
