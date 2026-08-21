class PersonalInformation:

    def __init__(self, name="", age=0, email="", phone="", address=""):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

    def display(self):
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
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
        }

    def from_dict(self, data):
        self.name = data.get("name", "")
        self.age = data.get("age", 0)
        self.email = data.get("email", "")
        self.phone = data.get("phone", "")
        self.address = data.get("address", "")
