import db
port=[{"Fan":3,"Light":2,"Tv":17,"Music_System":4}]
key_list={'Fan','Light','Modem','TV'}
needlist=db.fetch("Bhuvaneshwaran",key_list,1)
for r in needlist:
                for key in port:
                    if key[r] is not None:
                        print(key[r],type(key[r]))
##                        GPIO.output(key[r],GPIO.HIGH)
