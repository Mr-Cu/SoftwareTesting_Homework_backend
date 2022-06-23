import decimal


class Triangle:
    def type(self, a, b, c):
        if a == 0:
            return "a不能为0"
        if b == 0:
            return "b不能为0"
        if c == 0:
            return "c不能为0"
        if a < 0:
            return "a不能小于0"
        if b < 0:
            return "b不能小于0"
        if c < 0:
            return "c不能小于0"
        if a > 800:
            return "a超出取值范围"
        if b > 800:
            return "b超出取值范围"
        if c > 800:
            return "c超出取值范围"
        if a + c > b and a + b > c and c + b > a:
            if a == b == c:
                return "等边三角形"
            elif a == b or b == c or a == c:
                return "等腰三角形"
            else:
                return "普通三角形"
        else:
            return "不是三角形"


def compute(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    t = Triangle().type(a, b, c)  # 实例化收费系统

    return t


