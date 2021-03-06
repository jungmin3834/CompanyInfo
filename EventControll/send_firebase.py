from ClassDirectory.Company import *

#회사정보와 합격스펙데이터 분리 + 파이어베이스 초기화 및 데이터 입력함수 호출
def input_data(company):
    Info_to_firebase(company)

#파이어베이스 초기화
def initialize_firebase():
    import firebase_admin
    from firebase_admin import credentials
    cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "analysis-for-company",
  "private_key_id": "2044da0542bb11ae463955fd5865d20f741668f1",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQHIXZ3zrUKJR6\nwk4wgNkLWUfMBtPRHasWg2epS6DtCGRUqJ/tX2Jy7y1+2acxkvC4tbUmnBNQCEaI\nMgbm1tHjAPDsVHfEUfektCyXlt7hrbbh/XEq+Jh3PLTT9ZS8aTXgt+NdgD8+EkFv\nXit5zDqTrOvvgl3Y1jG3idnFEN6Hbg72KvGsfOn40GUYzPdpqjlIaLYuRvdiNLXr\n57+FhPvdBIZiQB+06RFWLImiySEA6Vzk/PFUdnb/QDVbsI3im06eDp/5AJM56vhX\nCsaHqkY28cup8DpX/Um0PTVtXRCJZuc74MSPgRvIbzXmBk3s/zciWSY7JTHYa4rm\nC21T9epjAgMBAAECggEALum3HLGPK+NH8VJa2OE6zC2gmzQQzKuQ9T7C/+1eBgDl\nyRXIE3T0lu8mxNkgsPKsVB8WCnGVgu2SpMIOPzw+zRrZtJSn+Pf3SMga40Mt1Bba\nSqBcwfCPQhXLt5o9IKng7NrXJK0z1HS+DnJef5LTw5VwDCpJqIdEZtjq39sZJtL2\n4KvE043/6IS2nXGAZDmY1I52hoQwptD+jNmMHbd895Xbjk05tqBEY5jyTohwJu7p\n0ex1HJI+ntMnqydnMDR2NHNkQbJLxCdk0y/NlVx0F6/Ya+QoTXwSteDIXpFE0TQM\nhrssiQ3xok8ayRikUDqMeVi2kGXv627joJILvSkaUQKBgQDw5eBpXGh9/dSRD92l\nqxJgTj0ElI07YP57H2sGsiJ9R22rCXu5BELOsEATe7a7owRyOZa2WBDmAUG+8OxR\nheW72mzPilRYsm8mnIh78m1E71Kr/2q1dV+DAdff58tA/FzHTpF3KuFw8//PFlRl\nS7FobhQqwbZY69e9f1a/px7lEwKBgQDdKHYshOHXT83CM4sNRIha5wAeyV/rNPyA\nr8XAttWjU+jIXpWql/lo+NnpyO52ZOKSrdrrMnjmxltMlvy4XtRS79OIwsZeektG\nObj9/2HfLxGDxsG23cZzdgqZQsIAuHU+k3ENo2DrDYlZYN0/mDNGNfXGroJ3V4f1\nF6jdIkSfcQKBgEcD/XwR+dvqkFeTTcwg+nHZnrNS96+hkGPLh0maCgDUpcfeK9MH\nJoq3+qvDtMLr88uYno1yuMiVZkRb0c7WojsW0Sz9oo/jSlEfpDyl4wCHbN+3lEWa\nLGX6jSE8u/aUbuVyi/+NbJhX1fm+o3KZNduLV/ai1JayMA91EqW9JqZxAoGAPWq3\nJrXgYgLviTb3LsARfe0Yw3P5B0C3vqURresYeTscMkjSF4YM5XH2Uk5Sqt5pbYKK\ngTaLDMuZHzPvCuSK4l1nyVsN677amK3/CcqaS3iuzIGt2jLModPuLZG0fq67IJ2h\nj8AHcj9YHVIhH0ANPTpO/tYHtUzBnPbtFjwmAoECgYACwgA1XTX9KPhD6EM7ANdI\nv8OBZ3ftmaQHo+dO87wtwVb5yZZOZrftnvSmt/ERGkOFB7qN8netP+eHBGHxSPPx\n/AgVYMGkPOnQlEWIOtI4TubwjvsTeyHtmMsI5sFSsi+eoCNBk8MmkoLugx97IOAk\nMK0fFz/owEwzoUZSFSGu7w==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-7tnqu@analysis-for-company.iam.gserviceaccount.com",
  "client_id": "103197426300283058233",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7tnqu%40analysis-for-company.iam.gserviceaccount.com"
}
)
    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'https://analysis-for-company.firebaseio.com/'
        })
    
#데이터 입력함수 정의
def Info_to_firebase(company):
    from firebase_admin import db
    ref = db.reference()
    users_ref = ref.child('companies')
    users_ref.update({
        company.company: {
            'Company_info':{
            'name': company.company,
            'sales': company.sales,
            'job' : company.job,
            'typed':company.typed,
            'establish':company.establish,
            'location':company.location,
            'qualification':company.qualification,
            'process':company.process,
            'companySales':company.companySales,
            'people':company.people,
            'preferential':company.preferential,
            'welfare':company.welfare
            },
            'passQualification': {
            '학점': company.PassQualification.grade,
            '토익': company.PassQualification.toeic,
            '토익 스피킹:':company.PassQualification.toeicSpeacking,
            '오픽':company.PassQualification.opic,
            '기타언어':company.PassQualification.other,
            '자격증':company.PassQualification.certificate,
            '해외경험':company.PassQualification.experience,
            '수상 내역':company.PassQualification.award,
            '인턴':company.PassQualification.intern,
            '봉사 활동' : company.PassQualification.volunteer
            }
        }
        })

# 회사데이터 삭제
def remove(company):
    from firebase_admin import db
    ref = db.reference()
    users_ref = ref.child('companies').child(company.company)
    users_ref.delete()


#회사 검색
def search():
    from firebase_admin import db
    #데이터 읽기
    s = "companies"
    ref = db.reference(s)
    data = ref.get()
    company_list = []
    if data == None:
        return

    for k in data:
          passQulification = PassQualification(data[k]['passQualification']['학점'],data[k]['passQualification']['토익'],data[k]['passQualification']['토익 스피킹:'],data[k]['passQualification']['오픽']
                            ,data[k]['passQualification']['기타언어'],data[k]['passQualification']['자격증'],data[k]['passQualification']['해외경험'],data[k]['passQualification']['수상 내역'],
                            data[k]['passQualification']['인턴'],data[k]['passQualification']['봉사 활동'])
          company = Company(data[k]['Company_info']['name'],data[k]['Company_info']['sales'],data[k]['Company_info']['job'],data[k]['Company_info']['typed'],data[k]['Company_info']['establish'],data[k]['Company_info']['location']
                  ,data[k]['Company_info']['qualification'],data[k]['Company_info']['process'],data[k]['Company_info']['companySales'],data[k]['Company_info']['people'],data[k]['Company_info']['preferential'],data[k]['Company_info']['welfare']
                  ,passQulification)
          company_list.append(company)

    # 회사정보담긴 객체들 집합 리스트로
    return company_list
