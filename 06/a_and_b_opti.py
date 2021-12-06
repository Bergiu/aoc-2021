import time

test_fish_inp = list(map(int, "3,4,3,1,2".split(",")))
f_time_start = time.time()
fish_inp = list(map(int, open("input").read().split(",")))
f_time_end = time.time()


def convert_inp(inp):
    days_left = [0] * 9
    for fish in inp:
        days_left[fish] += 1
    return days_left


def make_more_fish_old(days_left, days):
    for _ in range(0, days):
        today = days_left.pop(0)
        days_left[6] += today
        days_left.append(today)
    return days_left


def make_more_fish(days_left, days):
    """
    Improves the execution time by 2-10%.
    """
    for i in range(0, days):
        days_left[(i + 7) % 9] += days_left[i % 9]
    return days_left


def test1(fishs):
    example1 = map(int, "6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8".split(","))
    expected_result = convert_inp(example1)
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 18)
    print("Result Test 1:", sum(result))
    assert(sum(result) == 26)


def test2(fishs):
    example1 = map(int, "6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8".split(","))
    expected_result = convert_inp(example1)
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 80)
    print("Result Test 2:", sum(result))
    assert(sum(result) == 5934)


def test3(fishs):
    example1 = map(int, "6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8".split(","))
    expected_result = convert_inp(example1)
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 256)
    print("Result Test 3:", sum(result))
    assert(sum(result) == 26984457539)


def a_old(fishs):
    days_left = convert_inp(fishs)
    result = make_more_fish_old(days_left, 80)
    return sum(result)


def a(fishs):
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 80)
    return sum(result)


def b_old(fishs):
    days_left = convert_inp(fishs)
    result = make_more_fish_old(days_left, 256)
    return sum(result)


def b(fishs):
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 256)
    return sum(result)


if __name__ == '__main__':
    test1(test_fish_inp)
    test2(test_fish_inp)
    test3(test_fish_inp)
    a_loops = 20000
    b_loops = 1000
    a_time_start_old = time.time()
    for _ in range(a_loops):
        a(fish_inp)
    a_time_end_old = time.time()
    a_time_start = time.time()
    for _ in range(a_loops):
        a(fish_inp)
    a_time_end = time.time()
    b_time_start_old = time.time()
    for _ in range(b_loops):
        b_old(fish_inp)
    b_time_end_old = time.time()
    b_time_start = time.time()
    for _ in range(b_loops):
        b(fish_inp)
    b_time_end = time.time()
    a_time = (a_time_end - a_time_start) / a_loops
    a_time_old = (a_time_end_old - a_time_start_old) / a_loops
    b_time = (b_time_end - b_time_start) / b_loops
    b_time_old = (b_time_end_old - b_time_start_old) / b_loops
    f_time = f_time_end - f_time_start
    print("Duration a    : {:5.7f}s".format(a_time))
    print("Duration a old: {:5.7f}s".format(a_time_old))
    print("Duration b    : {:5.7f}s".format(b_time))
    print("Duration b old: {:5.7f}s".format(b_time_old))
    print("Duration file : {:5.7f}s".format(f_time))
    a_inc = a_time_old - a_time
    a_boost = a_inc / a_time_old * 100
    b_inc = b_time_old - b_time
    b_boost = b_inc / b_time_old * 100
    print(f"A Boosted: {a_boost:3.2f}%")
    print(f"B Boosted: {b_boost:3.2f}%")
