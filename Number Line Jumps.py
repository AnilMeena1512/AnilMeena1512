first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])
n=10000;
def NumberLine():
    for i in range(n):
        if((x1+v1*i)==(x2+v2*i)):
            return("YES");

    return("NO");
print(NumberLine())
