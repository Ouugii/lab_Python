from HinhHoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, canh: float):
        super(). __init__(canh)
        self.BanKinh = canh
    def TinhDienTich(self):
        return self.BanKinh*3.14*2
    def Xuat(self):
        print(f"Hinh tron ban kinh: {self.BanKinh}")
    
