# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MSI\Desktop\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Info_Window(object):

    def __init__(self, window ,company):
        self.setupUi(window)
        _translate = QtCore.QCoreApplication.translate
        self.company.setTitle(_translate("MainWindow", company.company))
        self.job.setText(_translate("MainWindow", company.job))
        self.establish.setText(_translate("MainWindow", company.establish))
        self.companySales_2.setText(_translate("MainWindow", company.companySales))
        self.people.setText(_translate("MainWindow", company.people))
        self.location.setText(_translate("MainWindow", company.location))
        self.qualification.setText(_translate("MainWindow", company.qualification))
        self.process.setText(_translate("MainWindow", company.process))
        self.preferential.setText(_translate("MainWindow", company.preferential))
        self.welfare.setText(_translate("MainWindow", company.welfare))
        self.sales.setText(_translate("MainWindow", company.sales))
        self.typed.setText(_translate("MainWindow", company.typed))

        self.grade.setText(company.PassQualification.grade)
        self.volunteer.setText(company.PassQualification.volunteer)
        self.intern.setText(company.PassQualification.intern)
        self.award.setText(company.PassQualification.award)
        self.experience.setText(company.PassQualification.experience)
        self.certificate.setText(company.PassQualification.certificate)
        self.other.setText(company.PassQualification.other)
        self.opic.setText(company.PassQualification.opic)
        self.toeicSpeacking.setText(company.PassQualification.toeicSpeacking)
        self.toeic.setText(company.PassQualification.toeic)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.company = QtWidgets.QGroupBox(self.centralwidget)
        self.company.setGeometry(QtCore.QRect(30, 30, 941, 441))
        self.company.setObjectName("company")

        #직종
        self.label_7 = QtWidgets.QLabel(self.company)
        self.label_7.setGeometry(QtCore.QRect(30, 50, 81, 21))
        self.label_7.setObjectName("label_7")

        #직종(입력)
        self.job = QtWidgets.QLabel(self.company)
        self.job.setGeometry(QtCore.QRect(110, 50, 240, 21))
        self.job.setObjectName("job")

        #설립일
        self.label_2 = QtWidgets.QLabel(self.company)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 21))
        self.label_2.setObjectName("label_2")

        #설립일(입력)
        self.establish = QtWidgets.QLabel(self.company)
        self.establish.setGeometry(QtCore.QRect(110, 80, 240, 21))
        self.establish.setObjectName("establish")

        #매출액
        self.label_3 = QtWidgets.QLabel(self.company)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 81, 21))
        self.label_3.setObjectName("label_3")

        #매출액(입력)
        self.companySales_2 = QtWidgets.QLabel(self.company)
        self.companySales_2.setGeometry(QtCore.QRect(110, 110, 240, 21))
        self.companySales_2.setObjectName("companySales_2")

        # 사원수
        self.label_6 = QtWidgets.QLabel(self.company)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 81, 21))
        self.label_6.setObjectName("label_6")

        #사원수(입력)
        self.people = QtWidgets.QLabel(self.company)
        self.people.setGeometry(QtCore.QRect(110, 140, 240, 21))
        self.people.setObjectName("people")

        #평균연봉
        self.label_4 = QtWidgets.QLabel(self.company)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 81, 21))
        self.label_4.setObjectName("label_4")

        #평균연봉(입력)
        self.sales = QtWidgets.QLabel(self.company)
        self.sales.setGeometry(QtCore.QRect(110, 170, 411, 21))
        self.sales.setObjectName("sales")

        #주소
        self.label_5 = QtWidgets.QLabel(self.company)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 21))
        self.label_5.setObjectName("label_5")

        #주소(입력)
        self.location = QtWidgets.QTextEdit(self.company)
        self.location.setGeometry(QtCore.QRect(110, 200, 250, 46))
        self.location.setObjectName("location")

        ###############################<합격스펙>란############################
        self.groupBox_4 = QtWidgets.QGroupBox(self.company)
        self.groupBox_4.setGeometry(QtCore.QRect(80, 300, 791, 80))
        self.groupBox_4.setObjectName("groupBox_4")

        #학점
        self.grade = QtWidgets.QLabel(self.groupBox_4)
        self.grade.setGeometry(QtCore.QRect(80, 20, 61, 20))
        self.grade.setObjectName("grade")

        #토익
        self.toeic = QtWidgets.QLabel(self.groupBox_4)
        self.toeic.setGeometry(QtCore.QRect(235, 20, 61, 20))
        self.toeic.setObjectName("toeic")

        #토익스피킹
        self.toeicSpeacking = QtWidgets.QLabel(self.groupBox_4)
        self.toeicSpeacking.setGeometry(QtCore.QRect(395, 20, 71, 20))
        self.toeicSpeacking.setObjectName("toeicSpeacking")

        #오픽
        self.opic = QtWidgets.QLabel(self.groupBox_4)
        self.opic.setGeometry(QtCore.QRect(535, 20, 71, 20))
        self.opic.setObjectName("opic")

        #기타 외국어
        self.other = QtWidgets.QLabel(self.groupBox_4)
        self.other.setGeometry(QtCore.QRect(690, 20, 71, 20))
        self.other.setObjectName("other")

        #자격증
        self.certificate = QtWidgets.QLabel(self.groupBox_4)
        self.certificate.setGeometry(QtCore.QRect(80, 50, 61, 20))
        self.certificate.setObjectName("certificate")

        #해외 경험
        self.experience = QtWidgets.QLabel(self.groupBox_4)
        self.experience.setGeometry(QtCore.QRect(235, 50, 61, 20))
        self.experience.setObjectName("experience")

        #수상내역
        self.award = QtWidgets.QLabel(self.groupBox_4)
        self.award.setGeometry(QtCore.QRect(390, 50, 71, 20))
        self.award.setObjectName("award")

        #인턴
        self.intern = QtWidgets.QLabel(self.groupBox_4)
        self.intern.setGeometry(QtCore.QRect(535, 50, 71, 20))
        self.intern.setObjectName("intern")

        #봉사
        self.volunteer = QtWidgets.QLabel(self.groupBox_4)
        self.volunteer.setGeometry(QtCore.QRect(695, 50, 71, 20))
        self.volunteer.setObjectName("volunteer")

        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(310, 20, 81, 21))
        self.label_19.setObjectName("label_19")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_26.setObjectName("label_26")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(480, 50, 81, 21))
        self.label_25.setObjectName("label_25")


        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(480, 20, 81, 21))
        self.label_20.setObjectName("label_20")

        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.label_17.setObjectName("label_17")

        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(620, 50, 81, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(310, 50, 81, 21))
        self.label_24.setObjectName("label_24")

        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(160, 20, 81, 21))
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(160, 50, 81, 21))
        self.label_22.setObjectName("label_22")

        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(620, 20, 81, 21))
        self.label_21.setObjectName("label_21")

        ###############################<채용>란############################
        self.groupBox_5 = QtWidgets.QGroupBox(self.company)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 30, 530, 250))
        self.groupBox_5.setObjectName("groupBox_5")

        # 인재상
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.label_11.setObjectName("label_11")

        # 인재상(입력)
        self.typed = QtWidgets.QLabel(self.groupBox_5)
        self.typed.setGeometry(QtCore.QRect(100, 30, 411, 21))
        self.typed.setObjectName("typed")

        #자격요건
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_8.setObjectName("label_8")

        #자격요건(입력)
        self.qualification = QtWidgets.QLabel(self.groupBox_5)
        self.qualification.setGeometry(QtCore.QRect(100, 60, 411, 21))
        self.qualification.setObjectName("qualification")

        #채용절차
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(20, 90, 81, 21))
        self.label_14.setObjectName("label_14")

        #채용절차(입력)
        self.process = QtWidgets.QTextEdit(self.groupBox_5)
        self.process.setGeometry(QtCore.QRect(100, 90, 411, 45))
        self.process.setObjectName("process")

        # 우대사항
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(20, 145, 81, 21))
        self.label_9.setObjectName("label_9")

        # 우대사항(입력)
        self.preferential = QtWidgets.QLabel(self.groupBox_5)
        self.preferential.setGeometry(QtCore.QRect(100, 145, 411, 21))
        self.preferential.setObjectName("preferential")

        #복지종류
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(20, 175, 120, 21))
        self.label_15.setObjectName("label_15")

        #복지종류(입력)
        self.welfare = QtWidgets.QTextEdit(self.groupBox_5)
        self.welfare.setGeometry(QtCore.QRect(100, 175, 411, 65))
        self.welfare.setObjectName("welfare")

        ###########################################################



        self.groupBox_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.groupBox_4.raise_()
        self.job.raise_()
        self.establish.raise_()
        self.companySales_2.raise_()
        self.people.raise_()
        self.location.raise_()
        self.sales.raise_()
        self.typed.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.company.setTitle(_translate("MainWindow", "기업이름"))
        self.label_2.setText(_translate("MainWindow", "설  립  일 :"))
        self.label_3.setText(_translate("MainWindow", "매  출  액 :"))
        self.label_4.setText(_translate("MainWindow", "평균 연봉 :"))
        self.label_5.setText(_translate("MainWindow", "주       소 :"))
        self.label_6.setText(_translate("MainWindow", "사  원  수 :"))
        self.label_7.setText(_translate("MainWindow", "직       종 :"))
        self.label_8.setText(_translate("MainWindow", "자격 요건 :"))
        self.label_9.setText(_translate("MainWindow", "우대 사항 :"))
        self.label_11.setText(_translate("MainWindow", "인  재  상 :"))
        self.label_14.setText(_translate("MainWindow", "채용 절차 :"))
        self.label_15.setText(_translate("MainWindow", "복지 종류 :"))
        self.groupBox_4.setTitle(_translate("MainWindow", "합격 스펙"))
        self.label_19.setText(_translate("MainWindow", "토익스피킹:"))
        self.label_26.setText(_translate("MainWindow", "자 격 증 :"))
        self.label_25.setText(_translate("MainWindow", "인 턴 :"))
        self.label_20.setText(_translate("MainWindow", "OPIC :"))
        self.label_17.setText(_translate("MainWindow", "학    점  :"))
        self.label_23.setText(_translate("MainWindow", "봉사횟수:"))
        self.label_24.setText(_translate("MainWindow", "수상  내역 :"))
        self.label_18.setText(_translate("MainWindow", "토     익  :"))
        self.label_22.setText(_translate("MainWindow", "해외경험 :"))
        self.label_21.setText(_translate("MainWindow", "외 국 어 :"))
        self.job.setText(_translate("MainWindow", "TextLabel"))
        self.establish.setText(_translate("MainWindow", "TextLabel"))
        self.companySales_2.setText(_translate("MainWindow", "TextLabel"))
        self.people.setText(_translate("MainWindow", "TextLabel"))
        self.location.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_5.setTitle(_translate("MainWindow", "채용"))
        self.qualification.setText(_translate("MainWindow", "TextLabel"))
        self.process.setText(_translate("MainWindow", "TextLabel"))
        self.preferential.setText(_translate("MainWindow", "TextLabel"))
        self.welfare.setText(_translate("MainWindow", "TextLabel"))
        self.sales.setText(_translate("MainWindow", "TextLabel"))
        self.typed.setText(_translate("MainWindow", "TextLabel"))
