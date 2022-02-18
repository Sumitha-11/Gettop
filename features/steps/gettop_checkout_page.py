from behave import given, when, then

@when('User can enter {firstname} firstname in the checkout form')
def enter_first_name(context,firstname):
    context.app.checkout_page.enter_first_name(firstname)

@when('User can enter {lastname} lastname in the checkout form')
def enter_last_name(context,lastname):
    context.app.checkout_page.enter_last_name(lastname)

@when('User can enter {company_name} company name in the checkout form')
def enter_company_name(context,company_name):
    context.app.checkout_page.enter_company_name(company_name)

@then('User can select {any} country from country drop down')
def select_country(context,any):
    context.app.checkout_page.select_country(any)

@then('User can enter {valid} street address')
def enter_street_address(context,valid):
    context.app.checkout_page.enter_street_address(valid)

@then('User can enter {correct} city')
def enter_city(context,correct):
    context.app.checkout_page.enter_city(correct)

@then('User can select {any} state')
def select_state(context,any):
    context.app.checkout_page.select_state(any)

@then('User can enter {correct} zipcode')
def enter_zipcode(context,correct):
    context.app.checkout_page.enter_zipcode(correct)

@then('User can enter {valid} phone number')
def enter_phone_number(context,valid):
    context.app.checkout_page.enter_phone_number(valid)

@then('User can enter {valid} email address')
def enter_email_address(context,valid):
    context.app.checkout_page.enter_email_address(valid)

@then('User can enter additional information if needed')
def additional_information(context):
    context.app.checkout_page.additional_information()

@then('Verify user cannot leave any required fields blank')
def required_field_not_blank(context):
    context.app.checkout_page.required_field_not_blank()

@then('Click on place order')
def click_place_order(context):
    context.app.checkout_page.click_place_order()

@then('Verify correct error message is displayed')
def error_message(context):
    context.app.checkout_page.error_message()

@when('Click on Shopping cart')
def click_shopping_cart(context):
    context.app.checkout_page.click_shopping_cart()

@then('Verify {selected_country} country is displayed')
def verify_correct_country(context,selected_country):
    context.app.checkout_page.verify_correct_country(selected_country)