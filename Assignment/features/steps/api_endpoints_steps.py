from behave import given, when, then
from django.test import Client
from django.urls import reverse
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Assignment.settings")  # Replace with your project name
django.setup()

@given('I am on the home page')
def step_impl(context):
    context.client = Client()
    context.url = reverse('home')
    context.response = context.client.get(context.url)
    assert context.response.status_code == 200


@when('I select "{option}"')
def step_impl(context, option):
    context.selected_option = option
    if option == "POST CREATE USER":
        context.response = context.client.post(context.url, {"option": option, "name": "Jane Doe", "job": "Developer"})
    else:
        context.response = context.client.get(context.url, {"option": option})


@then('I should see the response status code "{status_code}"')
def step_impl(context, status_code):
    actual_status_code = str(context.response.status_code)
    print(f"Expected: {status_code}, Actual: {actual_status_code}")  # Debugging print statement
    assert actual_status_code == status_code, f"Assertion Failed: Expected {status_code}, but got {actual_status_code}"


@then('I should see the response contains "{text}"')
def step_impl(context, text):
    response_json = json.loads(context.response.content)
    response_str = json.dumps(response_json, indent=4)
    print(f"Actual response: {response_str}")  # Debugging print statement
    assert text in response_str, f"Assertion failed. '{text}' not found in: {response_str}"
