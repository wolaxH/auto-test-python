import os
import importlib.util as util
from unittest.mock import patch
dirct = os.listdir()
current_path = os.getcwd()

for i in dirct:
    if (i != "main.py" and i[-3:] == ".py"):
        program = i

module_name = program[0:-3]

# 動態import
spec = util.spec_from_file_location(module_name, program)
module = util.module_from_spec(spec)

test_data = os.listdir("data")

count = 0
for file in test_data:
    count+=1
    file_path = os.path.join(current_path, "data",file)
    print(f"\ntask {count}")

    with open(file_path, mode = 'r', encoding = 'utf-8') as data:
        datas = list()
        for line in data:
            temp = line.replace("\n", "")
            datas.append(temp)
        
        with patch("builtins.input", side_effect=datas):
            spec.loader.exec_module(module)

os.system("pause")
