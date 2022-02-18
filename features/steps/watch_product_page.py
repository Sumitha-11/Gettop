from behave import given, when, then

@then('Click on each products and verify correct product_page is opened')
def click_product(context):
    context.app.product_page.click_and_verify_product()

@then('Click on watch series 5 product')
def click_watch_series(context):
    context.app.product_page.click_product()

@then('Add the product to cart')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()

@then('Click the Checkout button')
def click_checkout(context):
    context.app.product_page.click_checkout()

@when('Click on cart icon')
def click_cart_icon(context):
    context.app.product_page.click_cart_icon()



