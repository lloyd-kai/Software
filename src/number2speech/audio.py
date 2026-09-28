import os
import sys
import threading

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


# 素材目录三级解析


# 播放器类
class Player:
    def __init__(self,asset_dir=None):
        self.asset_dir = asset_dir or default_asset_dir()
        self._stop = threading.Event()

