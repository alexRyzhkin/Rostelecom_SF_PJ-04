import pytest
import allure
import uuid

@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
@pytest.fixture
def web_browser(request, selenium):
    browser = selenium
    # browser.maximize_window()
    # browser.set_window_size(1920, 1080)
    browser.set_window_size(1400, 1000)

    # возвращает браузер в тест
    yield browser


    if request.node.rep_call.failed:

        try:
            browser.execute_script("document.body.bgColor = 'white';")

            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass  # игнорирует ошибки


def get_test_case_docstring(item):
    """ Эта функция получает строку документации из тестового сценария и форматирует её,
    чтобы отображать эту строку документации вместо названия тестового сценария в отчётах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ эта функция находу изменяет имена тестовых сценариев"""

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ TЭта функция изменяет имена тестовых сценариев «на лету»
    при использовании параметра --collect-only для pytest
    (для получения полного списка всех существующих тестовых сценариев)
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # Если у тестового сценария есть строка документации,нам нужно изменить его название на строку документации,
            # чтобы отображались понятные человеку отчёты и чтобы можно было автоматически импортировать
            # тестовые сценарии в систему управления тестированием.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('It is Done!')
