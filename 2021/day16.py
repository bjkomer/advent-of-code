from functools import reduce


def get_data():

    with open("day16_input.txt", "r") as f:
        hex_str = f.readline()[:-1]
        digits = len(hex_str) * 4 # number of digits the binary value should have
        bin_str = f'{int(hex_str, 16):0>{digits}b}'
        return bin_str


def parse_packet(bin_str, sx=0):
    version = int(bin_str[sx:sx+3], 2)
    type_id = int(bin_str[sx+3:sx+6], 2)
    if type_id == 4:
        cur_ind = sx + 6
        bin_num = ''
        while bin_str[cur_ind] == '1':
            bin_num += bin_str[cur_ind+1:cur_ind+5]
            cur_ind += 5
        else:
            bin_num += bin_str[cur_ind+1:cur_ind+5]
            cur_ind += 5
        return cur_ind, version, int(bin_num, 2)

    length_type = bin_str[sx+6]
    if length_type == '0':
        length_val = int(bin_str[sx+7:sx+22], 2)
        start_index = sx + 22
        end_index = sx + 22 + length_val
        version_sum = 0
        values = []
        while start_index < end_index:
            start_index, vs, value = parse_packet(bin_str, start_index)
            values.append(value)
            version_sum += vs
    elif length_type == '1':
        length_val = int(bin_str[sx+7:sx+18], 2)
        start_index = sx+18
        version_sum = 0
        values = []
        for i in range(length_val):
            start_index, vs, value = parse_packet(bin_str, start_index)
            values.append(value)
            version_sum += vs
    if type_id == 0:
        result = reduce(lambda a, b: a + b, values)
    elif type_id == 1:
        result = reduce(lambda a, b: a * b, values)
    elif type_id == 2:
        result = min(values)
    elif type_id == 3:
        result = max(values)
    elif type_id == 5:
        result = values[0] > values[1]
    elif type_id == 6:
        result = values[0] < values[1]
    elif type_id == 7:
        result = values[0] == values[1]
    return start_index, version_sum + version, result


def solve():
    bin_str = get_data()
    start_index, version_sum, result = parse_packet(bin_str, sx=0)
    return version_sum, result

part1, part2 = solve()
print(part1)
print(part2)

