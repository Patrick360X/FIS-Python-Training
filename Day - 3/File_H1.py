f = open("Day - 3/data.txt", 'r')

counter = 0

line = f.readline()
while line:
    x = line.split()
    counter += 1
    print('Record No. : ',counter)

    id = line[:6]
    name = line[6:14]
    loc = line[14:26]
    sal = line[26:]
    new_sal = sal

    print("Id:",id,"\nName:",name,"\nLocation:",loc)
    print("Email: " + line[6:9] + line[14:17] + "@fis.com")

    if x[3] == "Boston":
        new_sal = sal * 1.10
        print("Salary: ", sal)
        print("New Salary: ", new_sal)
    elif x[3] == "LA":
        new_sal = sal * 1.15
        print("Salary: ", sal)
        print("New Salary: ", new_sal)
    else:
        new_sal = sal * 1.20
        print("Salary: ", sal)
        print("New Salary: ", new_sal)

    print("***************************")

    line = f.readline()

f.close()