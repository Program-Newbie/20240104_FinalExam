class Employee:
    # 建構子 名稱 年資 每月工作時數
    def __init__(self,name,salary_years,worktime) :
        self.name = name
        self.salary_years = salary_years
        self.worktime = worktime
    # 查詢 名字 年資 每月工作時數
    def ShowName(self):
        return self.name
    def ShowSalary(self):
        return self.salary_years
    def ShowWorkTime(self):
        return self.worktime
    # 月薪計算 增加每月工時 增加年資
    def MonthSalary(self):
        return 500 * self.worktime
    def AddWorkTime(self,add):
        self.worktime += add
    def AddSalary(self,add):
        self.salary_years += add

class Drinks:
    #建構子 名稱 甜度 價格
    def __init__ (self,name,sweet,price):
        self.name = name
        self.sweet = sweet
        self.price = price
    #更改 名稱 甜度 價格
    def ChangeName (self,name):
        self.name = name
    def ChangeSweet (self,sweet):
        self.sweet = sweet
    def ChangePrice (self,price):
        self.price = price

class ColdDrink(Drinks) : 
    #建構子 名稱 冰度 甜度 價格
    def __init__ (self,name,cold,sweet,price) :
        self.name = name
        self.sweet = sweet
        self.price = price
        self.cold = cold
    #顯示內容
    def Print(self):
        print(f"{self.name}, {self.cold} Ice, {self.sweet} Suger, {self.price}\n")

class HotDrink(Drinks) : 
    #顯示內容
    def Print(self):
        print(f"{self.name}, {self.sweet} Suger, {self.price}\n")

if __name__ == "__main__" :
    #飲料 各建立三個物件
    C1 = ColdDrink("Milk","More","Less","40")
    C2 = ColdDrink("BlackTea","Full","Full","45")
    C3 = ColdDrink("GreenTea","Less","Less","30")
    H1 = HotDrink("CoCo","Half","75")
    H2 = HotDrink("Coffee","Less","60")
    H3 = HotDrink("Espresso","Full","70")

    print(f"\n---------------------Drinks----------------------\n")
    C1.Print()
    C1.ChangeName("MilkTea")    #更改名稱
    C1.Print()

    C2.Print()
    C2.ChangeSweet("Less")      #更改甜度
    C2.Print()

    C3.Print()
    C3.ChangePrice("45")        #更改價格
    C3.Print()

    print(f"--------Hot Drink---------\n")

    H1.Print()
    H1.ChangeName("Latte")      #更改名稱
    H1.Print()

    H2.Print()
    H2.ChangeSweet("Full")      #更改甜度
    H2.Print()

    H3.Print()
    H3.ChangePrice("75")        #更改價格
    H3.Print()

    #員工 建立三位
    print(f"--------------------Employee---------------------\n")
    E1 = Employee("David",1100000,176)
    E2 = Employee("Kavin",1050000,109)
    E3 = Employee("Aris",1040000,115)
    
    # E1
    print(f"------E1------")
    print(f"{E1.ShowName()} Work {E1.ShowWorkTime()} hr/month")
    print(f"Get {E1.MonthSalary()}/month , {E1.ShowSalary()}/year\n")
    #增加年薪 每月工作時數
    E1.AddSalary(10000)
    E1.AddWorkTime(24)
    print(f"{E1.ShowName()} Work {E1.ShowWorkTime()} hr/month")
    print(f"Get {E1.MonthSalary()}/month , {E1.ShowSalary()}/year\n")

    #E2
    print(f"------E2------")
    print(f"{E2.ShowName()} Work {E2.ShowWorkTime()} hr/month")
    print(f"Get {E2.MonthSalary()}/month , {E2.ShowSalary()}/year\n")
    #增加年薪 每月工作時數
    E2.AddSalary(7000)
    E2.AddWorkTime(24)
    print(f"{E2.ShowName()} Work {E2.ShowWorkTime()} hr/month")
    print(f"Get {E2.MonthSalary()}/month , {E2.ShowSalary()}/year\n")

    #E3
    print(f"------E3------")
    print(f"{E3.ShowName()} Work {E3.ShowWorkTime()} hr/month")
    print(f"Get {E3.MonthSalary()}/month , {E3.ShowSalary()}/year\n")
    #增加年薪 每月工作時數
    E3.AddSalary(3000)
    E3.AddWorkTime(24)
    print(f"{E3.ShowName()} Work {E3.ShowWorkTime()} hr/month")
    print(f"Get {E3.MonthSalary()}/month , {E3.ShowSalary()}/year\n")

    print(f"--------------------------------------------------")

    