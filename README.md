# Py-book

## 初始化

用`virtualenv`，统一一下需要的依赖，可能比较多

```python
virtualenv venv
(venv) pip install -r requirements.txt
```

## 语法格式化工具

- `autopep8` VS Code默认会推荐这个
- `flake8` 打包的时候会用这个做检查
- `black` 这个可以批量格式化，基本符合`flake`要求

**格式化某个文件夹**

```bash
python -m black {source_file_or_directory}
```

## 运行工具及环境

> 两个维护者的开发工具并不一致

### IDLE + PyCharm used by gzlgfang

- 用IDLE打开文件，F5运行Module的方式执行程序 

### VS Code used by FrankScarlet

VS Code插件如下：

- Python `ms-python.python` 

配置文件里追加`[python]`默认语法格式化器选项（用的默认`autopep8`），`Ctrl+Shift+P`输入`Format Document`的时候指定使用微软的Python插件格式化`.py`文件

- Jupyter `ms-toolsai.jupyter`

可装可不装，这本书里应该不涉及`.ipynb`，不过即使不装这个插件上面那个插件似乎也支持打开笔记本。

- Markdown All in One `yzhang.markdown-all-in-one`

最近发现这个插件还挺好用的。比VS Code原本默认的Markdown支持更高一点。


## 目录

- `chapters`
- `pyplot`
- `qt5`