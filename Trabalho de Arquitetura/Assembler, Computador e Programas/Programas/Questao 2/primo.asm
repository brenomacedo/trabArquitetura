goto main
wb 0

n ww 100

initial_i ww 2
i ww 2
pow2i ww 0
counter ww 1

main pull x, n
  dec x
  jz x, primo_dois

  push x, n

proximo_teste_primo pull x, counter
  add x, initial_i
  push x, counter

  goto verificaprimo

verificaprimo pull x, initial_i
  push x, i
  pow2 x
  push x, pow2i

lacoprimo pull x, counter
  sub x, pow2i
  jngt x, eh_primo

  pull x, counter
  mod x, i

  jz x, proximo_teste_primo

  pull x, i
  inc x
  push x, i
  pow2 x
  push x, pow2i
  goto lacoprimo

eh_primo pull x, n
  dec x
  
  jz x, achou_primo
  push x, n
  goto proximo_teste_primo

primo_dois pull x, initial_i
  push x, n
  halt

achou_primo pull x, counter
  push x, n
  halt