from app.application import Application
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'sumithasundaresa_OYSuxe'
bs_pw = 'pzDorZcYyj6xPos1Uceh'

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    #context.driver = webdriver.Chrome()
    # context.driver = webdriver.PhantomJS()
    # context.driver = webdriver.Firefox(executable_path='C:\\Users\\USER\\Automation\\Gettop-Project\\geckodriver.exe')

    # ## HEADLESS MODE ####
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized')  #
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--log-level=1")
    options.add_argument('--allow-running-insecure-content')
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--allow-insecure-localhost')
    # options.add_argument("enable-features=NetworkServiceInProcess")
    # options.add_argument("--disable-browser-side-navigation")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--ignore-ssl-errors")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")
    # options.add_argument("--log-level=3")
    # options.add_argument("--silent")
    # options.add_argument("disable-features = NetworkService")
    # options.add_argument("--always-authorize-plugins")
    # options.add_argument('--dns-prefetch-disable')
    # options.add_argument("--no-proxy-server")
    # options.add_argument("--aggressive-cache-discard")
    # options.add_argument("--disable-cache")
    # options.add_argument("--disable-application-cache")
    # options.add_argument("--disable-offline-load-stale-cache")
    # options.add_argument("--disk-cache-size=0")

    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 7 ; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument('--start-maximized')
    # options.add_argument("--disable-extensions")
    # options.add_argument('disable-infobars')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # context.driver = webdriver.Chrome(options=options,executable_path='/chromedriver.exe')

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--allow-insecure-localhost')
    # options.add_argument('--log-level=3')
    # context.driver = webdriver.Chrome(options = options,executable_path='/chromedriver.exe')

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '98',
    #     'os': 'Windows',
    #     'os_version': '7',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    # context.driver.set_page_load_timeout(30)
    # context.driver.set_window_size(1200, 600)
    context.driver.get_screenshot_as_file('gettop_screen.png')
    print(context.driver.current_url)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get_screenshot_as_file('gettop_screen1.png')
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    #print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
   # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

