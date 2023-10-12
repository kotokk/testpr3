Feature: Guess Letter in PoleChudesGame

  Scenario: Guessing a correct letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the player guesses the correct letter "P"
    Then the hidden word should be updated
    And the player's score should be updated

  Scenario: Guessing an incorrect letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the player guesses the incorrect letter "Z"
    Then the hidden word should not be updated
    And the player's score should remain the same
