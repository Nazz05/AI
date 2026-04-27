# Cau hinh tham so chinh cua ung dung

# GRID: Ma tran dai dien the gioi
# 0 = o trong (co the di chuyen)
# 1 = tuong (khong the di chuyen)
# Kich thuoc: 5x5
GRID = [
    [0,0,0,1,0],  # Hang 0: o 0-2 trong, tuong o 3, o 4 trong
    [1,1,0,1,0],  # Hang 1: tuong 0-1, o 2 trong, tuong 3, o 4 trong
    [0,0,0,0,0],  # Hang 2: tat ca trong
    [0,1,1,1,0],  # Hang 3: o 0 trong, tuong 1-3, o 4 trong
    [0,0,0,0,0]   # Hang 4: tat ca trong
]

# VI TRI BAT DAU: Hang 0, Cot 0 (goc trai tren)
START = (0,0)

# VI TRI DICH: Hang 4, Cot 4 (goc phai duoi)
GOAL = (4,4)