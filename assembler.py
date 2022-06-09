from sys import argv

try:
    argv[1]
    argv[2]
except:
    print('Sintaxe invalida!')
    print('Modo de usar: python3 assembler.py prog.asm output.bin')
    exit(1)

try:
    argv[3]
    print('Sintaxe invalida!')
    print('Modo de usar: python3 assembler.py prog.asm output.bin')
    exit(1)
except:
    pass

asmFile = None

byteCounter = 1
byteList = []
addrNames = {}
cmdBins = {
    'add': 0x05,
    'sub': 0x09,
    'pull': 0x01,
    'push': 0x10,
    'mul': 0x13,
    'div': 0x1D,
    'mod': 0x24,
    'inc': 0x04,
    'dec': 0x0F,
    'sl': 0x0D,
    'sr': 0x0E,
    'fact': 0x30,
    'flg': 0x39,
    'clg': 0x3D,
    'goto': 0x28,
    'jz': 0x2A,
    'jngt': 0x2D,
    'halt': 0xFF
}

try:
    asmFile = open(argv[1])
except:
    print('Arquivo assembly \'' + argv[1] + '\' nao encontrado!')
    exit(1)

asmLines = asmFile.readlines()

def encode_ww(line):
    global byteCounter

    splittedLine = line.split(' ')
    if len(splittedLine) == 2 and splittedLine[0] == 'ww':
        word = int(splittedLine[1])
        byteList.append(word & 0xFF)
        byteList.append((word & 0xFF00) >> 2)
        byteList.append((word & 0xFF0000) >> 4)
        byteList.append((word & 0xFF000000) >> 6)
        byteCounter += 4
    elif len(splittedLine) == 3 and splittedLine[1] == 'ww':
        word = int(splittedLine[2])
        byteList.append(word & 0xFF)
        byteList.append((word & 0xFF00) >> 8)
        byteList.append((word & 0xFF0000) >> 16)
        byteList.append((word & 0xFF000000) >> 24)

        addrName = splittedLine[0]
        addrNames[addrName] = (byteCounter // 4)

        byteCounter += 4
    else:
        raise Exception('sintaxe de "ww" invalida')

def encode_wb(line):
    global byteCounter

    splittedLine = line.split(' ')
    if len(splittedLine) == 2 and splittedLine[0] == 'wb':
        word = int(splittedLine[1])
        byteList.append(word & 0xFF)
        byteCounter += 1
    elif len(splittedLine) == 3 and splittedLine[1] == 'wb':
        word = int(splittedLine[2])
        byteList.append(word & 0xFF)

        addrName = splittedLine[0]
        addrNames[addrName] = (word & 0xFF)

        byteCounter += 1
    else:
        raise Exception('sintaxe de "wb" invalida')

def encode_arg_cmd(line, cmd):
    global byteCounter

    splittedLine = line.split(' ')
    if len(splittedLine) == 3 and splittedLine[0] == cmd and splittedLine[1] == 'x,':
        word = None

        byteList.append(cmdBins[cmd])

        try:
            word = int(splittedLine[2])
            byteList.append(0xFF & word)
        except:
            word = splittedLine[2]
            byteList.append(word)

        byteCounter += 2
    elif len(splittedLine) == 4 and splittedLine[1] == cmd and splittedLine[2] == 'x,':
        word = None

        byteList.append(cmdBins[cmd])
    
        try:
            word = int(splittedLine[3])
            byteList.append(0xFF & word)
        except:
            word = splittedLine[3]
            byteList.append(word)


        addrName = splittedLine[0]
        addrNames[addrName] = byteCounter

        byteCounter += 2
    else:
        raise Exception('sintaxe de "' + cmd + ' x" invalida')

def encode_goto(line):
    global byteCounter

    splittedLine = line.split(' ')
    if len(splittedLine) == 2 and splittedLine[0] == 'goto':
        word = None

        byteList.append(cmdBins['goto'])

        try:
            word = int(splittedLine[1])
            byteList.append(0xFF & word)
        except:
            word = splittedLine[1]
            byteList.append(word)

        byteCounter += 2
    elif len(splittedLine) == 3 and splittedLine[1] == 'goto':
        word = None

        byteList.append(cmdBins['goto'])
    
        try:
            word = int(splittedLine[2])
            byteList.append(0xFF & word)
        except:
            word = splittedLine[2]
            byteList.append(word)


        addrName = splittedLine[0]
        addrNames[addrName] = byteCounter

        byteCounter += 2
    else:
        raise Exception('sintaxe de "goto" invalida')

def encode_noarg_cmd(line, cmd):
    global byteCounter

    splittedLine = line.split(' ')
    if len(splittedLine) == 2 and splittedLine[0] == cmd and splittedLine[1] == 'x':
        byteList.append(cmdBins[cmd])
        byteCounter += 1
    elif len(splittedLine) == 3 and splittedLine[1] == cmd and splittedLine[2] == 'x':
        byteList.append(cmdBins[cmd])
        addrName = splittedLine[0]
        addrNames[addrName] = byteCounter
        byteCounter += 1
    else:
        raise Exception('sintaxe de "inc x" invalida')

def encode_halt(line):
    global byteCounter

    splittedLine = line.split(' ')
    if len(splittedLine) == 1 and splittedLine[0] == 'halt':
        byteList.append(cmdBins['halt'])
        byteCounter += 1
    elif len(splittedLine) == 2 and splittedLine[1] == 'halt':
        byteList.append(cmdBins['halt'])
        addrName = splittedLine[0]
        addrNames[addrName] = byteCounter
        byteCounter += 1
    else:
        raise Exception('sintaxe de "halt" invalida')

lineCounter = 0

try:
    for line in asmLines:
        line = line.replace('\t', '').replace('  ', '').replace('    ', '').replace('\n', '')

        lineCounter += 1

        if len(line) == 0 or line[0] == '#':
            continue


        if 'ww' in line:
            encode_ww(line)
        elif 'wb' in line:
            encode_wb(line)
        elif 'add x' in line:
            encode_arg_cmd(line, 'add')
        elif 'sub x' in line:
            encode_arg_cmd(line, 'sub')
        elif 'pull x' in line:
            encode_arg_cmd(line, 'pull')
        elif 'push x' in line:
            encode_arg_cmd(line, 'push')
        elif 'mul x' in line:
            encode_arg_cmd(line, 'mul')
        elif 'div x' in line:
            encode_arg_cmd(line, 'div')
        elif 'mod x' in line:
            encode_arg_cmd(line, 'mod')
        elif 'inc x' in line:
            encode_noarg_cmd(line, 'inc')
        elif 'dec x' in line:
            encode_noarg_cmd(line, 'dec')
        elif 'sl x' in line:
            encode_noarg_cmd(line, 'sl')
        elif 'sr x' in line:
            encode_noarg_cmd(line, 'sr')
        elif 'fact x' in line:
            encode_noarg_cmd(line, 'fact')
        elif 'flg x' in line:
            encode_noarg_cmd(line, 'flg')
        elif 'clg x' in line:
            encode_noarg_cmd(line, 'clg')
        elif 'goto' in line:
            encode_goto(line)
        elif 'jz x' in line:
            encode_arg_cmd(line, 'jz')
        elif 'jngt x' in line:
            encode_arg_cmd(line, 'jngt')
        elif 'halt' in line:
            encode_halt(line)
        else:
            raise Exception('Comando inexistente')
except Exception as err:
    print('Erro na linha ' + str(lineCounter) + ': ' + str(err))
    exit(1)

for c in range(0, len(byteList)):
    byte = byteList[c]

    if type(byte) == str:
        try:
            addrNames[byte]
        except:
            print('Variavel ' + byte + ' nao foi encontrada')
            exit(1)
        byteList[c] = addrNames[byte]

asmFile.close()

binFile = None

try:
    binFile = open(argv[2], 'wb')
except:
    print('Erro ao escrever o arquivo de saida')
    exit(1)

binFile.write(bytes([0]))
for byte in byteList:
    binFile.write(bytes([byte]))

binFile.close()
