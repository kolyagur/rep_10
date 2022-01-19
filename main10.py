import pickle
import json
import yaml
from pydantic import BaseModel
from typing import Union
import pandas as pd

#записать в файл строку потом ее считать
with open('test.txt', 'w') as f:
   f.write('Строка 1')
with open('test.txt','r') as file:
   pass
   print (file.read())

#pickle
class Pick:
   def func():
      print('Hello')

with open('pickle', 'wb') as file:
   pickle.dump(Pick.func, file)
   file.close()    

with open('pickle', 'rb') as file:
   p = pickle.load(file)
   print(p)
   file.close()  

#
data = {'age': 45,
      'name': 'Peter',
      'children': 
      [
         {
            'age': 3,
            'name': 'Alice'
         }
      ],
      'married': True,
      'city': None
      }

# Сериализация json
with open('json', 'w') as write_json_file:
   json.dump(data, write_json_file)
   write_json_file.close()

json_str = json.dumps(data)

# Десериализация json
with open('json', 'r') as read_json_file:
   json_f = json.load(read_json_file)
   read_json_file.close()
   print(json_f)

# Сериализация yaml
with open('yaml', 'w') as file:
   yaml.safe_dump(data, file)
   file.close()

# Десериализация yaml
with open('yaml', 'r') as yaml_file:
   data_f = yaml.safe_load(yaml_file)
   yaml_file.close()
   print(data_f)

print('_'*100)

# Сериализация pydantic
class Class_pydantic(BaseModel):
   age: str
   name: str
   children: list
   married: bool
   city:  Union[str,None]

print(Class_pydantic(**data))

#excel в CSV
df = pd.DataFrame(data)
df.to_excel('./file_x.xlsx', sheet_name='Budgets', index=False)

f = pd.read_excel('file_x.xlsx')
f.to_csv('file_c.csv', encoding='utf-8', index=False)