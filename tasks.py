# # from robocorp.tasks import task
# # from robocorp import browser
# # # @task
# # # def minimal_task():
# #     # message = "Hello"
# #     # message = message + " World!"

# # @task
# # def robot_spare_bin_python():
# #     """Insert the sales data for the week and export it as a PDF"""
# #     open_the_intranet_website()

# # def open_the_intranet_website():
# #     """Navigates to the given URL"""
# #     browser.goto("https://robotsparebinindustries.com/")

from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(
        slowmo=100000,
    )
    open_the_intranet_website()
    login()
    fill_and_submit_sales_form()

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")
    # browser.goto("https://www.google.com/maps")

def login():
    """Fills in the login form and clicks the 'Log in' button"""
    page=browser.page()
    page.fill("#username","maria")
    page.fill("#password","thoushallnotpass")
    page.click("button:text('Log in')")

def fill_and_submit_sales_form():
    """Fills in the sales data and click the 'Submit' button"""
    page = browser.page()

    page.fill("#firstname", "John")
    page.fill("#lastname", "Smith")
    page.fill("#salesresult", "123")
    page.select_option("#salestarget", "10000")
    page.click("text=Submit")
    
# 
# from robocorp.tasks import task
# from robocorp import browser
# from RPA.Browser.Selenium import Selenium


# sel = Selenium()
# @task

# def robot_spare_bin_python():
#     print("there")
#     browser.configure(
#         slowmo=100000,
#     )
#     """Insert the sales data for the week and export it as a PDF"""
#     open_the_intranet_website()
#     log_in()

# def open_the_intranet_website():
#     """Navigates to the given URL"""
#     print("hello")
#     sel.open_available_browser("https://robotsparebinindustries.com/")
#     # browser.goto("https://robotsparebinindustries.com/")

# def log_in():
#     """Fills in the login form and clicks the 'Log in' button"""