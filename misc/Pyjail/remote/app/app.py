import signal

BANNER = "Welcome to PyJail"
TIMEOUT = 300

def main():
    print(BANNER)
    while True:
        try:
            user_input = input(">>> ").strip()
            if any(x in user_input for x in ["import", "environ", "getenv", "os", "print", "system", "__", "open", "flag"]):
                print("Blocked!")
                continue
            exec(user_input)
        except Exception:
            continue

if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    main()