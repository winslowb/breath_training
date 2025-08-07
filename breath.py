#!/usr/bin/env python3

import time
import argparse
import os
import subprocess
import sys
import select
import random
import json
from datetime import datetime

try:
    # Try using playsound if available for better cross-platform audio
    from playsound import playsound
    import threading
    HAVE_PLAYSOUND = True
except ImportError:
    HAVE_PLAYSOUND = False

# For curses mode (optional)
try:
    import curses
    HAVE_CURSES = True
except ImportError:
    HAVE_CURSES = False

QUIT_MESSAGES = [
    "Keep going, you're doing amazing!",
    "Nice session! Remember to breathe and smile.",
    "Great job today—stay calm and carry on!",
    "You rock! Take a moment to appreciate your progress.",
    "Well done! See you next time for more mindful breaths."
]

def check_quit(window=None):
    if window:
        window.nodelay(True)
        c = window.getch()
        if c in [ord('q'), ord('Q')]:
            window.clear()
            window.addstr(0, 0, random.choice(QUIT_MESSAGES))
            window.refresh()
            time.sleep(1)
            sys.exit(0)
    else:
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            line = sys.stdin.readline().strip()
            if line.lower() == 'q':
                print("\n" + random.choice(QUIT_MESSAGES))
                sys.exit(0)


def play_sound_async(sound_file, enable_audio=True):
    if not enable_audio:
        return
    if HAVE_PLAYSOUND:
        try:
            threading.Thread(target=playsound, args=(sound_file,), kwargs={"block": True}, daemon=True).start()
        except Exception:
            pass
    else:
        try:
            subprocess.Popen(["mpg123", "-q", sound_file])
        except Exception:
            pass


def countdown(phase_name, seconds, sound_file=None, enable_audio=True, window=None):
    if sound_file:
        play_sound_async(sound_file, enable_audio)
    for i in range(int(seconds), 0, -1):
        bar_length = 20
        filled = int(((seconds - i + 1) / seconds) * bar_length)
        bar = '●' * filled + '○' * (bar_length - filled)
        line = f"{phase_name:<22} {i:2d}s {bar}"
        if window:
            window.clear()
            window.addstr(0, 0, line)
            window.refresh()
        else:
            print(line, end='\r', flush=True)
        check_quit(window)
        time.sleep(1)
    end_line = f"{phase_name:<22} Done {'●' * 20}"
    if window:
        window.clear()
        window.addstr(0, 0, end_line)
        window.refresh()
        time.sleep(1)
    else:
        print(end_line)


def log_session(rounds_completed):
    log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Completed {rounds_completed} rounds.\n"
    with open("session_log.txt", "a") as log_file:
        log_file.write(log_line)


def load_config():
    config_path = "config.json"
    defaults = {
        "inhale": 4,
        "hold": 4,
        "exhale": 4,
        "hold2": 4,
        "rounds": None,
        "enable_audio": True
    }
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as fp:
                config = json.load(fp)
            defaults.update(config)
        except Exception:
            pass
    return defaults


def breathing_coach(inhale, hold, exhale, hold2, rounds, enable_audio=True, use_curses=False):
    if not use_curses:
        print("\n🧘 Breathing coach started. Press 'q' then Enter at any time to quit.\n")
        print("🧾 Breath Cycle Summary:")
        print(f"   Inhale          : {inhale} sec")
        print(f"   Hold (after in) : {hold} sec")
        print(f"   Exhale          : {exhale} sec")
        print(f"   Hold (after ex) : {hold2} sec")
        print(f"   Rounds          : {rounds if rounds else '∞'}\n")
        time.sleep(6)
        print("Starting in...")
        for i in range(4, 0, -1):
            print(f"   {i}", end='\r', flush=True)
            time.sleep(1)
        print("   Begin!            ")

    def run_round(round_num, window=None):
        if not use_curses:
            os.system('clear')
            print(f"Round {round_num}\n")
        else:
            window.clear()
            window.addstr(0, 0, f"Round {round_num}\n")
            window.refresh()
        countdown("Inhale", inhale, "gong-inhale.mp3", enable_audio, window)
        if hold > 0:
            countdown("Hold (after inhale)", hold, "ding.mp3", enable_audio, window)
        countdown("Exhale", exhale, "gong-exhale.mp3", enable_audio, window)
        if hold2 > 0:
            countdown("Hold (after exhale)", hold2, "ding.mp3", enable_audio, window)

    if rounds is None or rounds <= 0:
        round_count = 0
        try:
            if not use_curses:
                while True:
                    round_count += 1
                    run_round(round_count)
            else:
                stdscr = curses.initscr()
                while True:
                    round_count += 1
                    run_round(round_count, stdscr)
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        if not use_curses:
            for round_count in range(1, int(rounds) + 1):
                run_round(round_count)
        else:
            stdscr = curses.initscr()
            for round_count in range(1, int(rounds) + 1):
                run_round(round_count, stdscr)
        print(f"\nCompleted {rounds} rounds. Exiting.\n")
        log_session(rounds)


def main(use_curses=False):
    defaults = load_config()

    parser = argparse.ArgumentParser(description="A command-line breathing coach with audio and visual cues.")
    parser.add_argument("--inhale", type=int, default=defaults["inhale"], help="Inhale duration in seconds.")
    parser.add_argument("--hold", type=int, default=defaults["hold"], help="Hold (after inhale) duration in seconds.")
    parser.add_argument("--exhale", type=int, default=defaults["exhale"], help="Exhale duration in seconds.")
    parser.add_argument("--hold2", type=int, default=defaults["hold2"], help="Hold (after exhale) duration in seconds.")
    parser.add_argument("--rounds", type=int, default=defaults["rounds"], help="Number of cycles (<=0 for infinite).")
    parser.add_argument("--no-sound", action="store_true", help="Disable audio cues.")
    parser.add_argument("--use-curses", action="store_true", help="Use curses for UI display.")
    args = parser.parse_args()

    enable_audio = defaults["enable_audio"] and (not args.no_sound)

    if args.use_curses and not HAVE_CURSES:
        print("Curses module not available. Running in console mode.")
        args.use_curses = False

    breathing_coach(
        args.inhale,
        args.hold,
        args.exhale,
        args.hold2,
        args.rounds,
        enable_audio=enable_audio,
        use_curses=args.use_curses
    )


if __name__ == "__main__":
    try:
        if "--use-curses" in sys.argv:
            curses.wrapper(lambda stdscr: main(use_curses=True))
        else:
            main(use_curses=False)
    except KeyboardInterrupt:
        sys.exit(0)
