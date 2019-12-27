import xlwt
import xlrd
import csv
import datetime
from xlrd import xldate_as_tuple


class Excel:

    def open_csv(self, file_path):
        data_list = []
        data = open(file_path, 'r', encoding="utf-8")
        dataline = csv.reader(data)
        for data in dataline:
            # csv中每一行被转换为了list形式并被赋给i
            data_list.append(data)
        return data_list

    def save_xls(self,data_list,file_path):

        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
        # 将数据写入第 i 行，第 j 列
        i = 0
        for data in data_list:
            for j in range(len(data)):
                sheet1.write(i, j, data[j])
            i = i + 1

        f.save(file_path)


    def open_excel(self,file_path):

        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_index(0)
        rows = sheet.nrows
        cols = sheet.ncols
        # print(user_detail)
        data_list=[]
        for i in range(1, rows):
            a = []
            for j in range(cols):
                c_type = sheet.cell(i, j).ctype
                c_cell = sheet.cell_value(i, j)
                if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
                    c_cell = int(c_cell)
                elif c_type == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(c_cell, 0))
                    c_cell = date.strftime('%Y-%m-%d')
                elif c_type == 4:
                    c_cell = True if c_cell == 1 else False
                a.append(c_cell)
            data_list.append(a)
        return data_list




    def run(self):
        file_path=r"C:/Users/Administrator/Desktop/蜘蛛智联大数据产品1.5/aibuddy20191225.csv"
        aibuddy_list=self.open_csv(file_path)
        # print(len(aibuddy_list))
        file_path_1="C:/Users/Administrator/Desktop/蜘蛛智联大数据产品1.5/aibuddy20191225_1.xls"
        self.save_xls(aibuddy_list,file_path_1)

if __name__ == '__main__':
    excel=Excel()
    excel.run()
