goto main
wb 0

n ww 45

a ww 1
b ww 1
c ww 2
r ww 1

main pull x, n
  sub x, a
  jngt x, achou_raiz

  pull x, r
  inc x
  push x, r

  pow2 x
  push x, a

  goto main

achou_raiz pull x, r
  dec x
  push x, n
  halt