def isBalance(s):

    st = []

    for c in s:

        if c == "(" or c == "[" or c == "{":
            st.append(c)

        elif c == ")" or c == "]" or c == "}":

            if not st: return False

            top = st[-1]

            if ((c == ')' and top != '(') or
                (c == ']' and top != '[') or
                (c == '}' and top != '{')):

                return False

            st.pop()

    return not st

if __name__ == '__main__':

    s = "[()()]{}"
    a = "[(}]{)"
    b = "Jack"

    print("true" if isBalance(s) else "false")
    print("true" if isBalance(a) else "false")
    print("true" if isBalance(b) else "false")