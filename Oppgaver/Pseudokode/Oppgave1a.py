#FUNCTION beregn(n):
#   SET s TO 0
#   FOR  hvert tall i fra og med 1 til og med n
#      IF i % 2 EQUAL TO 0
#         SET s TO s + i
#      ELSE
#        SET s TO s - i
#      ENDIF
#  ENDFOR
#  RETURN s
#ENDFUNCTION
#DISPLAY beregn(7)

def beregn(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            s += i
        else:
            s -= i

    return s

print(beregn(7))
