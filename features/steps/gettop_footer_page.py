from behave import given, when, then

@then('Verify footer shows {expected_result} categories')
def verify_footer_categories(context,expected_result):
    context.app.footer_page.verify_footer_category()

@then('Verify all products in the footer have name')
def verify_product_name(context):
    context.app.footer_page.verify_product_name()

@then('Verify all products in the footer have price')
def verify_product_price(context):
    context.app.footer_page.verify_product_price()

@then('Verify {expected_count} product has rating in the footer')
def verify_product_rating(context,expected_count):
    context.app.footer_page.verify_product_rating(expected_count)

@then('Verify {expected_text} shown in footer')
def verify_copyright(context,expected_text):
    context.app.footer_page.verify_copyright(expected_text)

@then('Scroll to bottom of the page')
def scroll_bottom_page(context):
    context.app.footer_page.scroll_to_bottom()

@when('Click on footer button')
def click_footer_button(context):
    context.app.footer_page.click_footer_button()

@then('Verify GetTop logo at the top of the page')
def verify_gettop_logo(context):
    context.app.footer_page.gettop_logo_appears()

@when('Click on footer product link and verify correct footer product link opens')
def verify_footer_product_link(context):
    context.app.footer_page.verify_footer_product_link()