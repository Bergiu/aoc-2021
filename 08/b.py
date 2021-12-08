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
    for line in parsed:
        input, output = line
        # PREPARE
        # group the numbers with the same attributes (length)
        # first all number patterns that are unique with their length
        # len(1) = 2
        # one contains the characters that are used to display a one: "ab"
        one: word_t = list(filter(lambda x: len(x) == 2, input))[0]
        # len(4) = 4
        # four contains the characters that are used to display a one: "eafb"
        four: word_t = list(filter(lambda x: len(x) == 4, input))[0]
        # len(7) = 3
        seven: word_t = list(filter(lambda x: len(x) == 3, input))[0]
        # len(8) = 7
        eight: word_t = list(filter(lambda x: len(x) == 7, input))[0]
        # len(2) = 5
        # len(3) = 5
        # len(5) = 5
        # now group the rest of the numbers
        # two_three_five_list contains the characters that are
        # used to display two, three and five: ["cdfbe", "gcdfa", "fbcad"]
        two_three_five_list: io_t = list(filter(lambda x: len(x) == 5, input))
        # len(0) = 6
        # len(6) = 6
        # len(9) = 6
        # two_three_five_list contains the characters that are
        # used to display zero, six and nine: ["cagedb", "cdfgeb", "cefabd"]
        zero_six_nine_list: io_t = list(filter(lambda x: len(x) == 6, input))
        # OPERATIONS ON SETS
        # union adds sets together: (a,b) union (b,c) = (a,b,c)
        # intersection takes all elements that are in both: (b)
        # symmetric_difference takes the opposite of intersection (a,c)
        # a - b is a without b
        # ANALYSIS
        # c is in 1, 4, 7, 8
        # f is in 1, 4, 7, 8
        # b is in 4, 8
        # d is in 4, 8
        # a is in 7, 8
        # e is in 8
        # g is in 8
        # 'e' and 'g' is just an 8 without a 1, a 4 and a 7
        # if you wan't to print an e and g the e_g variable
        # contains the decoded pattern
        e_g: word_t = eight - one - four - seven
        # using the patterns from the known numbers we can get the
        # corresponding character of 'a', because 'a' is just an 8
        # without a 1, a 4 and without 'e' and 'g'.
        a: word_t = eight - one - four - e_g
        # and so on...
        b_d: word_t = eight - one - seven - e_g
        c_f: word_t = eight - e_g - b_d - a
        # now the other numbers are used to make a better analysis
        # only 'a', 'd' and 'g' are used in two, tree and five, so the
        # intersection contains only the pattern for 'a', 'd' and 'g'
        a_d_g: word_t = reduce(set.intersection, two_three_five_list)
        # removing 'a' and 'g' from a_d_g results into a 'd'
        d: word_t = a_d_g - a - e_g
        # and so on...
        b: word_t = b_d - d
        g: word_t = a_d_g - a - d
        e: word_t = e_g - g
        # f, g, b and a are used in zero, six and nine
        f_g_b_a: word_t = reduce(set.intersection, zero_six_nine_list)
        f: word_t = f_g_b_a - a - g - b
        c: word_t = c_f - f
        # DECODE
        # every one-character variable contains the character that
        # is used for them. For example if you encode a 'c' to a 'b',
        # then the variable c now contains 'b'.
        # the matrix connects the encoded char (key) to the decoded
        # char (value).
        decode_matrix: Dict[str, str] = {
            a.pop(): 'a', b.pop(): 'b', c.pop(): 'c', d.pop(): 'd',
            e.pop(): 'e', f.pop(): 'f', g.pop(): 'g'
        }
        # replace all chars with their decode chars
        # "efg abcd" -> [set("abc"), set("defg")]
        decoded_nums: List[word_t] = [{decode_matrix[char] for char in word} for word in output]
        # CONVERT
        # now we have the original character patterns and can convert them to the
        # numbers they represent
        # [0] of matrix is the patter for number 0 (a + b ... + g)
        # [1] of matrix is the patter for number 1 (c + f)
        # this results to: index of set("cf") is 1
        # to convert a character pattern to the number just search for the pattern
        # and take the index
        convert_matrix: List[word_t] = [
            set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"),
            set("abdfg"), set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg"),
        ]
        # replaced decoded chars with the number they represent
        # and wrap those numbers to an int
        # [set("cf"), set("acf")] -> 17
        yield int("".join(str(convert_matrix.index(dec)) for dec in decoded_nums))


if __name__ == '__main__':
    # decode_all returns an array of the decoded numbers
    # we need to sum it up
    print(sum(decode_all()))
