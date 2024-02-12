from bottle import Bottle, request, response, HTTPError

app = Bottle()

@app.route("/")
def welcome():
    response.set_header("Vary", "Accept")
    msg = "Welcome to the Extensive String Manipulation REST API"
    if "text/html" in request.headers.get("Accept", "*/*"):
        response.content_type = "text/html"
        return f"<h1>{msg}</h1>"
    response.content_type = "text/plain"
    return msg

@app.route("/upper")
def upper_case_service():
    word = request.query.word
    if not word:
        raise HTTPError(400, "Missing 'word' parameter in the query string.")
    return word.upper()

@app.route("/lower")
def lower_case_service():
    word = request.query.word
    if not word:
        raise HTTPError(400, "Missing 'word' parameter in the query string.")
    return word.lower()

@app.route("/isPalindrome")
def palindrome_check():
    word = request.query.word
    if not word:
        raise HTTPError(400, "Missing 'word' parameter in the query string.")
    result = word == word[::-1]
    return f"{word} is {'a' if result else 'not a'} palindrome"

@app.route("/wordCount")
def word_count_service():
    phrase = request.query.phrase
    if not phrase:
        raise HTTPError(400, "Missing 'phrase' parameter in the query string.")
    return {"word_count": len(phrase.split())}

@app.route("/reverse")
def reverse_string():
    string = request.query.string
    if not string:
        raise HTTPError(400, "Missing 'string' parameter in the query string.")
    return string[::-1]

@app.route("/charCount")
def character_count():
    string = request.query.string
    if not string:
        raise HTTPError(400, "Missing 'string' parameter in the query string.")
    return {"character_count": len(string)}

@app.route("/concatenate")
def concatenate():
    strings = request.query.strings.split(',')
    if not strings or '' in strings:
        raise HTTPError(400, "Invalid or missing 'strings' parameter in the query string. Use comma to separate strings.")
    concatenated_string = ''.join(strings)
    return concatenated_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

'''

# Welcome message
curl "http://localhost:8080/"

# Current time
curl "http://localhost:8080/now"

# Convert to uppercase
curl "http://localhost:8080/upper?word=hello"

# Convert to lowercase
curl "http://localhost:8080/lower?word=HELLO"

# Check if a word is a palindrome
curl "http://localhost:8080/isPalindrome?word=madam"

# Count words in a phrase
curl "http://localhost:8080/wordCount?phrase=hello%20world"

# Reverse a string
curl "http://localhost:8080/reverse?string=hello"

# Count characters in a string
curl "http://localhost:8080/charCount?string=hello"

# Concatenate strings
curl "http://localhost:8080/concatenate?strings=hello,world"

'''