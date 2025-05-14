# Command-Line Breathing Coach

This Python script is a command-line tool designed to guide you through various breathing exercises. It provides both audible cues (using `mpg123` on Linux) and a dynamic visual countdown for each phase of your breathing cycle. You can configure the inhale, hold, and exhale durations, as well as the number of rounds you want to perform.

## Prerequisites

* **Python 3:** You need to have Python 3 installed on your system.
* **mpg123:** For the audible cues, this script uses `mpg123`. You can install it on Ubuntu using:
    ```bash
    sudo apt update
    sudo apt install mpg123
    ```
* **Sound Files:** You'll need three sound files:
    * `gong-inhale.mp3` (or your preferred inhale sound)
    * `ding.mp3` (or your preferred hold counter sound)
    * `gong-exhale.mp3` (or your preferred exhale sound)
    Place these files in the same directory as your Python script.

## How to Use

1.  **Save the script:** Save the Python code (provided in our conversation) as a `.py` file (e.g., `breathing_coach.py`).
2.  **Place sound files:** Ensure you have `gong-inhale.mp3`, `ding.mp3`, and `gong-exhale.mp3` in the same directory.
3.  **Run from the terminal:** Open your bash terminal, navigate to the directory where you saved the script, and run it using the `python3` command followed by the script name and any desired options.

    **Options:**
    * `--inhale`: Duration for inhalation in seconds (default: 4).
    * `--hold`: Duration to hold your breath in seconds (default: 0).
    * `--exhale`: Duration for exhalation in seconds (default: 8).
    * `--rounds`: Number of breathing cycles to perform (optional). If not specified, the script will run indefinitely until you press Ctrl+C.

    **Examples:**
    * Basic run with default settings:
        ```bash
        python3 breathing_coach.py
        ```
    * Run with a 4-7-8 breathing cycle for 5 rounds:
        ```bash
        python3 breathing_coach.py --inhale 4 --hold 7 --exhale 8 --rounds 5
        ```
    * Inhale for 6 seconds, no hold, exhale for 6 seconds, run indefinitely:
        ```bash
        python3 breathing_coach.py --inhale 6 --exhale 6
        ```

## Breathing Techniques to Try

Here are some breathing techniques you can practice using this tool, along with suggested configurations:

**For General Relaxation and Stress Reduction:**

* **4-7-8 Breathing (Relaxing Breath):**
    * `--inhale 4 --hold 7 --exhale 8 --rounds [desired number]`
* **Equal Breathing (Sama Vritti Pranayama):**
    * `--inhale 4 --hold 0 --exhale 4 --rounds [desired number]` (or try with a hold: `--inhale 4 --hold 4 --exhale 4`)
* **Long Exhalation Breathing:**
    * `--inhale 4 --hold 0 --exhale 6 --rounds [desired number]` (or longer exhale, e.g., `--exhale 8`)

**For Energy and Focus:**

* **(Note:** Our current script doesn't fully support the rapid breathing of techniques like Bellows Breath or Breath of Fire. However, you can experiment with faster equal breathing if it feels comfortable.)**
    * **Faster Equal Breathing (Experiment with caution):**
        * `--inhale 2 --hold 0 --exhale 2 --rounds [desired number]` (Start with a few rounds and see how you feel.)

**For Sleep:**

* **Extended Exhalation:**
    * `--inhale 4 --hold 0 --exhale 6 --rounds [desired number]`
* **Body Scan with Breath (Use as a guide):** Configure for a slow, comfortable breath (e.g., `--inhale 6 --hold 4 --exhale 8`) and mentally scan your body during the exhale.

**For Cardio Endurance and CO2 Tolerance:**

* **Buteyko-Inspired (Short Holds):**
    * `--inhale 4 --hold 2 --exhale 6 --rounds [desired number]` (Focus on a gentle hold after the exhale in your actual practice if desired.)
* **Box Breathing Variation (Extended Inhale Hold):**
    * `--inhale 4 --hold 6 --exhale 4 --rounds [desired number]` (Adjust the hold duration based on your comfort.)

**Remember:** Always listen to your body and adjust the timings to what feels comfortable and beneficial for you. If you have any health concerns, consult with a healthcare professional before starting new breathing exercises.
