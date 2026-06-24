# Meeting Docs

## 1. Giới thiệu

**Meeting Docs** là hệ thống quản lý tài liệu cuộc họp được phát triển bằng Django.

Hệ thống cho phép người dùng lưu trữ, quản lý và chia sẻ tài liệu. 
Các tài liệu được người dùng upload sẽ ở trạng thái chờ duyệt và chỉ được hiển thị công khai sau khi Admin phê duyệt.

---

# 2. Chức năng hệ thống

## Guest (Khách chưa đăng nhập)

Guest có thể:

- Xem danh sách tài liệu đã được duyệt
- Tìm kiếm tài liệu
- Xem chi tiết tài liệu
- Xem thông tin tài liệu
- Xem trước nội dung tài liệu được hỗ trợ
- Tải tài liệu xuống

Guest không thể:

- Upload tài liệu
- Chỉnh sửa tài liệu
- Xóa tài liệu
- Duyệt tài liệu

---

## User (Người dùng)

User sau khi đăng nhập có thể:

- Đăng ký tài khoản
- Đăng nhập / đăng xuất
- Upload tài liệu
- Xem tài liệu của mình
- Theo dõi trạng thái duyệt
- Chỉnh sửa tài liệu đã upload
- Xem trước nội dung tài liệu
- Tải tài liệu xuống

Quy trình xử lý tài liệu:

```
User upload tài liệu
        |
        v
Trạng thái: Chờ duyệt
        |
        v
Admin kiểm tra
        |
        v
Duyệt thành công
        |
        v
Hiển thị trên hệ thống
```

---

## Admin (Quản trị viên)

Admin có quyền:

- Đăng nhập hệ thống quản trị
- Xem Dashboard
- Xem tổng số tài liệu
- Xem danh sách tài liệu chờ duyệt
- Duyệt tài liệu
- Xóa tài liệu
- Quản lý tài liệu trong hệ thống

---

# 3. Phân quyền

| Chức năng | Guest | User | Admin |
|---|---|---|---|
| Xem tài liệu | ✅ | ✅ | ✅ |
| Xem chi tiết | ✅ | ✅ | ✅ |
| Xem trước file | ✅ | ✅ | ✅ |
| Tải file | ✅ | ✅ | ✅ |
| Đăng ký | ✅ | ❌ | ❌ |
| Đăng nhập | ❌ | ✅ | ✅ |
| Upload | ❌ | ✅ | ✅ |
| Sửa tài liệu của mình | ❌ | ✅ | ✅ |
| Duyệt tài liệu | ❌ | ❌ | ✅ |
| Xóa tài liệu | ❌ | ❌ | ✅ |

---

# 4. Công nghệ sử dụng

## Backend

- Python
- Django 6.0.6

## Database

- SQLite

## Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

## Thư viện hỗ trợ

| Package | Mục đích |
|---|---|
| Django | Framework phát triển web |
| openpyxl | Đọc và hiển thị file Excel (.xlsx) |
| python-dotenv | Quản lý biến môi trường |
| sqlparse | Xử lý SQL cho Django |
| asgiref | Hỗ trợ ASGI cho Django |
| tzdata | Hỗ trợ timezone |
| packaging | Quản lý package |
| et_xmlfile | Dependency của openpyxl |

---

# 5. Hỗ trợ xem trước tài liệu

| Định dạng | Chức năng |
|---|---|
| DOCX | Đọc và hiển thị nội dung văn bản |
| XLSX | Hiển thị dữ liệu dạng bảng |
| PNG/JPG/JPEG/GIF/WEBP | Hiển thị hình ảnh |
| PDF | Mở file và tải xuống |
| Khác | Chỉ hỗ trợ tải xuống |

---

# 6. Cấu trúc thư mục

```
meetingdocs/

│── manage.py
│── requirements.txt
│── db.sqlite3
│── README.md
│
├── documents/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── upload.html
│   └── document_detail.html
│
├── static/
│
└── media/
    └── uploaded files
```

---

# 7. Yêu cầu môi trường

- Python >= 3.12
- pip
- Virtual Environment

---

# 8. Cài đặt project

## Bước 1: Clone project

```bash
git clone <repository-url>
```

Di chuyển vào thư mục:

```bash
cd meetingdocs
```

---

## Bước 2: Tạo môi trường ảo

```bash
python -m venv venv
```

Kích hoạt:

Windows:

```bash
venv\Scripts\activate
```

---

## Bước 3: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## Bước 4: Migration database

```bash
python manage.py migrate
```

---

## Bước 5: Tạo tài khoản Admin

```bash
python manage.py createsuperuser
```

Nhập:

```
Username:
Email:
Password:
```

---

## Bước 6: Chạy chương trình

```bash
python manage.py runserver
```

Truy cập:

```
http://127.0.0.1:8000/
```

---

# 9. Requirements

Các thư viện chính:

```
asgiref==3.11.1
Django==6.0.6
et_xmlfile==2.0.0
openpyxl==3.1.5
packaging==26.2
python-dotenv==1.2.2
sqlparse==0.5.5
tzdata==2026.2
```

---

# 10. Lưu ý

- Cần giữ thư mục `media/` để lưu các file được upload.
- Cần giữ file `db.sqlite3` nếu muốn giữ dữ liệu hiện tại.
- Khi thêm thư viện mới cần cập nhật:

```bash
pip freeze > requirements.txt
```

---

# 11. Developer

**Project:** Meeting Docs  
**Framework:** Django  
**Database:** SQLite