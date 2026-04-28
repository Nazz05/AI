# M3 Report - Random Search va Q-learning

## 1. Muc tieu

Member 3 phu trach 2 bai:

- Bai 3: Tim kiem ngau nhien (Random Search) de tim duong kha thi trong GridWorld co chuong ngai vat.
- Bai 4: Su dung Q-learning de huan luyen tac nhan di tu diem bat dau den dich, sau do so sanh voi A*.

## 2. Dau vao duoc nhan tu M1

M3 su dung lai moi truong do M1 cung cap, khong tao grid rieng.

- `config.py`: chua `GRID`, `START`, `GOAL`
- `core/grid.py`: lop `GridWorld`

Y nghia:

- `GRID`: ban do dang luoi, trong do `0` la o di duoc, `1` la chuong ngai vat
- `START`: vi tri bat dau cua robot
- `GOAL`: vi tri dich can den
- `GridWorld.is_valid(x, y)`: kiem tra robot co the di den o do hay khong

## 3. Bai 3 - Random Search

### Cach lam

Robot di chuyen ngau nhien trong 4 huong: len, xuong, trai, phai. Moi lan chay duoc gioi han so buoc toi da. Neu robot den dich thi lan chay do duoc tinh la thanh cong.

### Giai thich reward

He thong su dung reward de danh gia chat luong duong di:

- Den dich: `+100`
- Moi buoc di hop le: `-1`
- Di vao tuong hoac vi tri khong hop le: `-5`

Y nghia:

- Reward cang cao thi lan chay cang tot
- Reward am lon cho thay robot da di long vong hoac va vao tuong nhieu lan

### Ket qua thu duoc

- So lan chay: 200
- So lan thanh cong: 27
- Ty le thanh cong: 13.5%

Vi du mot so lan chay:

- Lan 1: That bai, 12 buoc, reward = -202
- Lan 2: That bai, 21 buoc, reward = -166
- Lan 9: Thanh cong, 12 buoc, reward = -46

Duong di tot nhat tim duoc:

```text
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
```

Nhan xet:

- Random Search co the tim thay duong di.
- Tuy nhien ti le thanh cong thap.
- Duong di co the bi lap lai va khong toi uu.
- Vi du trong duong di tot nhat, robot van bi lap giua mot so o, cho thay cach tim kiem nay khong on dinh.

## 4. Bai 4 - Q-learning

### Cach lam

Tac nhan hoc thong qua tuong tac voi moi truong GridWorld.

- State: vi tri hien tai cua robot `(x, y)`
- Action: `UP`, `DOWN`, `LEFT`, `RIGHT`
- Reward:
  - Den dich: `+100`
  - Moi buoc di hop le: `-1`
  - Di vao tuong hoac vi tri khong hop le: `-5`

Bang Q duoc cap nhat trong qua trinh huan luyen de agent hoc hanh dong nao tot nhat tai moi vi tri.

### Giai thich cac thong so huan luyen

- `So episode huan luyen`: tong so lan agent thu hoc trong moi truong
- `So episode thanh cong`: so lan agent den duoc dich trong qua trinh huan luyen
- `Ty le thanh cong`: phan tram episode den dich thanh cong
- `Solved by greedy policy / Agent tim duoc chinh sach tot`: sau khi hoc xong, neu luon chon hanh dong co gia tri Q cao nhat thi agent van den duoc dich
- `Learned path`: duong di duoc trich xuat tu chinh sach sau khi hoc
- `Path length`: do dai duong di sau khi hoc

### Ket qua thu duoc

- So episode huan luyen: 500
- So episode thanh cong: 465
- Ty le thanh cong: 93.0%
- Agent tim duoc chinh sach tot: Co

Duong di sau khi hoc:

```text
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
```

Nhan xet:

- Q-learning hoc duoc cach den dich on dinh.
- Duong di sau khi hoc ngan hon va khong con lap nhu Random Search.

### Giai thich bang Q-learning

Bang Q co dang:

```text
(state) -> action_0: value, action_1: value, action_2: value, action_3: value
```

Trong bai nay:

- `state`: vi tri hien tai cua robot, vi du `(0, 0)`
- `action_0 = UP`
- `action_1 = DOWN`
- `action_2 = LEFT`
- `action_3 = RIGHT`

Y nghia:

- Moi gia tri Q bieu thi muc do "tot" neu chon hanh dong do tai state tuong ung
- Gia tri Q cang lon thi hanh dong cang co loi trong viec den dich

Vi du tu ket qua da chay:

```text
(0, 0) -> 0: 32.75, 1: 33.04, 2: 33.06, 3: 42.61
```

Tai vi tri `(0, 0)`, hanh dong `3 = RIGHT` co gia tri lon nhat la `42.61`, nen agent uu tien di sang phai.

Mot vi du khac:

```text
(3, 4) -> 0: 78.96, 1: 100.00, 2: 84.86, 3: 84.81
```

Tai vi tri `(3, 4)`, hanh dong `1 = DOWN` co gia tri lon nhat, vi di xuong se den ngay dich `(4, 4)`.

## 5. So sanh A* va Q-learning

Duong di A*:

```text
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
```

- Do dai duong di A*: 9 nut
- Do dai duong di Q-learning: 9 nut

Nhan xet:

- Tren grid nay, Q-learning hoc duoc duong di co do dai bang voi A*.
- Dieu nay cho thay chinh sach hoc duoc la rat tot.

## 6. Y nghia bieu do huan luyen

Bieu do Q-learning gom 3 phan:

- `Reward`: tang dan theo episode, cho thay agent hoc ngay cang tot hon
- `Steps`: giam dan theo episode, cho thay agent di den dich hieu qua hon
- `Success Rate`: tang dan, cho thay agent den dich on dinh hon sau qua trinh hoc

Lien he voi ket qua thuc te:

- Giai doan dau, reward am lon do agent di ngau nhien va chua biet cach tranh tuong
- Ve sau, reward tang dan va tiem can muc cao, cho thay agent da hoc duoc duong di tot
- So buoc giam dan ve gan do dai duong di toi uu
- Ti le thanh cong tang dan len muc cao, the hien agent den dich rat on dinh

## 7. Ket luan

- Random Search phu hop lam baseline don gian, nhung khong on dinh va khong toi uu.
- Q-learning cho ket qua tot hon ro ret.
- Member 3 da hoan thanh yeu cau cua bai 3 va bai 4 tren cung moi truong GridWorld do Member 1 cung cap.
