from python_json_config import ConfigBuilder
builder=ConfigBuilder()

config=builder.parse_config('json_format.json')
print(config.mysql.host)
print("1) import config by typing 'config=conv_json.config'\n")
access=tuple(config)
print("2) Type the following command to access the element\n")
for i in access:
    print('config.'+i)

   
