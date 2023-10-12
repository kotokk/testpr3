Feature: Testing PoleChudesGame display_hints function

Scenario: Display hints for PoleChudesGame
    Given a PoleChudesGame with word "PYTHON", topic "Programming" and hints ["High-level", "Interpreted"]
    When the display_hints function is called
    Then it should return "High-level, Interpreted"
