import math

class PhanSo:
    def __init__(self, tu_so, mau_so):
        if mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def __add__(self, other):
        new_tu_so = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        new_mau_so = self.mau_so * other.mau_so
        result = PhanSo(new_tu_so, new_mau_so)
        result.rut_gon()
        return result

    def __sub__(self, other):
        new_tu_so = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        new_mau_so = self.mau_so * other.mau_so
        result = PhanSo(new_tu_so, new_mau_so)
        result.rut_gon()
        return result

    def __mul__(self, other):
        new_tu_so = self.tu_so * other.tu_so
        new_mau_so = self.mau_so * other.mau_so
        result = PhanSo(new_tu_so, new_mau_so)
        result.rut_gon()
        return result

    def __truediv__(self, other):
        if other.tu_so == 0:
            raise ValueError("Không thể chia cho phân số có tử số bằng 0")
        new_tu_so = self.tu_so * other.mau_so
        new_mau_so = self.mau_so * other.tu_so
        result = PhanSo(new_tu_so, new_mau_so)
        result.rut_gon()
        return result

    def __str__(self):
        if self.mau_so == 1:
            return str(self.tu_so)
        return f"{self.tu_so}/{self.mau_so}"

# Sử dụng lớp PhanSo
ps1 = PhanSo(3, 4)
ps2 = PhanSo(1, 2)

print("Phân số 1:", ps1)
print("Phân số 2:", ps2)

tong = ps1 + ps2
print("Tổng:", tong)

hieu = ps1 - ps2
print("Hiệu:", hieu)

tich = ps1 * ps2
print("Tích:", tich)

thuong = ps1 / ps2
print("Thương:", thuong)
