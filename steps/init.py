from polechudes import PoleChudesGame
from behave import given, when, then


@given('a PoleChudesGame with word "{word}", topic "{topic}", and hints {hints}')
def step_given_pole_chudes_game(context, word, topic, hints):
    context.game = PoleChudesGame(word, topic, hints)

@when('the game is initialized')
def step_when_game_initialized(context):
    pass  # Initialization is already done in the 'given' step

@then('the word is "{expected_word}"')
def step_then_word(context, expected_word):
    assert context.game.word == expected_word.upper()

@then('the hidden word is "{expected_hidden_word}"')
def step_then_hidden_word(context, expected_hidden_word):
    assert "".join(context.game.hidden_word) == expected_hidden_word

@then('the topic is "{expected_topic}"')
def step_then_topic(context, expected_topic):
    assert context.game.topic == expected_topic

@then('the hints are {expected_hints}')
def step_then_hints(context, expected_hints):
    assert context.game.hints == eval(expected_hints)

@then('the guessed letters are empty')
def step_then_guessed_letters_empty(context):
    assert not context.game.guessed_letters

@then('the scores are set to 0')
def step_then_scores_set_to_0(context):
    assert context.game.player1_score == 0
    assert context.game.player2_score == 0

@then('the current turn score is 0')
def step_then_current_turn_score_0(context):
    assert context.game.current_turn_score == 0

@then('the total score is 0')
def step_then_total_score_0(context):
    assert context.game.total_score == 0

@then('it is Player 1\'s turn')
def step_then_player1_turn(context):
    assert context.game.player_turn == 1

