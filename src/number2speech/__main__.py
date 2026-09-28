# 统一入口：启动器 number_to_speech.py 与命令行/图形界面都走这里。

import sys

from . import __version__
from .converter import num_to_chinese

USAGE = """用法：
    python number_to_speech.py [数字文本]   打开图形界面，或只打印该数字的中文读法
    python number_to_speech.py --gui/-g     强制打开图形界面
    python number_to_speech.py --version    显示版本号
"""


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)

    if not argv or argv[0] in ("-g", "--gui"):
        from .gui import run_gui
        run_gui()
        return

    arg = argv[0]
    if arg in ("-h", "--help"):
        print(USAGE)
    elif arg == "--version":
        print("number2speech", __version__)
    else:
        # 命令行模式：只验证"数字 -> 中文"，无需录音素材
        try:
            print(arg, "->", num_to_chinese(arg))
        except ValueError as e:             # 超出 int 上限：报错而不是硬算
            print("错误：", e)


if __name__ == "__main__":
    main()