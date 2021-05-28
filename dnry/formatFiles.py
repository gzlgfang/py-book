# python c:\Users\scarl\.vscode\extensions\ms-python.python-2021.2.636928669\pythonFiles\pyvsc-run-isolated.py autopep8
# TODO: 应该有其他命令执行这个autopep8的脚本
# 参考文档: https://pypi.org/project/autopep8/
# => python C:\Users\scarl\AppData\Roaming\Python\Python38\site-packages\autopep8.py --in-place --aggressive E:\py-book\第1章代码\14-tup2.py


from pathlib import Path
import subprocess as sb

format_location = "E:\py-book\第1章代码"
autopep8_location = "C:\\Users\\scarl\\AppData\\Roaming\\Python\\Python38\\site-packages\\autopep8.py"

p = Path(format_location)


for p in p.glob('**/*.py'):
    sb.run(["python", f"{autopep8_location}",
            "--in-place", "--aggressive", f"{str(p)}"])
