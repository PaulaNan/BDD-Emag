from behave import *


@when('cart: I click on favorite button')
def step_impl(context):
    context.cart_page.click_favorite_btn()


@when('cart: I verify cart is empty')
def step_impl(context):
    context.cart_page.verify_empty_cart_msg()


@then('favorite: I verify favorite page url')
def step_impl(context):
    context.favorite_page.verify_url_page()


@when('cart: I click favorite button')
def step_impl(context):
    context.favorite_page.click_favorite_link()

@when('favorite: I click favorite button')
def step_impl(context):
    context.cart_page.verify_empty_cart_msg()
