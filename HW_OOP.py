
# 1.  الاب   (Vehicle)
class Vehicle:
    def __init__(self, vin, make, model, mileage):
        self.vin = vin              # معرف فريد
        self.make = make            # الشركة المصنعة
        self.model = model          # الموديل
        self.mileage = mileage      # عدد الكيلومترات التي تقطعها

    def get_maintenance_cost(self):
        # تكلفة صيانة أساسية ثابتة وهي 50 دولار
        return 50

    def display_info(self):
        return f"{self.make} {self.model} (VIN: {self.vin})"


# 2.  (الابناء)الفئات الفرعية المتخصصة (Subclasses)

class Car(Vehicle):
    def __init__(self, vin, make, model, mileage, passenger_capacity):
        #  super()ناخذ خصائص الاساسيةمن فئة الأب
        super().__init__(vin, make, model, mileage)
        self.passenger_capacity = passenger_capacity  # خاصية إضافية للسيارة

    # إعادة كتابة الدالة (Override) لتغيير الحسبة
    def get_maintenance_cost(self):
        return 50 + (5 * self.passenger_capacity)


class Truck(Vehicle):
    def __init__(self, vin, make, model, mileage, payload_capacity):
        super().__init__(vin, make, model, mileage)
        self.payload_capacity = payload_capacity      # خاصية إضافية للشاحنة

    # إعادة كتابة الدالة (Override) للشاحنة
    def get_maintenance_cost(self):
        return 100 + (self.mileage * 0.01)


class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, mileage, has_sidecar):
        super().__init__(vin, make, model, mileage)
        self.has_sidecar = has_sidecar                # خاصية إضافية للدراجة (True/False)

    # إعادة كتابة دالة عرض البيانات لإضافة معلومة الـ Sidecar
    def display_info(self):
        base_info = super().display_info()
        if self.has_sidecar:
            return f"{base_info} - Sidecar Edition"
        return base_info


# 3. فئة الإدارة (Fleet)
class Fleet:
    def __init__(self):
        self.vehicles = []  # قائمة لتخزين المركبات

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def total_maintenance_report(self):
        grand_total = 0
        print("=== Fleet Maintenance Report ===")
        
        # تطبيق مفهوم Polymorphism (تعدد الأشكال) هنا:
        # نستدعي نفس الدالة get_maintenance_cost وكل كائن يحسبها بطريقته الخاصة
        for vehicle in self.vehicles:
            cost = vehicle.get_maintenance_cost()
            grand_total += cost
            print(f"Vehicle: {vehicle.display_info()} | Cost: ${cost:.2f}")
            
        print("-" * 32)
        print(f"Grand Total for Fleet: ${grand_total:.2f}\n")


# 4.  (Testing code )
if __name__ == "__main__":
    # إنشاء أسطول مركبات جديد
    my_fleet = Fleet()

    # إنشاء الكائنات بقيم محددة
    car1 = Car(vin="C123", make="Toyota", model="Camry", mileage=20000, passenger_capacity=5)
    truck1 = Truck(vin="T456", make="Volvo", model="FH16", mileage=50000, payload_capacity=20)
    moto1 = Motorcycle(vin="M789", make="Harley", model="Iron 883", mileage=5000, has_sidecar=True)

    # إضافة المركبات إلى الأسطول
    my_fleet.add_vehicle(car1)
    my_fleet.add_vehicle(truck1)
    my_fleet.add_vehicle(moto1)

    # تشغيل التقرير وحساب التكاليف الإجمالية
    my_fleet.total_maintenance_report()


