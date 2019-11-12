#회사 이름에 관한 클래스 정의.

class PassQualification:
    def __init__(self, grade, toeic, toeicSpeacking, opic, other, certificate, experience ,award, intern, volunteer):
        self.grade = grade  # 학점
        self.toeic = toeic  # 토익
        self.toeicSpeacking = toeicSpeacking  # 토익 스피킹
        self.opic = opic  # 오픽
        self.other = other  # 기타 언어
        self.certificate = certificate  # 자격증
        self.experience = experience  # 해외경험
        self.award = award  # 수상 내역
        self.intern = intern  # 인턴
        self.volunteer = volunteer  # 자원 봉사

class Company:
    def __init__(self, company, sales, job , typed, establish, location , qualification , process , companySales, people, preferential,welfare,passQualification):
        self.company = company  #회사 이름
        self.sales = sales      #연봉
        self.job = job          #직종
        self.typed = typed        #인재상
        self.establish = establish  #설립일
        self.location = location    #위치
        self.qualification = qualification  # 자격요건
        self.process = process      #채용절차
        self.companySales = companySales    #회사 매출액
        self.people = people            #사원수
        self.preferential = preferential    #우대사항
        self.welfare = welfare    #복지종류
        self.PassQualification = passQualification #합격스팩 클래스(따로 빼뒀음)



#리스트 채우기 할 때 간편하게 쓰기 위해 구현된 함수.
    def getItemsByIndex(self,index):
        if index == 0:
            return self.company
        elif index == 1:
            return self.sales
        elif index == 2:
            return self.job
        elif index == 3:
            return self.location
        elif index == 4:
            return self.preferential
        elif index == 5:
            return self.qualification
        elif index == 6:
            return self.establish
        elif index == 7:
            return self.people
        elif index == 8:
            return self.companySales
        elif index == 9:
            return self.typed
        elif index == 10:
            return self.welfare

