from appium import webdriver
import time

# Настройки для подключения к Appium
desired_caps = {
    "platformName": "Android",
    "platformVersion": "13",  
    "deviceName": "sm-N770f/DSM",           
    "appPackage": "com.google.android.calculator",
    "appActivity": ".Calculator",
    "noReset": True,
}

# Подключение к Appium серверу
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

def test_addition():
    driver.find_element_by_id("com.google.android.calculator:id/digit_2").click()
    driver.find_element_by_id("com.google.android.calculator:id/op_add").click()
    driver.find_element_by_id("com.google.android.calculator:id/digit_3").click()
    driver.find_element_by_id("com.google.android.calculator:id/eq").click()
    result = driver.find_element_by_id("com.google.android.calculator:id/result_final").text
    assert result == '5', f"Expected 5 but got {result}"

def test_subtraction():
    driver.find_element_by_id("com.google.android.calculator:id/digit_5").click()
    driver.find_element_by_id("com.google.android.calculator:id/op_sub").click()
    driver.find_element_by_id("com.google.android.calculator:id/digit_2").click()
    driver.find_element_by_id("com.google.android.calculator:id/eq").click()
    result = driver.find_element_by_id("com.google.android.calculator:id/result_final").text
    assert result == '3', f"Expected 3 but got {result}"

def test_multiplication():
    driver.find_element_by_id("com.google.android.calculator:id/digit_4").click()
    driver.find_element_by_id("com.google.android.calculator:id/op_mul").click()
    driver.find_element_by_id("com.google.android.calculator:id/digit_2").click()
    driver.find_element_by_id("com.google.android.calculator:id/eq").click()
    result = driver.find_element_by_id("com.google.android.calculator:id/result_final").text
    assert result == '8', f"Expected 8 but got {result}"

def test_division():
    driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
    driver.find_element_by_id("com.google.android.calculator:id/op_div").click()
    driver.find_element_by_id("com.google.android.calculator:id/digit_4").click()
    driver.find_element_by_id("com.google.android.calculator:id/eq").click()
    result = driver.find_element_by_id("com.google.android.calculator:id/result_final").text
    assert result == '2', f"Expected 2 but got {result}"

# Запуск тестов
try:
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
finally:
    time.sleep(5)  # Задержка для просмотра результата перед закрытием
    driver.quit()
