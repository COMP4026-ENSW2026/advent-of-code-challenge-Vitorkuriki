with open('input.txt', 'r') as f:
    lines = f.readlines()
    caloria = [entrada.strip() for entrada in lines]


    elf_sums = []
    sum = 0
for entrada in caloria:
    if entrada != '':
        sum += int(entrada)
    elif entrada == '':
        elf_sums.append(sum)
        sum = 0
elf_sums.append(sum)


max(elf_sums)
