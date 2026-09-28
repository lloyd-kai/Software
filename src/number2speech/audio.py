import os
import sys
import winsound

AUDIO_MAP = {
    "零": "0.wav", "一":"1.wav","二":"2.wav","三":"3.wav","四":"4.wav","五":"5.wav","六":"6.wav","七":"7.wav","八":"8.wav","九":"9.wav",
    "十": "shi.wav","百":"bai.wav","千":"qian.wav",
    "万": "wan.wav","亿":"yi.wav",
    "点": "dian.wav","负":"fu.wav",
}

REQUIRED_CHARS = "零一二三四五六七八九十百千万亿"
OPTIONAL_CHARS = "点负"
ENV_ASSET_DIR = "N2S_ASSETS"


def default_asset_dir():
    env = os.environ.get(ENV_ASSET_DIR)
    if env:
        return env                              # ① 环境变量手工指定，优先级最高
    if getattr(sys, "frozen", False):           # ② PyInstaller 打包后
        external = os.path.join(_frozen_dir(), "assets")
        if os.path.isdir(external):
            return external                     #    exe 同级优先：换录音不用重打包
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, "assets")  # 单文件模式的解压临时目录
    cwd = os.path.join(os.getcwd(), "assets")
    if os.path.isdir(cwd):
        return cwd                              # ③ 当前工作目录
    return _project_asset_dir()                 # ④ 项目根（从 __file__ 上溯两级）
