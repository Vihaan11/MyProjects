while True:
    n1 = input("Dividend ? ")
    n2 = input("Divisor ? ")
    try:
        q = int(n1) / int(n2)
        nq = int(q)
        r = int(n1) % int(n2)
        nr = int(r)
        print("The quotient is " + str(nq) + " and the remainder is " + str(nr))
    except ZeroDivisionError:
        print("Sorry, can't divide by 0")
    except:
        print("Sorry, Unrecognizable Error")