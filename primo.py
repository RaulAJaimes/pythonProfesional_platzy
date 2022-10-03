def serNumprimo(n: int) -> bool:
    
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def run():
    print(serNumprimo('tres'))

if __name__ == '__main__':
    run()