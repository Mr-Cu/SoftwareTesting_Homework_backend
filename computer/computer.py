class SaleSystem:
    zj_price = 25  # 主机价格
    zj_max = 70  # 主机每月最大销售量
    xsq_price = 30  # 显示器价格
    xsq_max = 80  # 显示器每月最大销售量
    ws_price = 45  # 外设价格
    ws_max = 90  # 外设每月最大销售量
    min_num = 1  # 部件最小销售量

    zj_num = 0  # 主机销量
    xsq_num = 0  # 显示器销量
    ws_num = 0  # 外设销量
    sales = 0  # 销售额
    reward = 0  # 佣金

    def condition(self):
        if self.zj_num < 0 or self.xsq_num < 0 or self.ws_num < 0:
            if self.zj_num < 0 and self.zj_num!=-1:
                print("M销售值不能为负")
            if self.zj_num==-1:
                print("系统自动统计销售总额")
            if self.xsq_num < 0:
                print("I销售值不能为负")
            if self.ws_num < 0:
                print("P销售值不能为负")
            return False
        if self.zj_num < self.min_num or self.xsq_num < self.min_num or self.ws_num < self.min_num:
            print("每月应至少销售一台完整机器！")
            return False
        if self.zj_num > self.zj_max:
            print("M的值超出范围")
            return False
        if self.xsq_num > self.xsq_max:
            print("I的值超出范围")
            return False
        if self.ws_num > self.ws_max:
            print("P的值超出范围")
            return False
        return True

    def conditionstr(self):
        if self.zj_num < 0 or self.xsq_num < 0 or self.ws_num < 0:
            if self.zj_num < 0 and self.zj_num!=-1:
                return "M销售值不能为负";
            if self.zj_num==-1:
                return "系统自动统计销售总额";
            if self.xsq_num < 0:
                return "I销售值不能为负";
            if self.ws_num < 0:
                return "P销售值不能为负";
        if self.zj_num < self.min_num or self.xsq_num < self.min_num or self.ws_num < self.min_num:
            return "每月应至少销售一台完整机器！"

        if self.zj_num > self.zj_max:
            return "M的值超出范围"

        if self.xsq_num > self.xsq_max:
            return "I的值超出范围"

        if self.ws_num > self.ws_max:
            return "P的值超出范围"

    def calculatedSales(self):
        self.sales = self.zj_num * self.zj_price + self.xsq_num * \
                     self.xsq_price + self.ws_num * self.ws_price
        # print("Sales this month：" + str(self.sales))

    def calculatedReward(self):
        self.calculatedSales()

        if self.sales <= 1000:
            self.reward = self.sales * 0.1
        elif self.sales <= 1800:
            self.reward = self.sales * 0.15
        else:
            self.reward = self.sales * 0.2

        return str(self.reward)


def compute(num1, num2, num3):
    saleSystem = SaleSystem()  # 实例化销售系统

    # 输入，主机为-1终止

    if num1 < -1 or num2 < 0 or num3 < 0:
        if num1 < 0 and num1!=-1:
            return "M销售值不能为负";
        if num1==-1:
            return "系统自动统计销售总额";
        if num2 < 0:
            return "I销售值不能为负";
        if num3 < 0:
            return "P销售值不能为负";
        # return "Sales volume cannot be negative"

    saleSystem.zj_num += num1
    saleSystem.xsq_num += num2
    saleSystem.ws_num += num3

    # 判断最小销售量和最大销售量条件，符合条件则计算佣金
    if saleSystem.condition():
        return saleSystem.calculatedReward()
    else :
        return saleSystem.conditionstr()


if __name__ == '__main__':
    compute()
