 # Command-Line Breathing Coach

 This Python script is a command-line breathing coach that guides you through inhale, hold, and exhale phases with both audible cues and dynamic visual feedback.

 ## Features
 - Audible cues for inhale, hold, and exhale phases using mpg123 and customizable sound files.
 - Numeric per-second countdown display for each phase.
 - Graphical hold-phase progress bar using Unicode circles.
 - Interactive prompts for any missing inhale/hold/exhale/rounds parameters.
 - Quit early by pressing `q` then Enter at any time, and receive a random supportive message.

 ## Prerequisites
 - Python 3
 - mpg123 (install via `sudo apt update && sudo apt install mpg123`)
 - Sound files (`gong-inhale.mp3`, `ding.mp3`, `gong-exhale.mp3`) placed alongside the script.
- Development dependencies: install dev tools via `pip install -r requirements-dev.txt`

 ## Usage
 ```bash
 python3 breath.py [--inhale SECONDS] [--hold SECONDS] [--exhale SECONDS] [--rounds COUNT]
 ```
 - All options are optional. If omitted, you'll be prompted for values (showing defaults).
 - `--rounds` blank or omitted runs indefinitely.
 - Press `q` then Enter at any time during execution to quit with an encouraging message.

 ### Options
 - `--inhale`: inhale duration in seconds (default: 4)
 - `--hold`:   hold duration in seconds (default: 0)
 - `--exhale`: exhale duration in seconds (default: 8)
 - `--rounds`: number of cycles (blank for infinite)

 ### Examples
 - Basic run with defaults (prompts):
   ```bash
   python3 breath.py
   ```
 - 4-7-8 cycle for 5 rounds:
   ```bash
   python3 breath.py --inhale 4 --hold 7 --exhale 8 --rounds 5
   ```
 - 6-0-6 cycle indefinitely:
   ```bash
   python3 breath.py --inhale 6 --exhale 6
   ```