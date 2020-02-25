from flask import Flask

test = Flask(__name__) # create a Flask instance using Flask Object

#we are going to create website so need a URL, so we need URL routing

#called DECORATOR in Python, Flask uses to define URL

@test.route('/') #base URL of website
def helloWorld():
    return "Hello World"

# # if we
# if __name__ == "__main__:
#     test.run(debug=True)