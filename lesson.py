import csv


class Competitor:
    def __init__(self, name, lastname, number):
        self.name = name
        self.lastname = lastname
        self.number = number

    def __add__(self, mark):
        self.arr_marks.append(mark)

    @property
    def full_name(self):
        return f'{self.lastname} {self.name}'

    def __str__(self):
        return f'{self.full_name} '



#reading competitors
competitors = []
with open("data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        s1 = Competitor(line[0], line[1], int(line[2]))
        competitors.append(s1)


class Result:
     def __init__(self, id, result):
         self.id = int(id)
         self.result = int(result)


     def __str__(self):
         return f'{self.id} {self.result} '
#printing results
results = []
with open("text.csv", 'r') as file:
     csv_reader = csv.reader(file)
     for line in csv_reader:
            s1 = Result(int(line[0]), int(line[1]))
            results.append(s1)

all_results = []
for x in competitors:
    all_results.append(x)
    for y in results:
        if x.number == y.id:
            all_results.append(y.result)

my_iter = iter(all_results)
for my_iter in all_results:
    print(my_iter)

def combine(sportsmans, results):
    for sportsman in competitors:
        res = res0 = str(sportsman)
        for result in results:
            if sportsman.number == result.id:
                res += " " + str(result.result)
        if res == res0:
            res += " 0"
        yield res

for res in combine(competitors, results):
    print(res)

#task4
