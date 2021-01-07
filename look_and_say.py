#6.8

def look_and_say(n):
    l = ["1"]
    if n == 0:
        return "1"
    for i in range(1, n + 1):
        prev_str = l[i-1]
        result_str = ""
        cur_val = prev_str[0]
        counter = 0
        for char in prev_str:
            if cur_val == char:
                counter += 1
            else:
                result_str += str(counter) + str(cur_val)
                cur_val = char
                counter = 1
        result_str += str(counter) + str(cur_val)
        l.append(result_str)
    return l

print(look_and_say(7))

