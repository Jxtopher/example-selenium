from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


def get_full_page(driver: webdriver, url: str, out_path_png: str) -> None:
    driver.get(url)

    for _ in range(1000):
        driver.execute_script("window.scrollBy(0,10);")
        sleep(0.0001)

    for _ in range(1000):
        driver.execute_script("window.scrollBy(0,-20);")
        sleep(0.0001)

    driver.find_element(By.TAG_NAME, "body").screenshot(out_path_png)


def get_short_page(driver: webdriver, url: str, out_path_png: str) -> None:
    driver.get(url)
    driver.execute_script("window.scrollBy(0,0);")
    sleep(1)
    driver.get_screenshot_as_file(out_path_png)


def get_driver_firefox():
    options = Options()
    options.headless = True
    options.binary = "/usr/bin/firefox"
    return webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options,
    )


def get_driver_chrome():
    options = Options()
    options.headless = True

    linux_chrome_path = {
        "binary_location": "/opt/chrome-linux/chrome",
        "executable_path": "/opt/chrome-linux/chromedriver",
    }

    options.binary = linux_chrome_path["binary_location"]
    return webdriver.Chrome(
        executable_path=linux_chrome_path["executable_path"],
        options=options,
    )


if __name__ == "__main__":
    domain = "https://example.com"

    driver = get_driver_firefox()
    driver.get(domain)
    get_full_page(driver, domain + "/", "/home/user/results/example-full.png")
    get_short_page(driver, domain + "/", "/home/user/results/example-short.png")

    driver.close()
