from ClassDirectory.Company import *

#Ui창에 TextView들과 연동되어 있느 클래스 . 클래스 정보 받아올 때 Companyinfo.makeCompany() 하면 위에 클래스 두개 정보 받아옴
class CompanyInfo:
    class PassQualificationInfo:
        def __init__(self, window):
            self.grade = window.tv_grade  # 학점
            self.toeic = window.tv_toeic  # 토익
            self.toeicSpeacking = window.tv_toeicSpeacking  # 토익 스피킹
            self.opic = window.tv_opic  # 오픽
            self.other = window.tv_other  # 기타 언어
            self.certificate = window.tv_certificate  # 자격증
            self.experience = window.tv_experience  # 해외경험
            self.award = window.tv_award  # 수상 내역
            self.intern = window.tv_intern  # 인턴
            self.volunteer = window.tv_volunteer  # 자원 봉사

        def clearAllEditText(self):
            self.grade.setText("")
            self.toeic.setText("")
            self.toeicSpeacking.setText("")
            self.opic.setText("")
            self.other.setText("")
            self.certificate.setText("")
            self.experience.setText("")
            self.award.setText("")
            self.intern.setText("")
            self.volunteer.setText("")

        def makeUpEditText(self, company):
            self.grade.setText(company.grade)
            self.toeic.setText(company.toeic)
            self.toeicSpeacking.setText(company.toeicSpeacking)
            self.opic.setText(company.opic)
            self.other.setText(company.other)
            self.certificate.setText(company.certificate)
            self.experience.setText(company.experience)
            self.award.setText(company.award)
            self.intern.setText(company.intern)
            self.volunteer.setText(company.volunteer)

    def __init__(self,window):
        self.company = window.tv_company  # 회사 이름
        self.sales = window.tv_sales  # 연봉
        self.job = window.tv_job  # 직종
        self.typed = window.tv_type  # 인재상
        self.establish = window.tv_establish  # 설립일
        self.location = window.tv_location  # 위치
        self.qualification = window.tv_qualification  # 자격요건
        self.process = window.tv_process  # 채용절차
        self.companySales = window.tv_companySales  # 회사 매출액
        self.people = window.tv_people  # 사원수
        self.preferential = window.tv_preferential  # 우대사항
        self.welfare = window.tv_welfare  # 복지
        self.PassQualification = self.PassQualificationInfo(window)  # 합격스팩 클래스(따로 빼뒀음)

    def makeUpEditText(self,company):
        self.company.setText(company.company)
        self.sales.setText(company.sales)
        self.job.setText(company.job)
        self.typed.setText(company.typed)
        self.establish.setText(company.establish)
        self.location.setText(company.location)
        self.qualification.setText(company.qualification)
        self.process.setText(company.process)
        self.companySales.setText(company.companySales)
        self.people.setText(company.people)
        self.preferential.setText(company.preferential)
        self.welfare.setText(company.welfare)
        self.PassQualification.makeUpEditText(company.PassQualification)

    def clearAllEditText(self):
        self.company.setText("")
        self.sales.setText("")
        self.job.setText("")
        self.typed.setText("")
        self.establish.setText("")
        self.location.setText("")
        self.qualification.setText("")
        self.process.setText("")
        self.companySales.setText("")
        self.people.setText("")
        self.preferential.setText("")
        self.welfare.setText("")
        self.PassQualification.clearAllEditText()

    def makeCompany(self):
        passqualification = PassQualification(self.PassQualification.grade.text(),self.PassQualification.toeic.text(),self.PassQualification.toeicSpeacking.text(),self.PassQualification.opic.text(),self.PassQualification.other.text()
                          ,self.PassQualification.certificate.text(),self.PassQualification.experience.text() ,self.PassQualification.award.text(),self.PassQualification.intern.text(),self.PassQualification.volunteer.text())
        return Company(self.company.text(),self.sales.text(),self.job.text(),self.typed.text(),self.establish.text(),self.location.text(),self.qualification.text()
                       ,self.process.text(),self.companySales.text(),self.people.text(),self.preferential.text(),self.welfare.text(),passqualification)
