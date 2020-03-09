import configparser
import json
import sys
config=configparser.ConfigParser()
file_name=sys.argv[2]
if sys.argv[1]!='-f':
   print("Error occured the first argument should be '-f'")
else:
   try:
     file_read=open(file_name,'r')
   except Exception as e:
     print(e)
   else:
     config.read(file_name)
     se='{'
     m=1
     sect_size=len(config.sections())
     cal=1
     for d in config.sections():
        se+='"'+d+'"'
        se+=':{'
        len_d=len(config.options(d))
        for k in config.options(d):
            se+='"'+k+'"'+':'+'"'+config[d][k]+'"'
            if m!=len_d:
               se+=','
               m+=1
        m=1
        val=len(se)
        if cal!=sect_size:
          se+='},'
          cal+=1
        else:
          se+='}'
     se+='}'
     set_dict=json.dumps(json.loads(se),indent=4)
     file_json=open("json_format.json","w")
     file_json.write(set_dict)
     file_json.close()
     print("\n\n")
     print("*********Congratulation your initalization file has successfully converted into json file**********\n")
     print("open python shell in using python3 in your shell or command line\n\n")
     print("import conv_json in python shell")

