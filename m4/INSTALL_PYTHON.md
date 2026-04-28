# HƯỚNG DẪN CÀI ĐẶT PYTHON

## 1. Cài đặt Python 3.7+

### Cách 1: Download từ python.org (Khuyến nghị)
1. Truy cập https://www.python.org/downloads/
2. Tải Python 3.10 hoặc 3.11 (phiên bản mới nhất)
3. Chạy file installer
4. **QUAN TRỌNG**: Đánh dấu "Add Python to PATH" ✓
5. Click "Install Now"

### Cách 2: Dùng Microsoft Store
1. Mở Microsoft Store
2. Tìm "Python"
3. Cài đặt Python 3.10 hoặc 3.11

## 2. Kiểm tra cài đặt

Mở PowerShell và chạy:
```powershell
python --version
```

Nếu thấy "Python 3.x.x" → Cài đặt thành công ✓

## 3. Cài đặt thư viện cần thiết

```powershell
pip install matplotlib
```

## 4. Chạy dự án

```powershell
cd "e:\CACMONTRENLOP\NAM3\Ki2\2. AI"
python main.py
```

Chọn:
- **2** để chạy M4 (Logic + Planning) ← Đây là yêu cầu của bạn
- **1** để chạy M1 (A* Pathfinding)
- **3** để chạy cả hai

## Khắc phục lỗi phổ biến

### Lỗi: "python: command not found" hoặc "Python t∞m th"
→ Python chưa được cài đặt hoặc chưa thêm vào PATH
→ Cài đặt lại Python và đánh dấu "Add Python to PATH"

### Lỗi: "ModuleNotFoundError: No module named 'matplotlib'"
→ Chạy: `pip install matplotlib`

### Lỗi: "No such file or directory"
→ Kiểm tra đường dẫn folder có chứa khoảng trắng "2. AI"
→ Thử: `cd "e:\CACMONTRENLOP\NAM3\Ki2\2. AI"` (với ngoặc kép)
