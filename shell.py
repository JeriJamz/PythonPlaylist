import Lingo

while True:
    text = input('SC >')

    result, error = Lingo.run('<srdin>', text)

    if error: 
        print(error.as_string())
    else:
        print(result)
