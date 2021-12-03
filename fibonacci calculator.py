N1 = 0
N2 = 1
N3 = 0
count = 0
answer = []

while True:

    N = int(input("Please enter the number of terms to go to in the sequence . . . "))
    if N > 2500:
        print("The entered number is too big")

    else:
        break

answer.append(N1)
answer.append(N2)

while True:
    if count < N:
        N3 = N1 + N2
        answer.append(N3)
        N1 = N2
        N2 = N3
        count += 1

    else:
        break

print(answer)