import pandas as pd


class student():
    
  
        
    
    def __init__(self, name, surname, number, score):
        self.name = name
        self.surname = surname
        self.number = number
        self.score = score
        global letterscore
        if 100 >= self.score >= 90:
            self.status = True
            letterscore = "A"
        elif 90 > self.score >= 80:
            self.status = True
            letterscore = "B"
        elif 80 > self.score >= 70:
            self.status = True
            letterscore = "C"
        elif 70 > self.score >= 60:
            self.status = True
            letterscore = "D"
        elif 60 > self.score >= 50:
            self.status = True
            letterscore = "E"
        elif 50 > self.score >= 0:
            self.status = False
            letterscore = "F"

    def learnStatus(self):
        if self.status:
            print(f"Tebrikler {letterscore} notu ile geçtiniz.")

        else:
            print(f"Malesef {letterscore} notu ile kaldınız.")


studentList = []

# girilecek element sayisi
n = int(input("Kaç öğrenci gireceksiniz?: "))

# girilecek elemente göre objecti listeye ekliyoruz
for i in range(0, n):
    print(f"\n Girdi {i+1} \n")
    newName = input("İsminiz: ")
    newSurname = input("Soyisminiz: ")
    newNumber = int(input("Okul numaranız: "))
    newScore = int(input("Sınav notunuz: "))

    # adding the element
    studentList.append(student(newName, newSurname, newNumber, newScore))


""" 
for obj in studentList:
    # print(dir(obj.__dict__))
    # print(obj.__getattribute__("name"))
    # print(type(obj))

    df = pd.DataFrame([obj.__dict__])
    
    #df_final = pd.DataFrame.from_dict([dict(df[[0, 1]].to_numpy())])
    print(df)
"""


""" 
def dataf():
    for obj in studentList:
        data = [obj.__dict__]
        index="Student "+ str(obj)
        columns=obj.__dict__.keys()
df = pd.DataFrame(dataf())
"""


df = pd.DataFrame(obj.__dict__ for obj in studentList)

print(df)