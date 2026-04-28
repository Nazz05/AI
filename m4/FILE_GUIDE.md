# 📚 FILE GUIDE - Hướng dẫn tìm file

Dự án này có rất nhiều file. Đây là hướng dẫn để tìm thông tin bạn cần:

## 🎯 Tôi muốn...

### Chạy chương trình
1. **Chạy ngay**: [QUICKSTART.md](QUICKSTART.md)
2. **Cài đặt Python**: [INSTALL_PYTHON.md](INSTALL_PYTHON.md)
3. **Chạy M4 riêng**: `python demo_m4.py`

### Hiểu M4 là gì
1. **Tóm tắt nhanh**: [QUICKSTART.md](QUICKSTART.md)
2. **Giải thích chi tiết**: [MEMBER_M4.md](MEMBER_M4.md)
3. **Tóm tắt tất cả**: [M4_SUMMARY.md](M4_SUMMARY.md)

### Xem code
| Muốn xem | File | Mục đích |
|---------|------|---------|
| Logic (Part 1) | `logic/rules.py` | Predicate, Rule, KnowledgeBase |
| Inference Engine | `logic/inference.py` | Forward Chaining |
| Planning (Part 2) | `planning/strips.py` | STRIPS Algorithm |
| Domain definition | `planning/domain.py` | Actions (hành động) |
| Planner | `planning/planner.py` | Chạy planning |
| Main program | `../main.py` | Menu & chạy (ở thư mục cha) |

### Hiểu M1 (A*)
- Xem: `../search/astar.py`
- Hướng dẫn: `../README.md` - Phần "GIẢI THÍCH THUẬT TOÁN A*"

### Biết rõ cấu trúc dự án
- `../README.md` - Phần "CẤU TRÚC DỰ ÁN"
- [M4_SUMMARY.md](M4_SUMMARY.md) - Phần "📁 Cấu trúc file"

---

## 📖 Thứ tự đọc khuyến nghị

### Nếu bạn là người mới
1. [QUICKSTART.md](QUICKSTART.md) - 5 phút
2. [MEMBER_M4.md](MEMBER_M4.md) - 20 phút
3. Chạy: `python demo_m4.py`
4. Đọc code: `logic/rules.py` và `planning/strips.py`

### Nếu bạn là kỹ sư
1. [M4_SUMMARY.md](M4_SUMMARY.md) - Tổng quan
2. [MEMBER_M4.md](MEMBER_M4.md) - Chi tiết kỹ thuật
3. Đọc code từng file
4. Chạy và debug

### Nếu bạn cần cải thiện/mở rộng
1. [M4_SUMMARY.md](M4_SUMMARY.md) - Cấu trúc
2. [MEMBER_M4.md](MEMBER_M4.md) - Khái niệm
3. Đọc code chính
4. Thêm feature mới vào `domain.py`

---

## 📄 Danh sách file

### Documentation (4 file)
| File | Mục đích | Dành cho |
|------|---------|----------|
| [README.md](README.md) | Tổng quan dự án | Ai cũng cần đọc |
| [QUICKSTART.md](QUICKSTART.md) | Hướng dẫn nhanh M4 | Người mới bắt đầu |
| [MEMBER_M4.md](MEMBER_M4.md) | Chi tiết M4 (khái niệm + code) | Ai muốn hiểu sâu |
| [M4_SUMMARY.md](M4_SUMMARY.md) | Tóm tắt M4 hoàn thành | CEO/Manager |
| [INSTALL_PYTHON.md](INSTALL_PYTHON.md) | Hướng dẫn cài Python | Không có Python |
| [FILE_GUIDE.md](FILE_GUIDE.md) | File này - Hướng dẫn tìm file | Bạn đang đọc |

### Code - Logic Part (2 file)
| File | Dòng code | Mục đích |
|------|-----------|---------|
| [logic/rules.py](logic/rules.py) | ~180 | Predicate, Rule, KnowledgeBase |
| [logic/inference.py](logic/inference.py) | ~150 | LogicInferenceEngine, Forward Chaining |

