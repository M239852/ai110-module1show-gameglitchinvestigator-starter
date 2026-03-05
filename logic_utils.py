def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Refactored check_guess from app.py into logic_utils.py using Claude Code Agent mode.
# Fixed high/low bug: old code had a TypeError fallback using string comparison
# (e.g. "9" > "50" is True lexicographically), causing wrong outcomes for single-digit guesses.
# New implementation uses numeric comparison only and returns a plain outcome string (not a tuple).
def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome string.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
