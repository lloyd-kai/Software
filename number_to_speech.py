"""
项目启动器
使用方法:
    python number_to_speech.py [数字文本] 打开图形界面，可以打印该数字对应的中文读法
    python number_to_speech.py --gui
"""
import os
import sys

sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"src"))

from number2speech.__main__ import main

if __name__ == "__main__":
    main()

