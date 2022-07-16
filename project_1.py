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
        
        if self.status==True: self.userstatus= "Geçti"
        else: self.userstatus="Kaldı" # IF kosulu revize edildi. (A)

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
            except: # Except genelleştirildi. (A)
                print("Lütfen sinav notunuzu sayisal olarak giriniz.")

        # adding the element
        studentList.append(student(newName, newSurname, newNumber, newScore))
    
    df = pd.DataFrame(obj.__dict__ for obj in studentList)

    print(df)


    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

    #excel cıktısı
    df.to_excel(writer, sheet_name='Sheet1')


    # Get the xlsxwriter objects from the dataframe writer object.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']


    #Format oluşturdum.
    format1 = workbook.add_format()

    format1.set_pattern(1)  
    format1.set_bg_color('red')
    format2 = workbook.add_format()

    format2.set_pattern(1)  
    format2.set_bg_color('#4bffff')




    #Dataframe dimensionı çektik
    (max_row, max_col) = df.shape

    worksheet.conditional_format(1, max_col, max_row, max_col,
                            {'type':     'cell',
                            'criteria': '==',
                            'value':     '"Kaldı"',
                            'format':    format1})

    worksheet.conditional_format(1, max_col, max_row, max_col,
                            {'type':     'cell',
                            'criteria': '==',
                            'value':     '"Geçti"',
                            'format':    format2})

    
 


    



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

    # Gecen ve kalan ogrencileri excelde ayrı  sheetlere yazdırdım.
    suc.to_excel(writer, sheet_name='Gecenler')
    fai.to_excel(writer, sheet_name='Kalanlar')



    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
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

