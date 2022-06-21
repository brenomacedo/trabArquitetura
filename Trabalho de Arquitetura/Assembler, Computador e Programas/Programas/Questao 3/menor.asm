goto main
wb 0

x1 ww -1
x2 ww 12
x3 ww 35

main pull x, x1
  sub x, x2
  jngt x, x2_maior
  
  pull x, x2
  sub x, x3
  jngt x, x3_maior

  pull x, x3
  push x, x1
  halt

x2_maior pull x, x1
  sub x, x3
  jngt x, x2_maior_c1

  pull x, x3
  push x, x1
  halt

x2_maior_c1 halt

x3_maior pull x, x2
  push x, x1
  halt