import sys


def maain():
    transition = [[[0, 1], [0]], [[4], [2]], [[4], [3]], [[4], [4]]]
    input1 = input("enter the string: ")
    input1 = list(
        input1)  # copy the input in list because python strings are immutable and thus can't be changed directly
    for index in range(len(input1)):  # parse the string of a,b in 0,1 for simplicity
        if input1[index] == 'a':
            input1[index] = '0'
        else:
            input1[index] = '1'
    final = "3"  # set of final states = {3}
    start = 0
    i = 0  # counter to remember the number of symbols read

    trans(transition, input1, final, start, i)
    print("rejected")


def trans(transition, input1, final, state, i):
    for j in range(len(input1)):
        for each in transition[state][int(input1[j])]:  # check for each possibility
            if each < 4:  # move further only if you are at non-hypothetical state
                state = each
                if j == len(input1) - 1 and (str(state) in final):  # last symbol is read and current state lies in the set of final states
                    print("accepted")
                    sys.exit()
                trans(transition, input1[i + 1:], final, state, i)  # input string for next transition is input[i+1:]
        i = i + 1  # increment the counter


maain()
