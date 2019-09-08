ss = input().strip()

def solve(eq,val='X'):
    eq1 = eq.replace("=","-(") + ")"
    c = eval(eq1,{val:1j})
    a = -c.real / c.imag
    return (a)

if __name__=="__main__":

    res = solve(ss,'X')