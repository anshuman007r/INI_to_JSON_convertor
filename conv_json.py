from python_json_config import ConfigBuilder
builder=ConfigBuilder()

config=builder.parse_config('json_format.json')
access=list(config)
k=0
for i in access:

   c=i.split('.')[1]
   a="print"+"("+"config."+i+")"
   print(i.split('.')[0]+" "+c+"=")
   exec(a)
   print('\n')


   
