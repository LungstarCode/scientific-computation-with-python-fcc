

def square_root_bisection(square_target, tolerance=1e-7, max_iterations= 100):
    if square_target < 0:
        raise ValueError('square root of a negative number is not defined in real numbers!')
    
    if square_target == 1:
        print(f'The square root of {square_target} is 1')

    elif square_target == 0:
        print(f'The square root of {square_target} is 0')