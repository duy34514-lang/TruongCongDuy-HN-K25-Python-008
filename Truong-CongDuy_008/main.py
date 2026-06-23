from function import *
from class_vehicle import *

manager = VehicleManager()


def show_menu():
    print("""
================ MENU ================
1. Hiển thị danh sách phương tiện
2. Thêm phương tiện mới
3. Cập nhật phương tiện
4. Xóa phương tiện
5. Tìm kiếm phương tiện
6. Thoát
=====================================
""")


def main():
    while True:
        show_menu()

        choice = check_int(
            "Nhập lựa chọn của bạn",
            1,
            6
        )

        match choice:
            case 1:
                manager.show_all()

            case 2:
                manager.add_vehicle()

            case 3:
                manager.update_vehicle()

            case 4:
                manager.delete_vehicle()

            case 5:
                manager.search_vehicle()

            case 6:
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống quản lý phương tiện!"
                )
                break


main()
