import os, sys, time, random, string
class LUNIX:
    def __init__(self):
        self.name = "LUNIX"
        self.version = "1.0"
    def run(self):
        username = input("Write username: ")
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Welcome to {self.name} version {self.version}! Your logged in as {username}.")
        while True:
            command = input(f"{username}@{self.name}:~$ ")
            if command == "exit":
                print("Goodbye!")
                break
            if command == "clear":
                os.system("cls" if os.name == "nt" else "clear")
            if command == "fastfetch":
                print("Fetching system information...")
                time.sleep(1)
                print(f"OS: {os.name}")
                print(f"Python version: {sys.version}")
                print(f"Random string: {''.join(random.choices(string.ascii_letters + string.digits, k=10))}")
            elif command == "help":
                print("Available commands: help, exit")
            else:
                print(f"Unknown command: {command}")
LUNIX().run()