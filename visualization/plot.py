import matplotlib.pyplot as plt

# Ve hinh anh the gioi va duong di tim duoc

def draw(grid, path):
    """
    Hien thi grid va duong di bang do thi matplotlib
    
    Hien thi:
        - Grid: mau den la tuong (1), mau trang la o trong (0)
        - Duong di: duong trang noi cac diem tren duong
        
    Tham so:
        grid: Doi tuong GridWorld
        path: Danh sach vi tri tao thanh duong di
              [(x0,y0), (x1,y1), ..., (xn,yn)]
              hoac None neu khong tim duoc
    """
    
    # Hien thi grid bang heatmap
    # cmap='gray': 0 (trang), 1 (den)
    plt.imshow(grid.grid, cmap='gray')

    # Neu co duong di, ve duong di len tren grid
    if path:
        # Tach toa do x va y ra khac nhau
        # path: [(x0,y0), (x1,y1), ...]
        # x_coords: [y0, y1, ...] (cot trong matplotlib)
        # y_coords: [x0, x1, ...] (hang trong matplotlib)
        # Chu y: matplotlib dung (column, row) con grid dung (row, column)
        x = [p[1] for p in path]  # Chi so cot
        y = [p[0] for p in path]  # Chi so hang
        
        # Ve duong di bang duong trang
        plt.plot(x, y)

    # Hien thi cua so do thi
    plt.show()