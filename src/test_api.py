import pytest
import requests

BASE_URL = "http://localhost:8080"

# Welcome endpoint tests
def test_welcome():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Welcome" in response.text

# Upper case service endpoint tests
@pytest.mark.parametrize("word, expected", [("hello", "HELLO"), ("Test", "TEST"), ("123", "123")])
def test_upper_case_service(word, expected):
    response = requests.get(f"{BASE_URL}/upper?word={word}")
    assert response.status_code == 200
    assert response.text == expected

def test_upper_case_service_empty():
    response = requests.get(f"{BASE_URL}/upper?word=")
    assert response.status_code == 400

# Lower case service endpoint tests
@pytest.mark.parametrize("word, expected", [("HELLO", "hello"), ("Test", "test"), ("123", "123")])
def test_lower_case_service(word, expected):
    response = requests.get(f"{BASE_URL}/lower?word={word}")
    assert response.status_code == 200
    assert response.text == expected

def test_lower_case_service_empty():
    response = requests.get(f"{BASE_URL}/lower?word=")
    assert response.status_code == 400

@pytest.mark.parametrize("word, is_palindrome", [("madam", False), ("hello", True)])
def test_palindrome_check(word, is_palindrome):
    response = requests.get(f"{BASE_URL}/isPalindrome?word={word}")
    assert response.status_code == 200
    result_text = response.text.lower()
    assert ("not a palindrome" in result_text) == is_palindrome

# Word count endpoint tests
@pytest.mark.parametrize("phrase, count", [("hello world", 2), ("one", 1)])
def test_word_count(phrase, count):
    response = requests.get(f"{BASE_URL}/wordCount?phrase={phrase}")
    assert response.status_code == 200
    assert response.json()['word_count'] == count

def test_word_count_no_param():
    response = requests.get(f"{BASE_URL}/wordCount")
    assert response.status_code == 400

# Reverse string endpoint tests
@pytest.mark.parametrize("string, expected", [("hello", "olleh"), ("123", "321")])
def test_reverse_string(string, expected):
    response = requests.get(f"{BASE_URL}/reverse?string={string}")
    assert response.status_code == 200
    assert response.text == expected

# Character count endpoint tests
@pytest.mark.parametrize("string, expected", [("hello", 5), ("123 456", 7)])
def test_character_count(string, expected):
    response = requests.get(f"{BASE_URL}/charCount?string={string}")
    assert response.status_code == 200
    assert response.json()['character_count'] == expected

# Concatenate strings endpoint tests
@pytest.mark.parametrize("strings, expected", [("hello,world", "helloworld"), ("123,456", "123456")])
def test_concatenate(strings, expected):
    response = requests.get(f"{BASE_URL}/concatenate?strings={strings}")
    assert response.status_code == 200
    assert response.text == expected

def test_concatenate_no_param():
    response = requests.get(f"{BASE_URL}/concatenate")
    assert response.status_code == 400

# Running the tests
if __name__ == "__main__":
    pytest.main()
