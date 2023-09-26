from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
from datetime import datetime
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1
    
    def timSvTheoLoai(self, loai:str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    def SVdiemRL(self):
        kq = [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > 80]
        for i in kq:
            print(i)

    def Truoc1999(self):
        # kq = [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ) and sv.trinhDo == "Cao Dang" and sv.ngaySinh < datetime.strptime(15/8/1999, "%d.%m.%Y")]
        # for i in kq:
        #     print(i)
        dssv = DanhSachSv()
        for sv in self.dssv:
            if isinstance(sv, SinhVienPhiCQ) and sv.trinhDo == "Cao Dang" and int(datetime.strptime(sv.SinhVien.ngaySinh, "%d.%m.%Y").year) < 1999:
                dssv.themSV(sv)
        return dssv
