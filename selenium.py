from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up WebDriver (make sure you have the right driver for your browser)
driver = webdriver.Chrome()

def test_operation(num1, num2, operation, expected_result):
    """Helper function to test calculator operations."""
    num1_input = driver.find_element(By.ID, "num1")
    num2_input = driver.find_element(By.ID, "num2")
    result_span = driver.find_element(By.ID, "result")

    # Clear previous result
    driver.execute_script("arguments[0].innerText = '';", result_span)

    # Input values
    num1_input.clear()
    num1_input.send_keys(str(num1))

    num2_input.clear()
    num2_input.send_keys(str(num2))

    # Click operation button
    button = driver.find_element(By.XPATH, f"//button[contains(text(), '{operation}')]")
    button.click()

    # Wait for result to update
    try:
        WebDriverWait(driver, 10).until(lambda d: result_span.text.strip() != "")
        result_text = result_span.text.strip()
        print(f"Test {num1} {operation} {num2} = {result_text}")

        # Assert result matches expected output
        assert result_text == str(expected_result), f"Test failed: Expected {expected_result}, got {result_text}"
        print("✅ Test Passed!")
    except TimeoutException:
        print("❌ Test failed: Result not updated in time")

try:
    # Open the frontend calculator page (adjust path accordingly)
    driver.get("file:///C:/Users/JARVIS/OneDrive/Desktop/ST/calculator.html")

    # Wait for inputs to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "num1")))

    # Test cases
    test_operation(10, 5, "Add", 15)         # Addition Test
    test_operation(10, 5, "Subtract", 5)     # Subtraction Test
    test_operation(10, 5, "Multiply", 50)    # Multiplication Test
    test_operation(10, 5, "Divide", 2)       # Division Test
    test_operation(10, 0, "Divide", "Division by zero is not allowed")  # Division by zero

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
