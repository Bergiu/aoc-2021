import time

test_fish_inp = list(map(int, "3,4,3,1,2".split(",")))
f_time = time.time()
fish_inp = list(map(int, open("input").read().split(",")))
f_time_end = time.time()


def convert_inp(inp):
    days_left = [0] * 9
    for fish in inp:
        days_left[fish] += 1
    return days_left


def make_more_fish(days_left_inp, days):
    days_left = [day for day in days_left_inp]
    for i in range(0, days):
        today = days_left.pop(0)
        days_left[6] += today
        days_left.append(today)
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


def a(fishs):
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 80)
    print("Result:", sum(result))


def b(fishs):
    days_left = convert_inp(fishs)
    result = make_more_fish(days_left, 256)
    print("Result:", sum(result))


if __name__ == '__main__':
    test1(test_fish_inp)
    test2(test_fish_inp)
    test3(test_fish_inp)
    a_time = time.time()
    a(fish_inp)
    a_time_end = time.time()
    b_time = time.time()
    b(fish_inp)
    b_time_end = time.time()
    print("Duration a: {:5.7f}s".format(a_time_end - a_time))
    print("Duration b: {:5.7f}s".format(b_time_end - b_time))
    print("Duration f: {:5.7f}s".format(f_time_end - f_time))
