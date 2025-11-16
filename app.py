import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome
driver = webdriver.Chrome()

# Load the local HTML file
file_path = "file://" + os.path.abspath("sum.html")
driver.get(file_path)

time.sleep(2)   # give the browser time to load

# Get the displayed text
result_text = driver.find_element(By.ID, "result").text
print("Displayed Result:", result_text)

# Validate using assertion
assert result_text == "Sum = 12", "Test Failed: Incorrect sum displayed"

print("Test Passed: Output is correct!")

driver.quit()
