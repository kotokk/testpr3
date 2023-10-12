from behave import given, when, then
from your_module import PoleChudesGame  # Замените 'your_module' на фактическое имя модуля

@given('a PoleChudesGame instance with word "{word}" topic "{topic}" and hints {hints}')
def step_given_pole_chudes_game(context, word, topic, hints):
    context.game = PoleChudesGame(word, topic, hints)

@when("it's player 1's turn")
def step_when_player_1_turn(context):
    context.game.player_turn = 1

@when("it's player 2's turn")
def step_when_player_2_turn(context):
    context.game.player_turn = 2

@when('the current turn score is {score:d}')
def step_when_current_turn_score(context, score):
    context.game.current_turn_score = score

@when('the scores are updated')
def step_when_scores_updated(context):
    context.game.update_scores()

@then("player 1's total score should be updated by {score:d}")
def step_then_player_1_score_updated(context, score):
    assert context.game.player1_score == score

@then("player 2's total score should be updated by {score:d}")
def step_then_player_2_score_updated(context, score):
    assert context.game.player2_score == score
