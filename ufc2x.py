from array import array
import memory

# X <- X + 1 [OK]
# X <- X - 1 [OK]
# X <- memory[address] [OK]
# X <- X + memory[address] [OK]
# X <- X - memory[address] [OK]
# X <- x << 1 [OK]
# X <- X >> 1 [OK]
# momery[address] <- X [OK]
# X <- X * memory[address] [OK]
# X <- X // memory[address] [OK]
# X <- X % memory[address] [OK]
# GOTO address [OK]
# if X == 0 GOTO address [OK]
# if X < 0 GOTO address [OK]

# ===== fazer o assembly

MIR = 0
MPC = 0

MAR = 0
MDR = 0
PC  = 0
MBR = 0
X   = 0
Y   = 0
H   = 0

NGT = 0
Z   = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0

firmware = array('L', [0]) * 512

# PC <- PC + 1; MBR <- read_byte(PC); GOTO MBR
firmware[0] = 0b00000000010000110101001000001001

# X <- memory[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 2
firmware[1] = 0b00000001000000110101001000001001
## MAR <- MBR; read_word; GOTO 3
firmware[2] = 0b00000001100000010100100000010010
## X <- MDR; GOTO 0
firmware[3] = 0b00000000000000010100000100000000

# X <- X + 1
firmware[4] = 0b00000000000000110101000100000011
## X <- X + 1; GOTO 0

# X <- X + momery[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 6
firmware[5] = 0b00000011000000110101001000001001
## MAR <- MBR; read_word; GOTO 7
firmware[6] = 0b00000011100000010100100000010010
## H <- MDR; GOTO 8;
firmware[7] = 0b00000100000000010100000001000000
## X <- X + H; GOTO 0
firmware[8] = 0b00000000000000111100000100000011

# X <- X - memory[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 10
firmware[9] = 0b00000101000000110101001000001001
## MAR <- MBR; read_word; GOTO 11
firmware[10] = 0b00000101100000010100100000010010
## H <- MDR; GOTO 12;
firmware[11] = 0b00000110000000010100000001000000
## X <- X - H; GOTO 0
firmware[12] = 0b00000000000000111111000100000011

# X <- X << 1
## X <- X << 1; GOTO 0
firmware[13] = 0b00000000000001010100000100000011

# X <- X >> 1
## X <- X >> 1; GOTO 0
firmware[14] = 0b00000000000010010100000100000011

# X <- X - 1
## X <- X - 1; GOTO 0
firmware[15] = 0b00000000000000110110000100000011

# memory[address] <- X
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 17
firmware[16] = 0b00001000100000110101001000001001
## MAR <- MBR; GOTO 18
firmware[17] = 0b00001001000000010100100000000010
## MDR <- X; write_word; GOTO 0
firmware[18] = 0b00000000000000010100010000100011

# X <- X * memory[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 20
firmware[19] = 0b00001010000000110101001000001001
## MAR <- MBR; read_word; GOTO 21
firmware[20] = 0b00001010100000010100100000010010
## H <- MDR; GOTO 22
firmware[21] = 0b00001011000000010100000001000000
## if X - H < 0; GOTO 23 + 256; else GOTO 23
firmware[22] = 0b00001011101000111111000000000011
### [23] H é menor ou igual
## Y <- H; GOTO 24
firmware[23] = 0b00001100000000011000000010000000
### [279] H é maior
## Y <- X; GOTO 25
firmware[279] = 0b00001100100000010100000010000011
## H <- X; GOTO 25
firmware[24] = 0b00001100100000010100000001000011
### [25] inicia a multiplicação
## X <- 0; GOTO 26
firmware[25] = 0b00001101000000010000000100000000
## if Y == 0 GOTO 256 + 27; else GOTO 27
firmware[26] = 0b00001101100100010100000000000100
### [283] y é zero, portanto, vá para a próxima instrução
firmware[283] = 0b00000000010000110101001000001001
## Y <- Y - 1; GOTO 28
firmware[27] = 0b00001110000000110110000010000100
## X <- X + H; GOTO 26
firmware[28] = 0b00001101000000111100000100000011
# H fica o maior
# Y fica o menor

# X <- X // memory[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 30
firmware[29] = 0b00001111000000110101001000001001
## MAR <- MBR; read_word; GOTO 31
firmware[30] = 0b00001111100000010100100000010010
## H <- MDR; GOTO 32
firmware[31] = 0b00010000000000010100000001000000
## Y <- X; GOTO 33
firmware[32] = 0b00010000100000010100000010000011
## X <- 0; GOTO 34
firmware[33] = 0b00010001000000010000000100000000
## Y <- Y - H; if Y - H < 0 GOTO 35 + 256; else GOTO 35
firmware[34] = 0b00010001101000111111000010000100
### [35] Y é maior ou igual a 0
## X <- X + 1; GOTO 34
firmware[35] = 0b00010001000000110101000100000011
### [291] Y é menor que 0
firmware[291] = 0b00000000010000110101001000001001

# X <- X % memory[address]
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 37
firmware[36] = 0b00010010100000110101001000001001
## MAR <- MBR; read_word; GOTO 38
firmware[37] = 0b00010011000000010100100000010010
## H <- MDR; GOTO 39
firmware[38] = 0b00010011100000010100000001000000
## X <- X - H; if X - H < 0 GOTO 39 + 256; else 39
firmware[39] = 0b00010011101000111111000100000011
### [295] X é menor que 0
## X <- X + H; GOTO 0
firmware[295] = 0b00000000000000111100000100000011

