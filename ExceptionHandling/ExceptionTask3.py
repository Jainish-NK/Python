def checkString(**kwargs):
    try:
        for i in kwargs.keys():
            if type(i).__name__ != "str":
                raise TypeError("Only for String Keys valid...")
    except TypeError as e:
        return e
    return "All keys are strings."

ans = checkString(Gujarat="Gandhinagar", Bihar="Patna", patna="Lucknow")
print(ans)


def checkString(**kwargs):
    try:
        for i in kwargs.values():
            if type(i).__name__ != "str":
                raise TypeError("only string values valid...")
    except TypeError as e:
        return e
    return "All value are strings..."

ans = checkString(Guj = "gandinagar",bihar = "patna",patna="lucknow")
print(ans)