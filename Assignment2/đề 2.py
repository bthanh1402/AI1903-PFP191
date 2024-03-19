class sach():
    def nhapsach(self):
        self.ten_sach = input('Nhap ten sach: ')
        self.ten_tac_gia = input('Nhap ten tac gia: ')
        self.nxb = input('Nhap ten nha xuat ban: ')
        self.nam = int(input('Nhap ten nam xuat ban: '))
        self.gia = float(input('Nhap ten gia ban: '))
        
def nhapthongtin():
    lst = []
    n = int(input('Nhap ten so cuon sach muon nhap: '))
    book = sach()
    f = open('FU.txt', 'w')
    f.write(str(n) + '\n')
    for x in range(n):
        book = sach()
        book.nhapsach()
        lst.append(book)
    for book in lst:
        f.write(book.ten_sach + '\n')
        f.write(book.ten_tac_gia + '\n')
        f.write(book.nxb + '\n')
        f.write(str(book.nam) + '\n')
        f.write(str(book.gia) + '\n' + '\n')
    f.close()

def inthongtinsach():
    book = sach()
    n = book.tongsosach
    
    print('Tong so cuon sach: ', n)
    print("{:<30} {:<30} {:<10} {:<10}".format("Ten sach", "Ten tac gia", "Nam XB", "Gia"))
    with open('FU.txt', 'r') as file:
        lstline = file.readlines()
        for i in range(1, len(lstline), 6):
            ten = lstline[i].strip()
            tacgia = lstline[i+1].strip()
            namxb = lstline[i+3].strip()
            gia = lstline[i+4].strip()
            print('{:<30} {:<30} {:<10} {:<10}'.format(ten,tacgia,namxb,gia))

def sapxeptheonam():
    with open('FU.txt', 'r') as file, open('FU2024.txt','w') as f:
        lines = file.readlines()
        n = lines[0].strip()
        f.write(str(n) + '\n')
        print('Tong so cuon sach:', n)
        print("{:<30} {:<30} {:<10} {:<10}".format("Ten sach", "Ten tac gia", "Nam XB", "Gia"))
        lines = [lines[i:i+5] for i in range(1,len(lines),6)]
        sortedlst = sorted(lines,key = lambda x: (int(x[3]),float(x[4])),reverse = True)
        for book in sortedlst:
            f.write("".join(book) + '\n')
            print('{:<30} {:<30} {:<10} {:<10}'.format(book[0].strip(),book[1].strip(),book[3].strip(),book[4].strip()))
                                    
def timtheotensach(tensach):
    found = False
    with open("FU.txt", "r") as file:
        lines = file.readlines()
        for i in range(1, len(lines), 5):
            if lines[i].strip() == tensach:
                found = True
                ten_sach = lines[i].strip()
                ten_tac_gia = lines[i + 1].strip()
                nha_xuat_ban = lines[i + 2].strip()
                print(tensach,ten_tac_gia, nha_xuat_ban)
                break
    if not found:
        print("Khong tim thay cuon sach nao!")        

def timtheotacgia(ten):
    print(ten)
    found = False
    with open("FU.txt", "r") as file:
        count = 0
        lines = file.readlines()
        for i in range(2, len(lines), 5):
            if lines[i].strip() == ten:
                found = True
                count += 1
                ten_sach = lines[i-1].strip()
                ten_tac_gia = lines[i].strip()
                nha_xuat_ban = lines[i+1].strip()
                print(ten_tac_gia, ten_sach, count)
                
    if not found:
        print("Khong tim thay ten tac gia!")   

def main():
    choice = '0'
    while (choice != '6'):
        print('1. Nhap thong tin cuon sach')
        print('2. In ra man hinh thong tin vua nhap')
        print('3. Sap xep thong tin giam dan theo nam')
        print('4. Tim kiem theo ten sach')
        print('5. Tim kiem theo ten tac gia')
        print('6. Thoat')
        choice = input('Chon chuc nang:')
        if choice == '1':
            nhapthongtin()
        elif choice == '2':
            inthongtinsach()
        elif choice == '3':
            sapxeptheonam()
        elif choice == '4':
            tensach = input('Nhap ten cuon sach can tim: ')
            timtheotensach(tensach)
        elif choice == '5':
            ten = input('Nhap ten tac gia can tim: ')
            timtheotacgia(ten)
        elif choice == '6':
            break
            
        
    
    
if __name__ == '__main__':
    main()
