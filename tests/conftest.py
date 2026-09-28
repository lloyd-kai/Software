# -*- coding: utf-8 -*-
"""让 pytest 不安装包也能 import 到 src/ 下的 number2speech。

pytest 启动时会先加载本文件（conftest 是它的约定），把 src/ 插到
模块搜索路径最前面，效果等同于启动器 number_to_speech.py 里那行
sys.path.insert
"""

import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))