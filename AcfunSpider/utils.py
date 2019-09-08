from datetime import datetime

class utils(object):
    @staticmethod
    def convetStrToDatetime(strDateTime):
        today=datetime.now()
        cur_year=str(today.year)
        if not(cur_year in strDateTime):
            postDate="%s-%s"%(cur_year,strDateTime)
        try:
            return datetime.strptime(strDateTime,"%Y-%m-%d %H:%M")
        except Exception,e:
            return datetime.now()
        
