Feature: Validate Input Letter for PoleChudesGame

  Scenario: Valid input letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the user input a valid letter "А"
    Then the letter should be considered valid

  Scenario: Empty input
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the user input an empty string
    Then the input should be considered invalid
    And an error message should be displayed

  Scenario: Non-alphabetic input
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the user input a non-alphabetic character "#"
    Then the input should be considered invalid
    And an error message should be displayed

  Scenario: Already guessed letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    And the player has already guessed the letter "А"
    When the user input the same letter "А" again
    Then the input should be considered invalid
    And an error message should be displayed
