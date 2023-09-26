from HinhHoc import HinhHoc

class HinhVuong(HinhHoc):
    def __init__(self, canh: float):
        super().__init__(canh)

    def TinhDienTich(self):
        return self.canh*self.canh
    def Xuat(self):
        print(f"Hinh vuong co canh {self.canh} dt {self.TinhDienTich()}")

hinhvuong = HinhVuong(99)
hinhvuong.Xuat()

