import memory
import clock
import ufc2x as cpu

# memory.write_byte(1, 1)
# memory.write_byte(2, 200)
# memory.write_byte(3, 4)
# memory.write_byte(4, 5)
# memory.write_byte(5, 201)
# memory.write_byte(6, 9)
# memory.write_byte(7, 202)
# memory.write_byte(8, 14)
# memory.write_byte(9, 13)
# memory.write_byte(10, 15)
# memory.write_byte(11, 16)
# memory.write_byte(12, 203)
# memory.write_byte(13, 19)
# memory.write_byte(14, 204)
# memory.write_byte(15, 29)
# memory.write_byte(16, 205)
# memory.write_byte(17, 36)
# memory.write_byte(18, 206)
# memory.write_byte(19, 40)
# memory.write_byte(20, 60)
# memory.write_byte(60, 1)
# memory.write_byte(61, 200)
# memory.write_byte(62, 1)
# memory.write_byte(63, 207)
# memory.write_byte(64, 42)
# memory.write_byte(65, 70)
# memory.write_byte(70, 1)
# memory.write_byte(71, 208)
# memory.write_byte(72, 9)
# memory.write_byte(73, 200)
# memory.write_byte(74, 45)
# memory.write_byte(75, 90)
# memory.write_byte(90, 1)
# memory.write_byte(91, 200)
# memory.write_byte(92, 255)


# memory.write_word(200, 50)
# memory.write_word(201, 20)
# memory.write_word(202, 30)
# memory.write_word(204, 8)
# memory.write_word(205, 12)
# memory.write_word(206, 3)
# memory.write_word(207, 0)
# memory.write_word(208, 1)

# =================================

# memory.write_byte(1, 1)
# memory.write_byte(2, 200)
# memory.write_byte(3, 48)
# memory.write_byte(4, 16)
# memory.write_byte(5, 201)

# memory.write_byte(6, 255)

# memory.write_word(200, 8)

# ================================

# memory.write_byte(1, 1)
# memory.write_byte(2, 200)
# memory.write_byte(3, 57)
# memory.write_byte(4, 255)

# memory.write_word(200, 256)

clock.start([cpu])

print(cpu.X)