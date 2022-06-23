

def sales_atom(arg_list):
    annual_sales, leave_days, rate_cash_to_account = arg_list[0], arg_list[1], arg_list[2]
    if annual_sales < 0 or leave_days < 0 or rate_cash_to_account > 1 or rate_cash_to_account < 0:
        return '输入超出范围'
    if annual_sales > 200 and leave_days <= 10:
        if rate_cash_to_account >= 0.6:
            commission_rate = 7
        else:
            commission_rate = 0
    else:
        if rate_cash_to_account <= 0.85:
            commission_rate = 6
        else:
            commission_rate = 5
    if commission_rate == 0:
        return '没有输出值'
    return commission_rate

def sales_atom_1(arg_list):
    annual_sales, leave_days, rate_cash_to_account = arg_list[0], arg_list[1], arg_list[2]
    zero = float('%.2f' % 0)
    if annual_sales < 0 or leave_days < 0 or rate_cash_to_account > 1 or rate_cash_to_account < 0:
        return '输入超出范围'
    if annual_sales > 200 and leave_days <= 10:
        if rate_cash_to_account >= 0.6:
            commission_rate = 7
        else:
            commission_rate = 0
    else:
        if rate_cash_to_account <= 0.85:
            commission_rate = 6
        else:
            commission_rate = 5
    if commission_rate == 0:
        return '没有输出值'
    else:
        result = annual_sales / commission_rate
        return float('%.2f' % result)

if __name__ == '__main__':
    print(sales_atom([230, 3, 0.7]))
