import defe

while True:
    text = input('SC >')

    result, error = defe.run('<srdin>', text)

    if error: 
        print(error.as_string())
    else:
        print(result)