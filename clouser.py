from timeit import repeat

def make_repeaterOf(n):
    def repeater (string):
        assert type(string)==str,'solo puede usar cadenas'
        return string *n 
    return repeater

def run():
    repeat_5 = make_repeaterOf(5)
    print(repeat_5('hola'))
    repeat_2 =make_repeaterOf(2)
    print(repeat_2('RAUL'))


if __name__ == '__main__':
    run()
