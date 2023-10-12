from behave import given, when, then
from polechudes import PoleChudesGame, player_2_turn  

@given('a PoleChudesGame instance with word "{word}" topic "{topic}" and hints {hints}')
def step_given_pole_chudes_game(context, word, topic, hints):
    context.game = PoleChudesGame(word, topic, hints)

@when("it's player 2's turn")
def step_when_player_2_turn(context):
    context.current_player_turn = context.game.player_turn
    context.guessed_letters_before = set(context.game.guessed_letters)
    context.player1_score_before = context.game.player1_score
    context.player2_score_before = context.game.player2_score
    context.current_turn_score_before = context.game.current_turn_score

@then('player 2 guesses a letter')
def step_then_player_2_guesses_letter(context):
    player_2_turn(context.game)

@then('the hidden word should be updated if the guess is correct')
def step_then_hidden_word_updated(context):
    assert set(context.game.guessed_letters) != context.guessed_letters_before

@then('the player\'s score should be updated if the guess is correct')
def step_then_player_score_updated(context):
    if context.current_player_turn == 1:
        assert context.game.player1_score != context.player1_score_before
    else:
        assert context.game.player2_score != context.player2_score_before

@then('the wheel should be spun')
def step_then_wheel_spun(context):
    assert context.game.current_turn_score != context.current_turn_score_before

@then('player 2 guesses the same letter "{letter}"')
def step_then_player_2_guesses_same_letter(context, letter):
    context.is_valid = context.game.guess_letter(letter)

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    assert context.is_valid is False

@then('the hidden word should not be updated')
def step_then_hidden_word_not_updated(context):
    assert set(context.game.guessed_letters) == context.guessed_letters_before

@then('the player\'s score should remain the same')
def step_then_player_score_not_updated(context):
    if context.current_player_turn == 1:
        assert context.game.player1_score == context.player1_score_before
    else:
        assert context.game.player2_score == context.player2_score_before
