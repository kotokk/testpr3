from behave import given, when, then
from polechudes import PoleChudesGame  # Замените 'your_module' на фактическое имя модуля

@given('a PoleChudesGame instance with word "{word}" topic "{topic}" and hints {hints}')
def step_given_pole_chudes_game(context, word, topic, hints):
    context.game = PoleChudesGame(word, topic, hints)

@when('the player guesses the correct letter "{letter}"')
def step_when_player_guesses_correct_letter(context, letter):
    context.guess_result = context.game.guess_letter(letter)

@when('the player guesses the incorrect letter "{letter}"')
def step_when_player_guesses_incorrect_letter(context, letter):
    context.guess_result = context.game.guess_letter(letter)

@then('the hidden word should be updated')
def step_then_hidden_word_updated(context):
    assert context.guess_result is True
    # Add additional assertions if needed

@then('the player\'s score should be updated')
def step_then_player_score_updated(context):
    assert context.game.current_turn_score > 0
    # Add additional assertions if needed

@then('the hidden word should not be updated')
def step_then_hidden_word_not_updated(context):
    assert context.guess_result is False
    # Add additional assertions if needed

@then('the player\'s score should remain the same')
def step_then_player_score_not_updated(context):
    assert context.game.current_turn_score == 0
    # Add additional assertions if needed
