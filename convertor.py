def number_to_chinese(num):
    units = "零一二三四五六七八九"
    positions = ["", "十", "百", "千", "万", "亿"]
    num_str = str(num)
    length = len(num_str)
    result = ""
    
    for i, digit in enumerate(num_str):
        if digit != '0':
            result += units[int(digit)] + positions[(length - i - 1) % 4]
        elif i > 0 and num_str[i - 1] != '0':
            result += units[0]
        if (length - i - 1) % 4 == 0 and (length - i - 1) > 0:
            result += positions[4]

    return result.rstrip('零')

# print(number_to_chinese(123456789))
