from behave import given, when, then

@when('Click on PROCEED TO CHECKOUT button')
def click_checkout(context):
    context.app.cart_page.click_checkout()

@then('Verify user can see cart page after clicking shopping cart')
def cart_page_displayed(context):
    context.app.cart_page.cart_page_displayed()
