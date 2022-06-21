goto main
wb 0

n ww 2000
a ww 100
b ww 400

main pull x, n
  sr x
  sr x
  sl x
  sl x
  sub x, n
  jngt x, naobiss
  
  pull x, n
  mod x, a

  jz x, divisivelcem

  zero x
  inc x
  push x, n
  halt

divisivelcem pull x, n
  mod x, b
  jz x, biss
  zero x
  push x, n
  halt

biss zero x
  inc x
  push x, n
  halt

naobiss zero x
  push x, n
  halt
