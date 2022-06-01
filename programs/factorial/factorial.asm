goto main
wb 0

result ww 0
op ww 8

main pull x, op
    fact x
    push x, result
    halt