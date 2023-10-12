Feature: Spin Wheel in PoleChudesGame

  Scenario: Player guesses a correct letter and spins the wheel
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the player guesses a correct letter
    And the player spins the wheel
    Then the current turn score should be updated
    And the player turn should be switched

  Scenario: Player guesses an incorrect letter and spins the wheel
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the player guesses an incorrect letter
    And the player spins the wheel
    Then the current turn score should be updated
    And the player turn should be switched
    And an additional message should be displayed if the result is "ПРИЗ"

  Scenario: Player spins the wheel without guessing a letter
    Given a PoleChudesGame instance with word "PYTHON" topic "Programming" and hints ["snake"]
    When the player spins the wheel without guessing a letter
    Then the current turn score should be updated
    And the player turn should be switched
    And an additional message should be displayed if the result is "ПРИЗ"
