from behave import given, when, then

@given('Open gettop page')
def open_gettop(context):
    context.app.main_page.open_gettop()

@then('Hover over WATCH')
def hover_over_watch(context):
    context.app.header.hover_watch()

@then('Verify {expected_count} items are shown under watch category')
def verify_number_of_items(context,expected_count):
    context.app.header.verify_number_of_items(expected_count)

@then('Click on WATCH')
def click_watch(context):
    context.app.header.click_watch()

@when('Hover over MAC')
def hover_over_mac(context):
    context.app.header.hover_over_MAC()

@then('Verify {expected_count} items are shown under MAC category')
def verify_all_mac_items(context,expected_count):
    context.app.header.verify_all_mac_items(expected_count)

@when('Hover over MAC and click on each products and verify correct product_page opens')
def hover_and_click_mac_product(context):
    context.app.header.hover_and_click_mac_product()