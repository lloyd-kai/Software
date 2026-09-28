import pytest
from number2speech.converter import integer_to_chinese


# 测试用例
@pytest.mark.parametrize("s, expect",[
    ("0", "零"),
    ("10", "十"),                 # 一十
    ("1005", "一千零五"),          # 连续零只读一个
    ("10000", "一万"),             # 末尾空组不补零
    ("10005", "一万零五"),          # 组间补零
    ("100000001", "一亿零一"),     # 跨大单位补零
    ("1234567890", "十二亿三千四百五十六万七千八百九十"),
])

def test_integer(s, expect):
    assert integer_to_chinese(s) == expect

