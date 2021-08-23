class Member:

    def __init__(self,Name='',Age='',Gender='',Mobile_no='',Email='',BMI='',Duration=''):
        self.__Name=Name
        self.__Mobile_no=Mobile_no
        self.__Age=Age
        self.__Gender=Gender
        self.__Email=Email
        self.__BMI=BMI
        self.__Duration=Duration

    def setName(self,Name):
        self.__Name=Name

    def getName(self):
        return self.__Name

    def setAge(self,Age):
        self.__Age=Age
    
    def getAge(self):
        return self.__Age

    def setGender(self,Gender):
        self.__Gender=Gender

    def getGender(self):
        return self.__Gender

    def setMobile_no(self,Mobile_no):
        self.__Mobile_no=Mobile_no

    def getMobile_no(self):
        return self.__Mobile_no

    def setEmail(self,Email):
        self.__Email=Email

    def getEmail(self):
        return self.__Email

    def setName(self,BMI):
        self.__BMI=BMI

    def getBMI(self):
        return self.__BMI

    def setDuration(self,Duration):
        self.__Duration=Duration

    def getDuration(self):
        return self.__Duration

    def __str__(self):
        return self.getName()+" "+self.getMobile_no()+" "+self.getDuration()+" "+self.getAge()+" "+self.getGender()+" "+self.getBMI()+" "+self.getEmail()+" "