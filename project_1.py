import pandas as pd
import openpyxl



class student():
    
    def __init__(self, name, surname, number, score):
        self.name = name
        self.surname = surname
        self.number = number
        self.score = score
        self.findStatus()
        
    def findStatus(self):
        
        if 100 >= self.score >= 0:
            if 100 >= self.score >= 90:
                self.status = True
                self.letterscore = "A"
            elif 90 > self.score >= 80:
                self.status = True
                self.letterscore = "B"
            elif 80 > self.score >= 70:
                self.status = True
                self.letterscore = "C"
            elif 70 > self.score >= 60:
                self.status = True
                self.letterscore = "D"
            elif 60 > self.score >= 50:
                self.status = True
                self.letterscore = "E"
            elif 50 > self.score >= 0:
                self.status = False
                self.letterscore = "F"
        else:
            print("Puanınızı doğru girdiğinizden emin olun!")
        
        if self.status: self.userstatus="Gecti" 
        else: self.userstatus="Kaldı" 
        
    

    def learnStatus(self):
        if self.status:
            print(f"Tebrikler {letterscore} notu ile geçtiniz.")

        else:
            print(f"Malesef {letterscore} notu ile kaldınız.")


studentList = []

# girilecek element sayisi
try:
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

    
    df = pd.DataFrame(obj.__dict__ for obj in studentList)

    print(df)

    #excel cıktısı
    df.to_excel("output.xlsx")

except ValueError:
        print("Değerleri doğru girdiğinizden emin olun!") 


#Kalan öğrencilerle geçen öğrencileri ayrı listelere ayırdım.

failStudents = []
successStudents= []
for stu in studentList:
    if stu.status:
        successStudents.append(stu)
    else:
        failStudents.append(stu)

suc  = pd.DataFrame(obj.__dict__ for obj in successStudents)
fai  = pd.DataFrame(obj.__dict__ for obj in failStudents)

print(suc,fai)










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

