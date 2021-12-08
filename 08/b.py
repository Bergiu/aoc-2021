from functools import reduce

lines = open("input").read().rstrip("\n").split("\n")
parsed = [
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


CONVERT_MATRIX = [
    set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"),
    set("abdfg"), set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg"),
]


def decode_all():
    global CONVERT_MATRIX
    for line in parsed:
        input, output = line
        # len(1) = 2
        one = list(filter(lambda x: len(x) == 2, input))[0]
        # len(4) = 4
        four = list(filter(lambda x: len(x) == 4, input))[0]
        # len(7) = 3
        seven = list(filter(lambda x: len(x) == 3, input))[0]
        # len(8) = 7
        eight = list(filter(lambda x: len(x) == 7, input))[0]
        # len(2) = 5
        # len(3) = 5
        # len(5) = 5
        two_three_five_list = list(filter(lambda x: len(x) == 5, input))
        # len(0) = 6
        # len(6) = 6
        # len(9) = 6
        zero_six_nine_list = list(filter(lambda x: len(x) == 6, input))

        # union fügt sets zusammen (a,b,c)
        # intersection nimmt die schnittmenge (b)
        # symmetric_difference nimmt alles außer der schnittmenge (a,c)
        # a - b is a without b
        # c in 1, 4, 7, 8
        # f in 1, 4, 7, 8
        # b in 4, 8
        # d in 4, 8
        # a in 7, 8
        # e in 8
        # g in 8
        e_g = eight - one - four - seven
        a = eight - one - four - e_g
        b_d = eight - one - seven - e_g
        c_f = eight - e_g - b_d - a
        # rest
        a_d_g = reduce(set.intersection, two_three_five_list)
        d = a_d_g - a - e_g
        b = b_d - d
        g = a_d_g - a - d
        e = e_g - g
        f_g_b_a = reduce(set.intersection, zero_six_nine_list)
        f = f_g_b_a - a - g - b
        c = c_f - f
        decode_matrix = {
            a.pop(): 'a', b.pop(): 'b', c.pop(): 'c', d.pop(): 'd',
            e.pop(): 'e', f.pop(): 'f', g.pop(): 'g'
        }
        # replace all chars with their decode chars
        decoded_nums = [{decode_matrix[char] for char in enc} for enc in output]
        # replaced decoded chars with the number they represent
        # and wrap those numbers to an int
        yield int("".join(str(CONVERT_MATRIX.index(dec)) for dec in decoded_nums))


if __name__ == '__main__':
    print(sum(decode_all()))
