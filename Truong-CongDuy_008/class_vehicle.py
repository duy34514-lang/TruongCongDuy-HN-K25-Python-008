from function import *


class Vehicle:

    def __init__(
        self,
        id,
        vehicle_name,
        licence_plate,
        base_maintenance_fee,
        kilometers,
        cost_per_km
    ):

        self.id = id
        self.vehicle_name = vehicle_name
        self.licence_plate = licence_plate
        self.base_maintenance_fee = base_maintenance_fee
        self.kilometers = kilometers
        self.cost_per_km = cost_per_km

        self.total_maintenance_cost = 0
        self.maintenance_type = ""

        self.calculate_maintenance_cost()
        self.classify_maintenance()

    def calculate_maintenance_cost(self):

        self.total_maintenance_cost = (
            self.base_maintenance_fee
            +
            self.kilometers * self.cost_per_km
        )

        return self.total_maintenance_cost

    def classify_maintenance(self):

        cost = self.total_maintenance_cost

        if cost < 1000000:
            self.maintenance_type = "Thấp"

        elif cost < 5000000:
            self.maintenance_type = "Trung bình"

        elif cost < 15000000:
            self.maintenance_type = "Cao"

        else:
            self.maintenance_type = "Rất cao"

        return self.maintenance_type


class VehicleManager:

    def __init__(self):
        self.vehicles = []

    def find(self, id):

        for v in self.vehicles:

            if v.id == id:
                return v

        return None

    def add_vehicle(self):

        id = check_string("Mã phương tiện")

        if self.find(id):
            print("Mã phương tiện đã tồn tại")
            return

        name = check_string(
            "Tên phương tiện"
        )

        plate = check_string(
            "Biển số xe"
        )

        for v in self.vehicles:

            if v.licence_plate == plate:
                print("Biển số đã tồn tại")
                return

        fee = check_float(
            "Phí bảo trì cố định",
            0
        )

        km = check_int(
            "Số km đã đi",
            0
        )

        cost = check_float(
            "Chi phí/km",
            0
        )

        vehicle = Vehicle(
            id,
            name,
            plate,
            fee,
            km,
            cost
        )

        self.vehicles.append(vehicle)

        print(
            "Thêm phương tiện thành công!"
        )

    def show_all(self):

        if not self.vehicles:

            print(
                "Danh sách phương tiện đang rỗng!"
            )
            return

        for v in self.vehicles:

            print(
                f"""
--------------------------
Mã: {v.id}
Tên: {v.vehicle_name}
Biển số: {v.licence_plate}
Phí cố định: {v.base_maintenance_fee}
Km: {v.kilometers}
Chi phí/km: {v.cost_per_km}
Tổng chi phí: {v.total_maintenance_cost}
Loại: {v.maintenance_type}
--------------------------
"""
            )

    def update_vehicle(self):

        id = check_string(
            "Nhập mã phương tiện"
        )

        vehicle = self.find(id)

        if vehicle is None:

            print(
                "Không tìm thấy phương tiện cần cập nhật!"
            )
            return

        vehicle.base_maintenance_fee = check_float(
            "Phí bảo trì mới",
            0
        )

        vehicle.kilometers = check_int(
            "Số km mới",
            0
        )

        vehicle.cost_per_km = check_float(
            "Chi phí/km mới",
            0
        )

        vehicle.calculate_maintenance_cost()
        vehicle.classify_maintenance()

        print(
            "Cập nhật phương tiện thành công!"
        )

    def delete_vehicle(self):

        id = check_string(
            "Nhập mã cần xóa"
        )

        vehicle = self.find(id)

        if vehicle is None:

            print(
                "Không tìm thấy phương tiện cần xóa!"
            )
            return

        confirm = input(
            "Bạn có chắc muốn xóa phương tiện này không? (Y/N): "
        )

        if confirm.lower() == "y":

            self.vehicles.remove(vehicle)

            print(
                "Xóa phương tiện thành công!"
            )

        elif confirm.lower() == "n":

            print(
                "Đã hủy thao tác xóa!"
            )

        else:

            print(
                "Lựa chọn không hợp lệ"
            )

    def search_vehicle(self):

        key = check_string(
            "Nhập từ khóa tìm kiếm"
        ).lower()

        result = []

        for v in self.vehicles:

            if (
                key in v.vehicle_name.lower()
                or
                key in v.licence_plate.lower()
            ):
                result.append(v)

        if not result:

            print(
                "Không tìm thấy phương tiện phù hợp!"
            )
            return

        for v in result:

            print(
                f"{v.id} | {v.vehicle_name} | {v.licence_plate}"
            )