# GOTO address
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 41
firmware[40] = 0b00010100100000110101001000001001
## PC <- MBR; MBR <- read_byte(PC); GOTO MBR
firmware[41] = 0b00000000010000010100001000001010

# if X == 0 GOTO address
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 43
firmware[42] = 0b00010101100000110101001000001001
## if X == 0; GOTO 44 + 256; else GOTO 44
firmware[43] = 0b00010110000100010100000000000011
### [300] X é igual a 0
## PC <- MBR; MBR <- read_byte(PC); GOTO MBR
firmware[300] = 0b00000000010000010100001000001010
## [44] X é diferente de 0
firmware[44] = 0b00000000010000110101001000001001

# if X < 0 GOTO address
## PC <- PC + 1; MBR <- read_byte(PC); GOTO 46
firmware[45] = 0b00010111000000110101001000001001
## if X < 0; GOTO 47 + 256; else GOTO 47
firmware[46] = 0b00010111101000010100000000000011
### [303] X é igual a 0
## PC <- MBR; MBR <- read_byte(PC); GOTO MBR
firmware[303] = 0b00000000010000010100001000001010
## [47] X é diferente de 0
firmware[47] = 0b00000000010000110101001000001001

#halt
firmware[255] = 0b00000000000000000000000000000000

def read_regs(reg_num):
   global BUS_A, BUS_B, H, MDR, PC, MBR, X, Y
   
   BUS_A = H
   
   if reg_num == 0:
      BUS_B = MDR
   elif reg_num == 1:
      BUS_B = PC
   elif reg_num == 2:
      BUS_B = MBR
   elif reg_num == 3:
      BUS_B = X
   elif reg_num == 4:
      BUS_B = Y
   else:
      BUS_B = 0
   
def write_regs(reg_bits):
   global MAR, MDR, PC, X, Y, H, BUS_C
   
   if reg_bits & 0b100000:
      MAR = BUS_C
   if reg_bits & 0b010000:
      MDR = BUS_C
   if reg_bits & 0b001000:
      PC = BUS_C
   if reg_bits & 0b000100:
      X = BUS_C
   if reg_bits & 0b000010:
      Y = BUS_C
   if reg_bits & 0b000001:
      H = BUS_C
      
def alu(control_bits):
   global NGT, Z, BUS_A, BUS_B, BUS_C

   a = BUS_A
   b = BUS_B
   o = 0
   
   shift_bits = (0b11000000 & control_bits) >> 6
   control_bits = 0b00111111 & control_bits

   if control_bits == 0b011000:
      o = a
   elif control_bits == 0b010100:
      o = b
   elif control_bits == 0b011010:
      o = ~a
   elif control_bits == 0b101100:
      o = ~b
   elif control_bits == 0b111100:
      o = a+b
   elif control_bits == 0b111101:
      o = a+b+1
   elif control_bits == 0b111001:
      o = a+1
   elif control_bits == 0b110101:
      o = b+1
   elif control_bits == 0b111111:
      o = b-a
   elif control_bits == 0b110110:
      o = b-1
   elif control_bits == 0b111011:
      o = -a
   elif control_bits == 0b001100:
      o = a & b
   elif control_bits == 0b011100:
      o = a | b
   elif control_bits == 0b010000:
      o = 0
   elif control_bits == 0b110001:
      o = 1
   elif control_bits == 0b110010:
      o = -1   
   
   if o == 0:
      Z = 1
   else:
      Z = 0

   if o < 0:
      NGT = 1
   else:
      NGT = 0
      
   if shift_bits == 0b01:
      o = o << 1
   elif shift_bits == 0b10:
      o = o >> 1
   elif shift_bits == 0b11:
      o = o << 8
      
   BUS_C = o
   
def next_instruction(next, jam):
   global MPC, MBR, Z, NGT
   
   if jam == 0:
      MPC = next
      return
      
   if jam & 0b001:
      next = next | (Z << 8)   
   
   if jam & 0b010:
      next = next | (NGT << 8)
      
   if jam & 0b100:
      next = next | MBR

   MPC = next
   
def memory_io(mem_bits):
   global PC, MBR, MDR, MAR
   
   if mem_bits & 0b001:
      MBR = memory.read_byte(PC)
   
   if mem_bits & 0b010:
      MDR = memory.read_word(MAR)
      
   if mem_bits & 0b100:
      memory.write_word(MAR, MDR)
      
def step():
   global MIR, MPC
   
   MIR = firmware[MPC]
   
   if MIR == 0:
      return False
      
   read_regs(MIR & 0b00000000000000000000000000000111)   
   alu((MIR & 0b00000000000011111111000000000000) >> 12)
   write_regs((MIR & 0b00000000000000000000111111000000) >> 6)
   memory_io((MIR & 0b00000000000000000000000000111000) >> 3)
   next_instruction((MIR & 0b11111111100000000000000000000000) >> 23,
                    (MIR & 0b00000000011100000000000000000000) >> 20)
   
   return True
   
   
   
   
   
   
   
   
   
   
   