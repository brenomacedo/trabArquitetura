goto main
wb 0

r ww 0
f ww 1
s ww 1
c ww 15

main pull x, f
    push x, r

    pull x, c
    dec x
    jz x, found
    dec x
    jz x, found
    
    push x, c

search dec x
    push x, c

    pull x, r
    push x, s

    add x, f
    push x, r

    pull x, s
    push x, f

    pull x, c

    jz x, found
    goto search

found halt
