#!/usr/bin/env python3

import time
import argparse
import os
import subprocess
import sys
import select
import random

QUIT_MESSAGES = [
    "Keep going, you're doing amazing!",
    "Nice session! Remember to breathe and smile.",
    "Great job today—stay calm and carry on!",
    "You rock! Take a moment to appreciate your progress.",
    "Well done! See you next time for more mindful breaths."
]

def check_quit():
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        line = sys.stdin.readline().strip()
        if line.lower() == 'q':
            print("\n" + random.choice(QUIT_MESSAGES))
            sys.exit(0)

def play_sound_async(sound_file, enable_audio=True):
    if not enable_audio:
        return
    try:
        subprocess.Popen(["mpg123", "-q", sound_file])
    except Exception:
        pass

def countdown(phase_name, seconds, sound_file=None, enable_audio=True):
    if sound_file:
        play_sound_async(sound_file, enable_audio)

    for i in range(int(seconds), 0, -1):
        bar_length = 20
        filled = int(((seconds - i + 1) / seconds) * bar_length)
        bar = '●' * filled + '○' * (bar_length - filled)
        print(f"{phase_name:<22} {i:2d}s {bar}", end='\r', flush=True)
        check_quit()
        time.sleep(1)
    print(f"{phase_name:<22} Done {'●'*20}")

def breathing_coach(inhale, hold, exhale, hold2, rounds, enable_audio=True):
    print("\n🧘 Breathing coach started. Press 'q' then Enter at any time to quit.\n")

    # Summary before beginning
    print("🧾 Breath Cycle Summary:")
    print(f"   Inhale          : {inhale} sec")
    print(f"   Hold (after in) : {hold} sec")
    print(f"   Exhale          : {exhale} sec")
    print(f"   Hold (after ex) : {hold2} sec")
    print(f"   Rounds          : {rounds if rounds else '∞'}\n")

    time.sleep(6)  # ⏳ Give user time to read summary

    print("Starting in...")
    for i in range(4, 0, -1):
        print(f"   {i}", end='\r', flush=True)
        time.sleep(1)
    print("   Begin!            ")

    def run_round(round_num):
        os.system('clear')
        print(f"Round {round_num}\n")
        countdown("Inhale", inhale, "gong-inhale.mp3", enable_audio)
        if hold > 0:
            countdown("Hold (after inhale)", hold, "ding.mp3", enable_audio)
        countdown("Exhale", exhale, "gong-exhale.mp3", enable_audio)
        if hold2 > 0:
            countdown("Hold (after exhale)", hold2, "ding.mp3", enable_audio)

    if rounds is None or rounds <= 0:
        round_count = 0
        while True:
            round_count += 1
            run_round(round_count)
    else:
        for round_count in range(1, int(rounds) + 1):
            run_round(round_count)
        print(f"\nCompleted {rounds} rounds. Exiting.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A command-line breathing coach with audio and visual cues.")
    parser.add_argument("--inhale", type=int, help="Inhale duration in seconds.")
    parser.add_argument("--hold", type=int, help="Hold (after inhale) duration in seconds.")
    parser.add_argument("--exhale", type=int, help="Exhale duration in seconds.")
    parser.add_argument("--hold2", type=int, help="Hold (after exhale) duration in seconds.")
    parser.add_argument("--rounds", type=int, help="Number of breathing cycles (blank = infinite).")
    parser.add_argument("--no-sound", action="store_true", help="Disable audio cues.")
    args = parser.parse_args()

    # Prompt interactively for missing values
    def prompt(name, default):
        val = input(f"{name} [default {default}]: ").strip()
        return int(val) if val else default

    if args.inhale is None:
        args.inhale = prompt("Inhale duration (sec)", 4)
    if args.hold is None:
        args.hold = prompt("Hold after inhale (sec)", 4)
    if args.exhale is None:
        args.exhale = prompt("Exhale duration (sec)", 4)
    if args.hold2 is None:
        args.hold2 = prompt("Hold after exhale (sec)", 4)
    if args.rounds is None:
        val = input("Number of rounds (blank = infinite): ").strip()
        args.rounds = int(val) if val else None

    breathing_coach(
        args.inhale,
        args.hold,
        args.exhale,
        args.hold2,
        args.rounds,
        enable_audio=not args.no_sound
    )

