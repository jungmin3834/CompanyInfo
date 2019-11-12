from ClassDirectory.CompanyInfo import *
from EventControll.send_firebase import *
from PyQt5.QtWidgets import QTableWidgetItem

class Container:
    def __init__(self, window):
        self.window = window
        initialize_firebase()
        self.companyInfo = CompanyInfo(window)
        self.refreshContainer()

    def refreshContainer(self):
        self.companyInfo.clearAllEditText()
        self.companyList = search()
        self.insertCompanyArrayToList(self.window, self.companyList)

    def getCompany(self):
        return self.companyInfo.makeCompany()

    def insertCompanyArrayToList(self,window, companyArray):
        window.tableWidget.setRowCount(0)
        window.tableWidget.setRowCount(len(companyArray))
        for j in range(0, len(companyArray)):
            for i in range(0, 11):
                window.tableWidget.setItem(j, i, QTableWidgetItem(companyArray[j].getItemsByIndex(i)))