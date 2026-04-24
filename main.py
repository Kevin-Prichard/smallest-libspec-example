import sys

def main():
    # REQUIREMENT-ID: spec.app.CmdLine
    if len(sys.argv) > 1:
        sys.stderr.write(
            "FATAL ERROR: Unexpected command line arguments provided.\n"
            f"Received: {sys.argv[1:]}\n"
            "This application strictly enforces a zero-argument policy.\n"
            "Please run the program without any additional arguments (e.g., 'python main.py').\n"
        )
        sys.exit(1)

    # REQUIREMENT-ID: spec.app.App
    print("Hello, world!")

if __name__ == "__main__":
    main()
