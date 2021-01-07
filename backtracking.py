# 6.7
num_map = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
}
def recur(num_l, prev_sentence):
    if len(num_l) == 0:
        print(prev_sentence)
    else:
        next_num = num_l[0]
        for char in num_map[next_num]:
            recur(num_l[1:], prev_sentence + char)

recur([2, 2, 7, 6, 6, 9, 6], "")