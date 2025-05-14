import time
import argparse
import os

def play_sound(sound_file):
    """Plays the sound file using mpg123 with quiet output."""
    os.system(f"mpg123 -q {sound_file} &")

def breathing_coach(inhale, hold, exhale, rounds):
    print("Breathing coach started. Press Ctrl+C to stop.")
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
                time.sleep(1)
            print("Inhale... Done")

            if hold > 0:
                print("Hold...", end='\r')
                for i in range(int(hold), 0, -1):
                    play_sound("ding.mp3")
                    print(f"Hold... {i}", end='\r')
                    time.sleep(1)
                print("Hold... Done")

            print("Exhale...", end='\r')
            play_sound("gong-exhale.mp3")
            for i in range(int(exhale), 0, -1):
                print(f"Exhale... {i}", end='\r')
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
                time.sleep(1)
            print("Inhale... Done")

            if hold > 0:
                print("Hold...", end='\r')
                for i in range(int(hold), 0, -1):
                    play_sound("ding.mp3")
                    print(f"Hold... {i}", end='\r')
                    time.sleep(1)
                print("Hold... Done")

            print("Exhale...", end='\r')
            play_sound("gong-exhale.mp3")
            for i in range(int(exhale), 0, -1):
                print(f"Exhale... {i}", end='\r')
                time.sleep(1)
            print("Exhale... Done")
        print(f"\nCompleted {rounds} rounds. Exiting.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A command-line breathing coach.")
    parser.add_argument("--inhale", type=int, default=4, help="Inhale duration in seconds.")
    parser.add_argument("--hold", type=int, default=0, help="Hold duration in seconds.")
    parser.add_argument("--exhale", type=int, default=8, help="Exhale duration in seconds.")
    parser.add_argument("--rounds", type=int, default=None, help="Number of breathing cycles to perform (optional).")
    args = parser.parse_args()

    breathing_coach(args.inhale, args.hold, args.exhale, args.rounds)
