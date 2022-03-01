from numpy import square


def run():
    """
    squares = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)
    print(squares)
    """
    # Otra manera de escribirlo sería así
    # [element for element in iterable if condition]
    
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

if __name__ == '__main__':
    run()