def segitigaExcel(kata):
    import xlsxwriter
    kata = kata.replace(" ","")
    pjg = len(kata)
    count=0
    hitung=0
    listTemp=[]
    listPerm=[]
    while pjg>0:
        pjg=pjg-count
        count+=1
        if pjg==0:
            for row in range(1,count):#buatbikin baris
                for col in range(row):
                    listTemp.append(kata[hitung])
                    hitung+=1
                listPerm.append(listTemp)
        elif pjg<0:
            print("maaf kata anda tidak memenuhi syarat")

    workbook = xlsxwriter.Workbook('soal2.xlsx')     
    worksheet = workbook.add_worksheet('data')

    row = 0
    col = 0
    for i in listPerm:
        worksheet.write(row,col,listPerm[i])
        row+=1
        col+=1

    workbook.close()