from SinhVien import SinhVien

class DanhSachSv:
    import datetime
    def __init__(self) -> None:
        self.__dssv = []
    def themSinhVien(self, sv: SinhVien):
        self.__dssv.append(sv)
    
    def xuat(self):
        for sv in self.__dssv:
            print(str(sv))
    
    def timSvTheoMssv(self, mssv:int):
        return [ sv for sv in self.__dssv if sv.mssv == mssv]

   

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.__dssv)):
            if self.__dssv[i].mssv == mssv:
                return i
        return -1
    
  

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.__dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten: str):
        return [ sv for sv in self.__dssv if sv.ten == ten]

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [ sv for sv in self.__dssv if (sv.ngay).date < ""]


def doc_file():
    dssv = DanhSachSv()
    with open("demofile.txt", 'r') as file:
        for line in file:
            maso, hoten, ngaysinh = line.strip().split(';')
            student = SinhVien(maso, hoten, ngaysinh)
            dssv.themSinhVien(student)
    return dssv

dssv = doc_file()
dssv.xuat()


