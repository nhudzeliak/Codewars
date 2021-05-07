def solution(number):
    initial = 2
    sum = 0
    while initial < number:
        if initial % 3 == 0 or initial % 5 == 0:
            sum += initial
        initial += 1
    return sum