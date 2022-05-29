from array import array

memory = array("L", [0]) * (1024*1024//4) #1 MByte
                                          #262.144 words
                                          #1 word = 32 bits
                                          #ou 4 bytes

def read_word(end):
	end = end & 0b111111111111111111
	return memory[end]
	
def write_word(end, val):
	end = end & 0b111111111111111111
	val = val & 0xFFFFFFFF
	memory[end] = val
	
def read_byte(end):
	end = end & 0b11111111111111111111
	end_word = end >> 2
	val_word = memory[end_word]
	
	end_byte = end & 0b11
	val_byte = val_word >> (end_byte << 3)
	val_byte = val_byte & 0xFF
	return val_byte
	
def write_byte(end, val):
	val = val & 0xFF

	end = end & 0b11111111111111111111
	end_word = end >> 2
	val_word = memory[end_word]
	
	end_byte = end & 0b11
	
	mask = ~(0xFF << (end_byte << 3))
	val_word = val_word & mask
	
	val = val << (end_byte << 3)
	
	val_word = val_word | val
	
	memory[end_word] = val_word
	