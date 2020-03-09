import configparser
import json

config=configparser.ConfigParser()

config.read('db8.ini')

'''host1=config['mysql']['host']
user1=config['mysql']['user']
passwd1=config['mysql']['password']
database1=config['mysql']['db']

host2=config['postgresql']['host']
user2=config['postgresql']['user']
passwd2=config['postgresql']['password']
database2=config['postgresql']['db']


dict_form={"mysql":{"host":host1,"user":user1,"password":passwd1,"database":database1}, "postgresql":{ "host":host2,"user":user2,"password":passwd2,"database":database2}}
set=json.dumps(dict_form,indent=4)'''
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
print("***************Congratulation your initalization file has successfully converted into json file**********************\n")
print("open python shell in using python3 in your shell or command line\n\n")
print("import conv_json in python shell")

