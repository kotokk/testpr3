Feature: Player 2 Turn in PoleChudesGame

  Scenario: Player 2 guesses a letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When it's player 2's turn
    Then player 2 guesses a letter
    And the hidden word should be updated if the guess is correct
    And the player's score should be updated if the guess is correct
    And the wheel should be spun

  Scenario: Player 2 guesses an already guessed letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    And player 1 has already guessed the letter "А"
    When it's player 2's turn
    Then player 2 guesses the same letter "А"
    And an error message should be displayed

  Scenario: Player 2 guesses an incorrect letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When it's player 2's turn
    And player 1 has already guessed all correct letters
    Then player 2 guesses an incorrect letter "Z"
    And the hidden word should not be updated
    And the player's score should remain the same
    And the wheel should be spun
