from behave import given, when, then

@given('Open gettop login page')
def open_login_page(context):
    context.app.main_page.open_login_page()

@then('Verify email,password and remember me UI elements are present in the login page')
def verify_UI_elements(context):
    context.app.login_page.verify_UI_elements()

@when('Verify {expected_text} UI element is present')
def verify_login(context,expected_text):
    context.app.login_page.verify_login_button(expected_text)

@then('Verify {expected_text} ui element is present')
def verify_lost_your_password(context,expected_text):
    context.app.login_page.lost_your_password(expected_text)

@when('Click on Lost your password link')
def click_lost_your_password(context):
    context.app.login_page.click_lost_your_password()

@then('Verify Reset password link is displayed')
def verify_verify_reset_password(context):
    context.app.login_page.verify_reset_password_link()

@then('Verify User can see Best Selling, Latest, Top Rated blocks')
def verify_footer_title(context):
    context.app.login_page.verify_footer_title()