def prime(number): # prime check of numbers
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return True
        else:
            return False
    else:
        return True


def table_prime(prime_table): #prime check of numbers in array
    for i in range(len(prime_table)):
        for j in range(0, len(prime_table[i]), 1):
            if prime(prime_table[i][j])==0:
                prime_table[i][j]=-1
    return prime_table


def calculate(table): #transfer data to array
    for i in range(len(table) - 2, -1, -1):
        for j in range(len(table[i])):
            if table[i][j]!=-1:
                if table[i + 1][j] ==-1 and table[i + 1][j + 1]==-1:
                    table[i][j]=-1
                else:
                    table[i][j] += max(table[i + 1][j], table[i + 1][j + 1])
    print(table[0][0])


def read(file):
    read_table = []
    file = open(file,"r")
    for i in file:
        temp = i.strip().split()
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        read_table.append(temp)
    return read_table


if __name__ == '__main__':
    file = "test.txt"
    table = read(file)
    table = table_prime(table)
    calculate(table)