from selenium import webdriver
from time import sleep

# Driver settings
SLEEP_TIME = 5
SEARCH_TERM = "//script[@class='yoast-schema-graph']"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


def search_element():
    try:
        driver.find_element("xpath", SEARCH_TERM)
    except Exception as error:
        print("Element not found")
        return False
    return True


def run_web_driver():
    # Domains list
    domains = [
        "google.com",
        "facebook.com",
    ]

    # Results list
    results = []

    # Iterate domains list
    try:
        for site in domains:
            driver.get("https://" + site)
            element_search_test = search_element()
            if element_search_test:
                results.append([site, "true"])
                print([site, "true"])
            else:
                print([site, "false"])
                results.append([site, "false"])
            sleep(SLEEP_TIME)
    except Exception as error:
        print("Error checking domains: " + str(error))
    finally:
        # Show results
        print(results)
        # Close driver
        driver.close()


# Run Task
run_web_driver()
