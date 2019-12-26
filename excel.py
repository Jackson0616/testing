import xlwt
import xlrd
import csv

class Excel:

    def open_csv(self, file_path):
        data_list = []
        data = open(file_path, 'r', encoding="utf-8")
        dataline = csv.reader(data)
        for data in dataline:
            # csv中每一行被转换为了list形式并被赋给i
            data_list.append(data)
        return data_list


    def save_excel(self,data_list):


    def run(self):
        file_path=r"C:/Users/Administrator/Desktop/蜘蛛智联大数据产品1.5/aibuddy20191225.csv"
        aibuddy_list=self.open_csv(file_path)
        print(len(aibuddy_list))

if __name__ == '__main__':
    excel=Excel()
    excel.run()
