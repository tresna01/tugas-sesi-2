UangBelanja = float(input("Masukan uang belanja : "))
TotalBelanja = float(input("Masukan total belanja : "))

diskon = 0.7 if TotalBelanja > 70000 else 0.0
kembalian = UangBelanja-(TotalBelanja * diskon)

print("kembalian %.0f" % kembalian)