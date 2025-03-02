bust_size = float(input("กรุณากรอกขนาด : "))

if bust_size <= 34:
    size = "XS"
elif bust_size <= 36:
    size = "S"
elif bust_size <= 38:
    size = "M"
elif bust_size <= 40:
    size = "L"
else:
    size = "XL"

print(f"ขนาดเสื้อคือ:{size}")
