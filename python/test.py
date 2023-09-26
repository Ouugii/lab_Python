import math

def kiem_tra_so_nguyen_to(n):
   if n == 1:
       return False       
   #Su dung vong lap for de duyet cac so tu 2 den can bac hai cua n
   for i in range(2, int(math.sqrt(n))+1):
       #Kiem tra tinh chia het
       if n % i == 0:
           return False
   return True

def liet_ke_so_nguyen_to(a, b):
   for i in range(a, b + 1):
       if kiem_tra_so_nguyen_to(i):
           print(i, end=' ')

#Khoi lenh co the phat sinh loi
try:
   #Nhap hai so tu ban phim
   #Ep kieu du lieu sang so nguyen
   a = int(input())
   b = int(input())

   #Su dung cau truc re nhanh xu ly cac truong hop1
   if a < 0 or b < 0:
       print("Vui long nhap so tu nhien!")
   elif a > b:
       print("So thu nhat lon hon so thu hai!")
   else:
       liet_ke_so_nguyen_to(a, b)

#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
