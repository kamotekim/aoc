
def part1():
    res = 0
    with open("day1in.txt") as f:
        lines = f.readlines()
        for line in lines:
            num_str = ""
            for n in line:
                if n in '0123456789':
                    num_str += n
                    break
            for n in line[::-1]:
                if n in '0123456789':
                    num_str += n
                    break
            res += int(num_str)
    return res


string_to_num = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four":'4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine":'9'
}

string_nums = [num for num in string_to_num.keys()]

def get_num(line, index):
    """Checks if there is a valid number starting at the index."""
    if line[index] in '0123456789':
        return line[index]
    sub_str = ""
    for i in range(index, len(line)):
        sub_str += line[i]
        flag = False
        for string_num in string_nums:
            if sub_str == string_num: 
                return string_to_num[string_num]
            if sub_str in string_num:
                flag = True
                break
        if not flag: break

def part2():
    res = 0
    with open("day1in2.txt") as f:
        lines = f.readlines()
        for line in lines:
            num_str = ""
            for i in range(len(line)):
                num = get_num(line, i)
                if not num: continue
                num_str += num
                break

            for i in range(len(line) - 1, -1, -1):
                num = get_num(line, i)
                if not num: continue
                num_str += num
                break
            res += int(num_str)
    return res



if __name__ == "__main__":
    print(part1())
    print(part2())
