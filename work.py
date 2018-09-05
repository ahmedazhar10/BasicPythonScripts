#import xlrd module
import xlrd

#Open file
workbook = xlrd.open_workbook("C:/Users/hp/Documents/Gym Log.xlsx")



#Open sheet:
worksheet = workbook.sheet_by_index(0)

worksheet.write(4,0,"yoo")
rows = worksheet.nrows
cols = worksheet.ncols



print("Number of rows: {0}".format(rows))
print("Number of columns: {0}".format(cols))

table = list()
record = list()

for i in range(rows):
    for j in range (cols):
        record.append(worksheet.cell(i,j).value)

    table.append(record)
    record = []

print(table)
