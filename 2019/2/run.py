
def run(program):
    i = 0
    while i < len(program):
        opcode = program[i]
        if opcode == 1:
            '''add'''
            operand_1 = program[program[i+1]]
            operand_2 = program[program[i+2]] 
            storage_idx = program[i+3]
            program[storage_idx] = operand_1 + operand_2
            i+=4
        elif opcode == 2:
            '''multiply'''
            operand_1 = program[program[i+1]]
            operand_2 = program[program[i+2]]
            storage_idx = program[i+3]
            program[storage_idx] = operand_1 * operand_2
            i += 4
        elif opcode == 99:
            return
        else:
            return

for i in range(100):
    for j in range(100):
        
        with open('input.txt') as file:
            program = file.readline().strip().split(',')
            program = [int(x) for x in program]

            program[1] = i 
            program[2] = j
    

            run(program)

            if program[0] == 19690720:
                print(100 * i + j)

