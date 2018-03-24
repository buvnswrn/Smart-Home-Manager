from pymongo import MongoClient
import pprint
import SHM_Bot as bot

def fetch(dat,img):
       conn=MongoClient('192.168.1.202',27017)
       db=conn.shm
       data=db.data
       key_list={'Fan','Light','Modem','TV','Music_System'}
       req_List=None
       req_List=data.find({'Name':dat})
       if req_List.count()==0:
              print("Requirements Not Found")
              bot.notify(img)
       else:
              for req in req_List:
                     print("Requirements of User:"+ req['Name'])
                     for key in key_list:
                         if(req[key]=="Checked"):
                                print(key+":Required")
                         else:
                                print(key+":Not Required")

              
def fetch(dat,key_list,k):
       conn=MongoClient('192.168.1.202',27017)
       db=conn.shm
       data=db.data
       retdata=list()
    #    key_list={'Fan','Light','Modem','TV','Music_System'}
       req_List=None
       req_List=data.find({'Name':dat})
       for req in req_List:
                     print("Requirements of User:"+ req['Name'])
                     for key in key_list:
                         if(req[key]=="Checked"):
                                print(key+":Required")
                                retdata.append(key)
                         else:
                                print(key+":Not Required")
       return retdata
    

#fetch("Bharaneef")
