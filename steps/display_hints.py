from behave import given, when, then
from polechudes import PoleChudesGame  # Подставьте правильное имя файла

@given('a PoleChudesGame with word "{word}", topic "{topic}", and hints {hints}')
def step_given_polechudes_game(context, word, topic, hints):
    context.game = PoleChudesGame(word, topic, hints)

@when('the display_hints function is called')
def step_when_display_hints_called(context):
    context.result = context.game.display_hints()

@then('it should return "{expected_result}"')
def step_then_check_result(context, expected_result):
    assert context.result == expected_result