### Code - Planning Part (3 file)
| File | Dòng code | Mục đích |
|------|-----------|---------|
| [planning/strips.py](planning/strips.py) | ~250 | Atom, Action, STRIPSPlanner |
| [planning/domain.py](planning/domain.py) | ~200 | Domain & Actions definition |
| [planning/planner.py](planning/planner.py) | ~150 | run_smart_home_planning(), run_logistics_planning() |

### Code - Main & Demo (3 file)
| File | Dòng code | Mục đích |
|------|-----------|---------|
| [main.py](main.py) | ~130 | Menu chính (M1 + M4) |
| [demo_m4.py](demo_m4.py) | ~40 | Demo từng phần |
| [test_import.py](test_import.py) | ~25 | Test import modules |

### Code - Existing M1 (4 file)
| File | Mục đích |
|------|---------|
| [config.py](config.py) | Cấu hình grid, START, GOAL |
| [core/grid.py](core/grid.py) | GridWorld class |
| [core/utils.py](core/utils.py) | Heuristic, reconstruct_path |
| [search/astar.py](search/astar.py) | A* algorithm |
| [visualization/plot.py](visualization/plot.py) | Vẽ grid + path |

---

## 🔍 Tìm nhanh

### Tôi muốn hiểu...

| Điều gì | Đọc file | Tìm section |
|--------|----------|-----------|
| Logic là gì | MEMBER_M4.md | "PART 1: LOGIC INFERENCE" |
| Forward Chaining | MEMBER_M4.md | "Khái niệm" → "4. Forward Chaining" |
| STRIPS là gì | MEMBER_M4.md | "PART 2: STRIPS PLANNING" |
| Ví dụ Smart Home | MEMBER_M4.md | "Ứng dụng: Smart Home Planning" |
| Cách sử dụng code | MEMBER_M4.md | "Cách sử dụng" |
| Cấu trúc thư mục | README.md | "CẤU TRÚC DỰ ÁN" |
| Lệnh chạy | QUICKSTART.md | "2️⃣ Chạy chương trình" |

### Tôi muốn xem code

| Code gì | File | Class/Function |
|---------|------|-----------------|
| Predicate | logic/rules.py | class Predicate |
| Rule | logic/rules.py | class Rule |
| Forward Chaining | logic/inference.py | LogicInferenceEngine.forward_chain() |
| Action STRIPS | planning/strips.py | class Action |
| STRIPS Planner | planning/strips.py | class STRIPSPlanner |
| Domain Smart Home | planning/domain.py | create_smart_home_domain() |
| Run Planning | planning/planner.py | run_smart_home_planning() |

---

## 💡 Tips

1. **Bắt đầu nhanh nhất**:
   ```
   Đọc: QUICKSTART.md (5 min)
   Chạy: python demo_m4.py
   ```

2. **Hiểu sâu M4**:
   ```
   Đọc: MEMBER_M4.md (30 min)
   Code: logic/rules.py + planning/strips.py
   Chạy: python main.py → Chọn 2
   ```

3. **Mở rộng M4**:
   ```
   Sửa: planning/domain.py (thêm actions)
   Chạy: python main.py → Chọn 2
   ```

4. **Debug**:
   ```
   Chạy: python test_import.py (kiểm tra import)
   Chạy: python demo_m4.py (test từng phần)
   ```

---

## ✅ Checklist

- [ ] Đã cài Python 3.7+
- [ ] Đã chạy `pip install matplotlib`
- [ ] Đã đọc [QUICKSTART.md](QUICKSTART.md)
- [ ] Đã chạy `python main.py` hoặc `python demo_m4.py`
- [ ] Đã xem kết quả Logic Inference
- [ ] Đã xem kết quả STRIPS Planning
- [ ] Đã đọc [MEMBER_M4.md](MEMBER_M4.md)
- [ ] Đã hiểu Forward Chaining
- [ ] Đã hiểu STRIPS Planning
- [ ] Sẵn sàng mở rộng/tùy chỉnh

---

**Cần giúp đỡ?** → Xem [QUICKSTART.md](QUICKSTART.md) hoặc [MEMBER_M4.md](MEMBER_M4.md)
