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
        
        # Giris kisminda kontrol yapildigi icin kontroller kaldirildi. (A)
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
        else:
            self.status = False
            self.letterscore = "F"
        
        if self.status==True: self.userstatus= "Gecti"
        else: self.userstatus="Kaldi" # IF kosulu revize edildi. (A)

    # Kullanilmadiği icin kapatildi. Silinebilir. Tartismaya acik. (A)
    """
    def learnStatus(self):
        if self.status:
            print(f"Tebrikler {letterscore} notu ile gectiniz.")

        else:
            print(f"Maalesef {letterscore} notu ile kaldiniz.")
    """

studentList = []

# girilecek element sayisi
try:
    n = int(input("Kac ogrenci gireceksiniz?: "))

    # girilecek elemente göre objecti listeye ekliyoruz
    for i in range(0, n):
        
        print(f"\n Girdi {i+1} \n")
        newName = input("İsminiz: ")
        newSurname = input("Soyisminiz: ")
        newNumber = input("Okul numaraniz: ") 
        # Bazi okul numaralarinda string karakterler olabiliyor. O sebeple int ibaresini kaldirdim. (A)
        # Sinav notu icin try-except yapildi. Hatasiz girilmesi adina while dongusu yapildi. (A)
        while True:    
            try:
                newScore = int(input("Sinav notunuz: "))
                if 0 <= newScore <= 100: break
                else: print("Sinav notunuz 0 ile 100 arasinda olmalidir. Lütfen tekrar giriniz.")
            except ValueError():
                print("Lütfen sinav notunuzu sayisal olarak giriniz.")

        # adding the element
        studentList.append(student(newName, newSurname, newNumber, newScore))
    
    df = pd.DataFrame(obj.__dict__ for obj in studentList)

    print(df)

    #excel cıktısı
    df.to_excel("output.xlsx")


 
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

    # Daha toplu gozukmesi adina kucuk rotuslar :) (A)
    print("--------------------")
    print("Dersi gecen ogrencilerin listesi:")
    print(suc)

    print("--------------------")
    print("Dersten kalan ogrencilerin listesi:")
    print(fai)

except ValueError:
        print("Ogrenci sayiniz hatali, programdan cikiliyor...") 








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

