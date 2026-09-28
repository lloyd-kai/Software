import os
import threading
import time

import winsound

AUDIO_MAP = {
    "零": "0.wav", "一":"1.wav","二":"2.wav","三":"3.wav","四":"4.wav","五":"5.wav","六":"6.wav","七":"7.wav","八":"8.wav","九":"9.wav",
    "十": "shi.wav","百":"bai.wav","千":"qian.wav",
    "万": "wan.wav","亿":"yi.wav",
    "点": "dian.wav","负":"fu.wav",
}

REQUIRED_CHARS = "零一二三四五六七八九十百千万亿"
OPTIONAL_CHARS = "点负"

# 指定素材目录
ENV_ASSET_DIR = "N2S_ASSETS"


# 素材目录解析
def _project_asset_dir():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(here))
    return os.path.join(root, "assets")

# 返回素材目录
def default_asset_dir():
    env = os.environ.get(ENV_ASSET_DIR) # 使用你自定义的环境变量

    if env:
        return env

    cwd = os.path.join(os.getcwd(), "assets")
    if os.path.isdir(cwd):
        return cwd
    return _project_asset_dir()

# 查询音频的完整性
def wav_path(char,asset_dir):
    wav = AUDIO_MAP.get(char)
    return os.path.join(asset_dir, wav) if wav else None




# 播放器类
class Player:
    """顺序播放器。

    winsound 的 SND_SYNC 会阻塞到当前片段播完，天然保证不重叠、不吞音；
    SND_PURGE 用于"停止"按钮，立即打断正在播放的片段。
    """
    def __init__(self,asset_dir=None):
        self.asset_dir = asset_dir or default_asset_dir()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()
        winsound.PlaySound(None, winsound.SND_PURGE)  # 掐断当前播放的片段

    def play(self,chinese_text,gap = 0.0):
        self._stop.clear()
        for ch in chinese_text:
            if self._stop.is_set():
                return
            path = wav_path(ch,self.asset_dir)
            if path and os.path.exists(path):
                winsound.PlaySound(path, winsound.SND_FILENAME)
                if gap>0:
                    time.sleep(gap)
