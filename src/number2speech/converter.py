"""
核心算法实现部分
这里限制输入的数字不超过int32位，如果需要超过就需要后续改进
"""

# 语言数组和单位数组
DIGITS = "零一二三四五六七八九"
SMALL_UNITS = ["","十","百","千"]

# 大数下标表
BIG_UNITS = ["","万","亿"]

# 最高支持32位
# 如果需要扩展可以修改
INT32_MAX = 2**31-1

def four_digits_to_chinese(seg):
    """
    把 1~4 位、无前导零要求的数字串转成中文

    Args:
        seg(str): 四位数字的字符串，允许前导零，

    Returns:
        str: 转换后的中文字符串
    """

    out = []
    n = len(seg)
    zero_flag = False  # 标记是否欠零
    for i, ch in enumerate(seg):
        d = int(ch)
        pos = n - 1 - i
        if d == 0:
            zero_flag = True  # 标记已经有一个零了
        else:
            if zero_flag and out:  # 如果有输出就需要补零
                out.append("零")
            zero_flag = False  # 恢复标记
            out.append(DIGITS[d] + SMALL_UNITS[pos])
    return "".join(out)


def integer_to_chinese(s):
    """
    纯数字字符串转换为中文读法

    Args:
        s(str): 必须是纯数字的字符串

    Returns:
        str: 最终转换的中文自然读法字符串
    """
    s = s.lstrip("0") # 去掉前面多余的零
    if s == "":
        return "零"

    groups = []
    while s:
        # 从后四位开始，每四位切一次
        groups.append(s[-4:])
        s = s[:-4]

    # 以下是处理零的问题
    parts = []
    need_zero = False
    for i in range(len(groups)-1, -1, -1):
        seg = groups[i]
        seg_str = four_digits_to_chinese(seg) # 每一组按四位拆开
        if seg_str == "":
            need_zero = True
            continue
        if parts and (need_zero or (len(seg) == 4 and seg[0] == "0")):
            if not parts[-1].endswith("零"):
                parts.append("零")
        need_zero = False
        parts.append(seg_str+BIG_UNITS[i])

    result = "".join(parts)

    # 对于十的特别处理
    if result.startswith("一十"):
        result = result[1:]

    return result


def digits_to_chinese(text):
    """
    将数字字符串转换为逐位读法的中文字符串，这里针对的是小数的读法

    Args:
        text(str): 必须是纯数字的字符串

    Returns:
        str: 最终转换的中文逐字读法字符串
    """
    out = []
    for ch in (text or "").strip():
        if ch.isdigit():
            out.append(DIGITS[int(ch)]) # 小数点后面的只需要查表，不需要查单位
        elif ch == ".":
            out.append("点")
        elif ch in "-负":
            out.append("负")
    return "".join(out)


def num_to_chinese(text):
    """
    数字读法转换为中文读法

    Args:
        text(str): 数字字符串

    Returns:
        str: 对应的中文读法

    """
    s = (text or "").strip()
    if not s or not any(ch.isdigit() for ch in s):
        return "" # 一个数字都没有直接返回空,用来处理异常数据

    negative = s.startswith("-") or s.startswith("负")
    if negative: # 如果是负数
        s = s[1:] # 从1开始截取

    if "." in s: # 如果是小数
        int_part, _, frac_part = s.partition(".") # 按第一个点拆
    else:
        int_part, frac_part = s,None

    int_digits = "".join(c for c in int_part if c.isdigit()) or "0"
    if int(int_digits) > INT32_MAX: # 如果大于32位，BIG_UNITS会越界
        raise ValueError("数字超过int上限%d"%INT32_MAX)
    result = integer_to_chinese(int_digits)

    # 如果有小数部分
    if frac_part is not None:
        frac_digits = "".join(c for c in frac_part if c.isdigit())
        if frac_digits:
            result+="点"+"".join(DIGITS[int(d)] for d in frac_digits) # 小数点逐位读

    if negative:
        result = "负"+result
    return result
