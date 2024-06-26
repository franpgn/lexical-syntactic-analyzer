import parser as parser

if __name__ == '__main__':
    while True:
        try:
            s = input('LISP > ')
        except KeyboardInterrupt:
            break
        if not s: continue
        result = parser.parse(s)

        print(f"Postfix: {result}")