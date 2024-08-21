from collections import namedtuple
import random
import time


def main():

    """
    Experiment to determine whether named tuples cause
    a performance slowdown compared to ordinary tuples.

    SPOILER ALERT
    They do, by around 10%.

    This code creates a large number of named tuples 
    and ordinary tuples containing x and y coordinates,
    calculates the times taken for each,
    and then outputs the percentage difference.
    """

    print("--------------------")
    print("| codedrome.com    |")
    print("| Named Tuple      |")
    print("| Performance Test |")
    print("--------------------\n")

    iterations = 1_000_000

    # declare a namedtuple for later use
    Point = namedtuple("Point", "x, y")

    random.seed(42)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # pick up a time value just before starting the loop 
    start_nt = time.perf_counter()

    for i in range(iterations):
    
        # create a Point named tuple with random values
        point = Point(random.randint(0, 24) , random.randint(0, 16))
        
        # read the values into variables
        # this is just to include access in the test
        x = point.x
        x = point.y

    # pick up another time value just after the loop finishes
    end_nt = time.perf_counter()

    # calculate the ellapsed time
    # (nb according to the official Python documentation
    #  https://docs.python.org/3/library/time.html
    #  this is the only meaningful use for values obtained
    #  using time.perf_counter(). It states:
    #  "The reference point of the returned value is undefined...")
    duration_nt = end_nt - start_nt

    print(f"time taken with namedtuple:                  {duration_nt}s")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # This is a repeat of the previous code with ordinary tuples

    start_t = time.perf_counter()

    for i in range(iterations):
    
        point = (random.randint(0, 24) , random.randint(0, 16))
        
        x = point[0]
        x = point[1]

    end_t = time.perf_counter()

    duration_t = end_t - start_t

    print(f"time taken with tuple:                       {duration_t}s")

    difference = round( (duration_t / duration_nt) * 100, 2)

    print(f"tuple time as percentage of namedtuple time  {difference}%")    


if __name__ == "__main__":

    main()
