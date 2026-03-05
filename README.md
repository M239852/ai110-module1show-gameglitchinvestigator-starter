# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
   The game's purpose is to guess a secret number within a difficulty-based range. Players receive higher/lower hints after each guess and earn points based on how quickly they find the answer.

- [x] Detail which bugs you found.

   | # | Bug | Location |
   |---|-----|----------|
   | 1 | `check_guess` used a `TypeError` fallback with string comparison — `"9" > "50"` is `True` lexicographically, so single-digit guesses above a two-digit secret returned the wrong outcome | `app.py` → `check_guess` |
   | 2 | `check_guess` returned a tuple `(outcome, message)` but tests expected just the outcome string | `app.py` → `check_guess` |
   | 3 | Hard difficulty range was `1–50`, which is *easier* than Normal's `1–100` | `app.py` → `get_range_for_difficulty` |
   | 4 | `new_game` button reset the secret using hardcoded `randint(1, 100)`, ignoring the selected difficulty | `app.py` → new game handler |
   | 5 | `new_game` button did not reset `score`, `status`, or `history`, leaving stale game state | `app.py` → new game handler |
   | 6 | Info message hardcoded "between 1 and 100" regardless of difficulty | `app.py` → `st.info(...)` |
   | 7 | `attempts` was initialized to `1` on first load but reset to `0` on new game, causing an off-by-one in attempts remaining | `app.py` → session state init |
   | 8 | All functions in `logic_utils.py` raised `NotImplementedError` — none were implemented | `logic_utils.py` |

- [x] Explain what fixes you applied.

   - **Refactored `check_guess` into `logic_utils.py`** (with Claude Code Agent mode): removed the string-comparison `TypeError` fallback entirely; the new implementation compares numerically only and returns a plain outcome string instead of a tuple. Updated `app.py` to import from `logic_utils` and map outcomes to hint messages locally.
   - **Fixed Hard difficulty range**: changed from `1–50` to `1–200` so difficulty scales correctly across Easy (1–20), Normal (1–100), and Hard (1–200).
   - **Fixed `new_game` button**: replaced hardcoded `randint(1, 100)` with `randint(low, high)` so the new secret respects the selected difficulty. Also added resets for `score`, `status`, and `history`.
   - **Fixed dynamic info message**: replaced the hardcoded "between 1 and 100" string with `{low}` and `{high}` so it reflects the actual range.
   - **Fixed `attempts` initialization**: unified the starting value to `0` to match the new-game reset and eliminate the off-by-one.
   - **Implemented all `logic_utils.py` stubs**: moved `get_range_for_difficulty`, `parse_guess`, and `update_score` from `app.py` into `logic_utils.py` and updated `app.py` to import all four functions from there.
   - **Added regression test** (`test_guess_too_low_single_digit_vs_two_digit`): verifies that `check_guess(9, 50)` returns `"Too Low"`, which would have failed under the old string-comparison fallback.


## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
   ![alt text](<Screenshot 2026-03-04 at 9.57.48 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
