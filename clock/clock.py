from time import strftime
import sys
import os

def display_clock():
    while True:
        # Clear the console (works on both Windows and Unix-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Get and display the current time
        current_time = strftime('%H:%M:%S %p')
        print(f"Current Time: {current_time}")

        # Wait for one second before updating the time
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    try:
        import time
        display_clock()
    except KeyboardInterrupt:
        print("\nClock stopped.")
