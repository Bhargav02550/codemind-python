string = input()
divisions = int(input())
if len(string) % divisions == 0:
    part_length = len(string) // divisions
    for i in range(0, len(string), part_length):
        part = string[i:i+part_length]
        print(part, end=" ")
    print()
else:
    print("Invalid String")
