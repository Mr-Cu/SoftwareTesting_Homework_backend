# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 21:22
# @Author  : STY
# @Email   : 1455670697@qq.com
# @File    : thecalendar.py
# @Software: PyCharm

import datetime


def calendar_atom(arg_list):
    v_list_new = [str(x) for x in arg_list]
    year, month, day = arg_list[0], arg_list[1], arg_list[2]
    if (year < 1901 or year > 2049) and (month < 1 or month > 12) and (day < 1 or day > 31):
        return 'Illegal Case'
    if year < 1901 or year > 2049:
        return '年不在范围之内'
    if month < 1 or month > 12:
        return '月不在范围之内'

    if day==29:
        if month==2 and not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return '日不在范围之内'
    if day==30:
        if month==2:
            return '日不在范围之内'
    if day==31:
        if (month == 4 or month == 6 or month == 9 or month == 11 or month==2):
            return '日不在范围之内'
    if day < 1 or day > 31:
        return '日不在范围之内'
    try:
        _date = datetime.datetime.strptime('-'.join(v_list_new), '%Y-%m-%d').date()
    except Exception as e:
        return str(e)
    return str(_date + datetime.timedelta(days=1))


if __name__ == '__main__':
    print(calendar_atom([2020, 12, 31]))
