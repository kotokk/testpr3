from behave import given, when, then
from polechudes import PoleChudesGame, is_valid_letter  # Замените 'your_module' на фактическое имя модуля

@given('a PoleChudesGame instance with word "{word}" topic "{topic}" and hints {hints}')
def step_given_pole_chudes_game(context, word, topic, hints):
    context.game = PoleChudesGame(word, topic, hints)

@when('the user input a valid letter "{letter}"')
def step_when_user_input_valid_letter(context, letter):
    context.is_valid = is_valid_letter(letter, context.game)

@when('the user input an empty string')
def step_when_user_input_empty_string(context):
    context.is_valid = is_valid_letter("", context.game)

@when('the user input a non-alphabetic character "{character}"')
def step_when_user_input_non_alphabetic(context, character):
    context.is_valid = is_valid_letter(character, context.game)

@when('the player has already guessed the letter "{letter}"')
def step_when_player_already_guessed_letter(context, letter):
    context.game.guessed_letters.add(letter)

@when('the user input the same letter "{letter}" again')
def step_when_user_input_same_letter_again(context, letter):
    context.is_valid = is_valid_letter(letter, context.game)

@then('the letter should be considered valid')
def step_then_letter_valid(context):
    assert context.is_valid is True

@then('the input should be considered invalid')
def step_then_input_invalid(context):
    assert context.is_valid is False

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    # Add assertions for error message display if applicable
    pass
