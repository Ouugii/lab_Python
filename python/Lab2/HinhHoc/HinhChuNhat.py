from HinhHoc import HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, rong: float):
        super().__init__(canh)
        self.ChieuDai = canh
        self.ChieuRong = rong

    def TinhDienTich(self):
        return self.ChieuDai*self.ChieuRong
    
    def Xuat(self):
        print(f"Hinh chu nhat co chieu dai: {self.ChieuDai}, chieu rong: {self.ChieuRong}")

hinhchunhat = HinhChuNhat