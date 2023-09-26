from datetime import datetime
from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSv

sv1 = SinhVienChinhQuy(195, "Tran Van A",datetime.strptime("23/6/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(196, "Tran Van C",datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiCQ(199,"Thai Thi Thu", datetime.strptime("15/8/1998", "%d/%m/%Y"),"Cao Dang", 2)
sv4 = SinhVienPhiCQ(201,"Bui Van Nam", datetime.strptime("13/7/1998", "%d/%m/%Y"),"Cao Dang", 2)
sv5 = SinhVienPhiCQ(198,"Nguyen Cong Tu", datetime.strptime("19/12/2000", "%d/%m/%Y"),"Trung Cap", 2.5)
sv6 = SinhVienChinhQuy(205,"Nguyen Thanh Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiCQ(203,"Nguyen Thanh Thanh", datetime.strptime("29/10/1999", "%d/%m/%Y"),"Trung Cap", 2.5)
sv8 = SinhVienChinhQuy(210,"Vo Hoai Nam", datetime.strptime("4/1/2000", "%d/%m/%Y"), 70)


dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

# dssv.xuat()

# vt = dssv.timSVTheoMs(199)
# print (f"Sinh vien o vi tri thu {vt + 1} trong danh sach")

# kq = dssv.timSvTheoLoai("chinhquy")
# print("Danh sach sinh vien theo loai:")
# for sv in kq:
#     print(sv)

# Tim = dssv.SVdiemRL()
# print(Tim)

Sort = dssv.Truoc1999()
Sort.xuat()