from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# FIX: Added regression test targeting the string-comparison bug, identified with Claude Code Agent mode.
def test_guess_too_low_single_digit_vs_two_digit():
    # Regression: the old fallback used string comparison, so check_guess(9, 50)
    # returned "Too High" because "9" > "50" lexicographically.
    # With numeric comparison, 9 < 50, so it must be "Too Low".
    result = check_guess(9, 50)
    assert result == "Too Low"
