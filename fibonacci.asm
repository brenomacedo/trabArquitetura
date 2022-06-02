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

search dec x
    pull x, r
    push x, s

    add x, f
    push x, r

    pull x, s
    push x, f

    jz x, found
    goto search

found halt
