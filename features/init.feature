Feature: Initialization of PoleChudesGame

  Scenario: Initializing PoleChudesGame with valid input
    Given a word "PYTHON" and a topic "Programming" with hints ["Easy", "Fun"]
    When I initialize a PoleChudesGame with the given word, topic, and hints
    Then the word should be "PYTHON" and the topic should be "Programming"
    And the hidden word should be ["_", "_", "_", "_", "_", "_"]
    And the hints should be ["Easy", "Fun"]
    And guessed letters should be an empty set
    And player 1 score should be 0
    And player 2 score should be 0
    And current turn score should be 0
    And total score should be 0
    And player turn should be 1

  Scenario: Initializing PoleChudesGame with an empty word
    Given an empty word and a topic "Programming" with hints ["Easy", "Fun"]
    When I initialize a PoleChudesGame with the given word, topic, and hints
    Then the initialization should raise an error with the message "Word cannot be empty"

  Scenario: Initializing PoleChudesGame with invalid characters in the word
    Given a word "12345" and a topic "Programming" with hints ["Easy", "Fun"]
    When I initialize a PoleChudesGame with the given word, topic, and hints
    Then the initialization should raise an error with the message "Word can only contain alphabetic characters"
