from behave import given, when, then

@then('Click on each products and verify correct product_page is opened')
def click_product(context):
    context.app.product_page.click_and_verify_product()




