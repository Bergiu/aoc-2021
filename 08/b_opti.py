# improved with: https://www.reddit.com/r/adventofcode/comments/rc0ucn/2021_day_8_part_2_my_logic_on_paper_based_on_sets/

from functools import reduce
from typing import List, Tuple, Set, Dict

lines: List[str] = open("input").read().splitlines()

word_t = Set[str]
io_t = List[word_t]
line_t = Tuple[io_t, ...]

parsed: List[line_t] = [
    tuple(map(
        lambda site: list(map(set, site.split(" "))),
        line.split(" | ")
    ))
    for line in lines
]

# every item in parsed is a tuple for one line of the input
# the tuple contains two lists. the first list contains the
# ten unique signal patterns and the second contains the
# digital output values.
# [(["ab", ...], ["ab", ...]), (..., ...)]


def decode_all():
    for inp, outp in parsed:
        # PREPARE
        nums: List[word_t] = [None] * 10
        nums[1] = next(filter(lambda x: len(x) == 2, inp))
        nums[4] = next(filter(lambda x: len(x) == 4, inp))
        nums[7] = next(filter(lambda x: len(x) == 3, inp))
        nums[8] = next(filter(lambda x: len(x) == 7, inp))
        two_three_five_list: io_t = next(filter(lambda x: len(x) == 5, inp))
        zero_six_nine_list: io_t = next(filter(lambda x: len(x) == 6, inp))
        # ANALYSIS
        nums[9] = next(filter(nums[4].issubset, zero_six_nine_list))
        zero_six_nine_list.remove(nums[9])
        nums[0] = next(filter(nums[7].issubset, zero_six_nine_list))
        zero_six_nine_list.remove(nums[0])
        nums[6] = zero_six_nine_list[0]
        nums[3] = next(filter(nums[7].issubset, two_three_five_list))
        two_three_five_list.remove(nums[3])
        nums[5] = next(filter(nums[6].issuperset, two_three_five_list))
        two_three_five_list.remove(nums[5])
        nums[2] = two_three_five_list[0]
        # CONVERT
        yield int("".join([str(nums.index(num)) for num in outp]))


if __name__ == '__main__':
    # decode_all returns an array of the decoded numbers
    # we need to sum it up
    print(sum(decode_all()))
