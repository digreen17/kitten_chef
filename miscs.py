import secrets
import string
import datetime
import json


def generate_random_password(length=15):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def current_time():
    return datetime.datetime.now()


def convert_datetime_in_feed(time):
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    month_idx = time.month - 1
    return time.strftime("%d {} %Y %H:%M").format(months[month_idx])


def convert_datetime_in_chat(time):
    return time.strftime("%d.%m.%Y %H:%M:%S")


def process_recipe(recipe_form):
    ingredients = []
    steps = []

    ingredient_names = recipe_form.getlist('ingredient_name')
    ingredient_amounts = recipe_form.getlist('ingredient_amount')

    step_titles = recipe_form.getlist('step_title')
    step_durations = recipe_form.getlist('step_duration')
    step_descriptions = recipe_form.getlist('step_description')

    for name, amount in zip(ingredient_names, ingredient_amounts):
        ingredients.append({'name': name, 'amount': amount})

    for title, duration, description in zip(step_titles, step_durations,
                                            step_descriptions):
        steps.append({'title': title, 'duration': duration,
                      'description': description})

    ingredients_json = json.dumps(ingredients)
    steps_json = json.dumps(steps)

    return ingredients_json, steps_json