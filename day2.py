# Day 2

# 4 Characters in an in a Segment
# Op 1 is Addition
# Op 2 is multiplication
# Op 99 is stop

def load_data(filepath):
    with open(filepath) as f:
        data = f.read()

    intcode = [int(p1) for p1 in data.split(",")]
    return intcode

def chunks(data, n):
    for i in range(0, len(data), n):
        yield data[i:i + n]

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def calculate(chunk):
    pass

def do_instruction(intcode, chunk, operator_map):
    if chunk[0] == 99:
        return 99

    op, p1, p2, addr = chunk[0], intcode[chunk[1]], intcode[chunk[2]], chunk[3]
    result = operator_map[op](p1,p2)
    intcode[addr] = result

operator_map = {
    1: add,
    2: multiply
}

if __name__ == "__main__":


    with open("input.txt") as f:
        intcode = f.read()
    intcode = [int(p1) for p1 in intcode.split(",")]
   
    data_backup = intcode

    for x in range(99):
        for y in range(99):
            intcode = load_data("input.txt")
            intcode[1] = x
            intcode[2] = y

            for chunk in chunks(intcode, 4):
                try:
                    result = do_instruction(intcode, chunk, operator_map)
                except KeyError as e:
                    pass

                if intcode[0] == 19690720:
                    print(100 * x + y)
                if result == 99:
                    break
              



