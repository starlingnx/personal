import json
import os


class PersonalInformation:

    def __init__(self, name="", age=0, email="", phone="", address=""):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

    def display(self):
        """Hiển thị thông tin dạng bảng đơn giản"""
        print("\n" + "=" * 35)
        print("       THÔNG TIN CÁ NHÂN")
        print("=" * 35)
        print(f" Họ và tên : {self.name if self.name else 'Chưa cập nhật'}")
        print(f" Tuổi      : {self.age if self.age else 'Chưa cập nhật'}")
        print(f" Email     : {self.email if self.email else 'Chưa cập nhật'}")
        print(f" Số ĐT     : {self.phone if self.phone else 'Chưa cập nhật'}")
        print(f" Địa chỉ   : {self.address if self.address else 'Chưa cập nhật'}")
        print("=" * 35 + "\n")

    def input_data(self):
        """Nhập thông tin mới từ bàn phím"""
        print("\n--- NHẬP THÔNG TIN MỚI ---")
        self.name = input("Nhập họ và tên: ").strip()

        while True:
            try:
                self.age = int(input("Nhập tuổi: "))
                break
            except ValueError:
                print("Lỗi: Tuổi phải là số nguyên! Vui lòng nhập lại.")

        self.email = input("Nhập email: ").strip()
        self.phone = input("Nhập số điện thoại: ").strip()
        self.address = input("Nhập địa chỉ: ").strip()
        print("Đã cập nhật dữ liệu thành công!")

    def to_dict(self):
        """Chuyển thành dictionary để ghi file JSON"""
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
        }

    def from_dict(self, data):
        """Đọc dữ liệu từ dictionary"""
        self.name = data.get("name", "")
        self.age = data.get("age", 0)
        self.email = data.get("email", "")
        self.phone = data.get("phone", "")
        self.address = data.get("address", "")


FILE_NAME = "person.json"


def save_to_json(person):
    """Lưu object vào file JSON"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(person.to_dict(), file, ensure_ascii=False, indent=4)
    print(f"Đã lưu dữ liệu vào file '{FILE_NAME}'.")


def load_from_json(person):
    """Đọc file JSON nếu tồn tại"""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                person.from_dict(data)
                print(f"Đã tải dữ liệu cũ từ '{FILE_NAME}'.")
        except Exception as e:
            print(f"Không thể đọc file dữ liệu cũ: {e}")


def main():
    user = PersonalInformation()
    load_from_json(user)

    while True:
        print("\n=== MENU QUẢN LÝ THÔNG TIN ===")
        print("1. Xem thông tin cá nhân")
        print("2. Nhập / Cập nhật thông tin")
        print("3. Lưu dữ liệu ra file JSON")
        print("4. Thoát chương trình")

        choice = input("Lựa chọn của bạn (1-4): ").strip()

        if choice == "1":
            user.display()
        elif choice == "2":
            user.input_data()
        elif choice == "3":
            save_to_json(user)
        elif choice == "4":
            save_to_json(user)
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lỗi: Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")


if __name__ == "__main__":
    main()
