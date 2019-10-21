# Global variables
B = "b"


def make_tape():
    return [0, 0, 0, 0, 1, 1, 1, B, B, B, B, B, B]


def go_middle(tape):
    return tape.index(B)


def l(pos):
    return pos - 1


def r(pos):
    return pos + 1


def a_state(tape, pos):
    print(tape)
    tape[pos] = 0
    pos = l(pos)
    b_state(tape, pos)


def b_state(tape, pos):
    while(True):
        if(tape[pos] == 1):
            tape[pos] = B
            c_state(tape, pos)
            break
        elif(tape[pos] == 0):
            f_state(tape, pos)
        else:
            pos = l(pos)


def c_state(tape, pos):
    while(True):
        if(tape[pos] == 0):
            d_state(tape, pos)
            break
        else:
            pos = r(pos)


def d_state(tape, pos):
    while(True):
        if(tape[pos] == B):
            tape[pos] = 1
            e_state(tape, pos)
            break
        else:
            pos = r(pos)


def e_state(tape, pos):
    while(True):
        if(tape[pos] == 0):
            pos = l(pos)
            b_state(tape, pos)
            break
        else:
            pos = l(pos)


def f_state(tape, pos):
    while(True):
        pos = r(pos)
        if(tape[pos] == B):
            tape[pos] = 1
        elif(tape[pos] == 0):
            g_state(tape, pos)
            break
        else:
            pos = r(pos)


def g_state(tape, pos):
    while(True):
        tape[pos] = B
        if(tape[pos] == B):
            x_state(tape, pos)
            break
        else:
            pos = r(pos)


def x_state(tape, pos):
    print(tape)
    exit()


def main():
    tape = make_tape()
    pos = int(go_middle(tape))
    a_state(tape, pos)


if __name__ == "__main__":
    main()
