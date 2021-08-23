class Super_user:
    regimen={}
    members=dict()
    def __int__(self,s_id,s_name):
        self.s_id=s_id
        self.s_name=s_name
    
    @classmethod
    def addMember(cls,member):
        Super_user.members[member.getMobile_no()]=member

obj=Super_user() 