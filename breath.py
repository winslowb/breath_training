import time
import argparse
import os
import subprocess
import sys
import select
import random

# messages to print on quit
QUIT_MESSAGES = [
    "Keep going, you're doing amazing!",
    "Nice session! Remember to breathe and smile.",
    "Great job today—stay calm and carry on!",
    "You rock! Take a moment to appreciate your progress.",
    "Well done! See you next time for more mindful breaths."
]

def check_quit():
    """Non-blocking check for 'q' input to quit."""
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        line = sys.stdin.readline().strip()
        if line.lower() == 'q':
            print("\n" + random.choice(QUIT_MESSAGES))
            sys.exit(0)

def play_sound(sound_file):
    """Plays the sound file using mpg123 with quiet output."""

def breathing_coach(inhale, hold, exhale, rounds):
    print("Breathing coach started. Press 'q' then Enter at any time to quit.")
    round_count = 0
    if rounds is None or rounds <= 0:
        while True:
            os.system('clear')  # Clear the screen
            round_count += 1
            print(f"Round: {round_count}")

            print("Inhale...", end='\r')
            play_sound("gong-inhale.mp3")
            for i in range(int(inhale), 0, -1):
                print(f"Inhale... {i}", end='\r')
                check_quit()
                time.sleep(1)
            print("Inhale... Done")

            if hold > 0:
                for i in range(int(hold), 0, -1):
                    # graphical countdown bar of circles
                    total = int(hold)
                    filled = int((i/total) * 20)
                    bar = '●' * filled + '○' * (20 - filled)
                    print(f"Hold... {i:2d}s {bar}", end='\r', flush=True)
                    check_quit()
                    process = subprocess.Popen(["mpg123", "-q", "ding.mp3"])
                    time.sleep(1)
                    try:
                        process.kill()
                    except Exception:
                        pass
                print("Hold... Done")

            print("Exhale...", end='\r')
            play_sound("gong-exhale.mp3")
            for i in range(int(exhale), 0, -1):
                print(f"Exhale... {i}", end='\r')
                check_quit()
                time.sleep(1)
            print("Exhale... Done")
    else:
        for round_count in range(1, int(rounds) + 1):
            os.system('clear')  # Clear the screen
            print(f"Round: {round_count}")

            print("Inhale...", end='\r')
            play_sound("gong-inhale.mp3")
            for i in range(int(inhale), 0, -1):
                print(f"Inhale... {i}", end='\r')
                check_quit()
                time.sleep(1)
            print("Inhale... Done")

            if hold > 0:
                for i in range(int(hold), 0, -1):
                    # graphical countdown bar of circles
                    total = int(hold)
                    filled = int((i/total) * 20)
                    bar = '●' * filled + '○' * (20 - filled)
                    print(f"Hold... {i:2d}s {bar}", end='\r', flush=True)
                    check_quit()
                    process = subprocess.Popen(["mpg123", "-q", "ding.mp3"])
                    time.sleep(1)
                    try:
                        process.kill()
                    except Exception:
                        pass
                print("Hold... Done")

            print("Exhale...", end='\r')
            play_sound("gong-exhale.mp3")
            for i in range(int(exhale), 0, -1):
                print(f"Exhale... {i}", end='\r')
                check_quit()
                time.sleep(1)
            print("Exhale... Done")
        print(f"\nCompleted {rounds} rounds. Exiting.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A command-line breathing coach.")
    parser.add_argument("--inhale", type=int, default=None,
                        help="Inhale duration in seconds (will prompt if omitted).")
    parser.add_argument("--hold", type=int, default=None,
                        help="Hold duration in seconds (will prompt if omitted).")
    parser.add_argument("--exhale", type=int, default=None,
                        help="Exhale duration in seconds (will prompt if omitted).")
    parser.add_argument("--rounds", type=int, default=None,
                        help="Number of breathing cycles to perform (blank=infinite).")
    args = parser.parse_args()

    # Interactive prompts for any missing values
    if args.inhale is None:
        default = 4
        val = input(f"Inhale duration in seconds [default {default}]: ").strip()
        args.inhale = int(val) if val else default
    if args.hold is None:
        default = 0
        val = input(f"Hold duration in seconds [default {default}]: ").strip()
        args.hold = int(val) if val else default
    if args.exhale is None:
        default = 8
        val = input(f"Exhale duration in seconds [default {default}]: ").strip()
        args.exhale = int(val) if val else default
    if args.rounds is None:
        val = input("Number of rounds (blank for infinite): ").strip()
        args.rounds = int(val) if val else None

    breathing_coach(args.inhale, args.hold, args.exhale, args.rounds)
