from HinhChuNhat import HinhChuNhat
from HinhHoc import HinhHoc
from HinhTron import HinhTron
from HinhVuong import HinhVuong

class DSHinhHoc:
    def __init__(self):
        self.__DSHinhHoc = []
    
    def ThemHinh(self, hh: HinhHoc):
        self.__DSHinhHoc.append(hh)

    def Xuat(self):
        for hh in self.__DSHinhHoc:
            hh.Xuat()