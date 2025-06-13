from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def function_wrapper():
        return f"<b>{function()}</b>"
    return function_wrapper

def make_emphasis(function):
    def function_wrapper():
        return f"<em>{function()}</em>"
    return function_wrapper

def make_underlined(function):
    def function_wrapper():
        return f"<u>{function()}</u>"
    return function_wrapper

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"<h1 style='text-align: center'>Hello there {name}" \
    f"you are {age} years old!!!!!!</h1><p>This is a paragraph</p>" \
    f"<img src='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQd1kWKsODGmz1P44kiLTfpeIOkaemYITnaRVOZEn372xCyrpNoQQ_dMDAV4dWLpVTDFekNEtlkJaDnhlTzoQWdNg' width=200>"

if __name__ == "__main__":
    app.run(debug=True)