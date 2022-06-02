goto main
wb 0

r ww 0
a ww 31
b ww 0
c ww 2

main pull x, a
    sr x
    inc x
    push x, b

    verificar pull x, c
    sub x, b
    jz x, primo

    pull x, a
    mod x, c
    jz x, nao_primo

    pull x, c
    inc x
    push x, c

    goto verificar
    
primo pull x, r
    inc x
    push x, r

nao_primo halt