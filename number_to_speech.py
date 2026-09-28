# 启动器保留
import os
import sys

sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"src"))

from number2speech.__main__ import main

if __name__ == "__main__":
    main()

