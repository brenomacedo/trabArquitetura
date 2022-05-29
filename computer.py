import memory
import clock
import ufc2x as cpu

memory.write_byte(1, 1)
memory.write_byte(2, 200)
memory.write_byte(3, 4)
memory.write_byte(4, 5)
memory.write_byte(5, 201)
memory.write_byte(6, 9)
memory.write_byte(7, 202)
memory.write_byte(8, 14)
memory.write_byte(9, 13)
memory.write_byte(10, 15)
memory.write_byte(11, 16)
memory.write_byte(12, 203)
memory.write_byte(13, 19)
memory.write_byte(14, 204)
memory.write_byte(15, 29)
memory.write_byte(16, 205)
memory.write_byte(17, 255)


memory.write_word(200, 50)
memory.write_word(201, 20)
memory.write_word(202, 30)
memory.write_word(204, 8)
memory.write_word(205, 313)

clock.start([cpu])

print(cpu.X)