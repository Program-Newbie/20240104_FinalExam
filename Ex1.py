class Fired_Chicken :
    #建構子 品項 數量 辣度 加點 備註
    def __init__ (self,CK_type,CK_num,Spicy,Extra,Note) :
        self.CK_type = CK_type
        self.CK_num = CK_num
        self.Spicy = Spicy
        self.Extra = Extra
        self.Note = Note
    #點單
    def Order (self,CK_type,CK_num,Spicy,Extra,Note) :
        self.CK_type = CK_type
        self.CK_num = CK_num
        self.Spicy = Spicy
        self.Extra = Extra
        self.Note = Note
    #列印訂單細節
    def ShowOrderInfo (self):
        print(f"{self.CK_num}x {self.CK_type}, {self.Spicy}, {self.Extra}, \"{self.Note}\"\n")
    #更改訂單細節
    def ChangeOrderInfo (self,change_str,change_info) :

        if( change_str == "Number" ) :  # 數量
            self.CK_num = change_info
        elif( change_str == "Type") :   # 品項
            self.CK_type = change_info
        elif( change_str == "Spicy") :  # 辣度
            self.Spicy = change_info
        elif( change_str == "Extra") :  # 加點
            self.Extra = change_info
        elif( change_str == "Note") :   # 備註
            self.Note = change_info


if __name__  == "__main__" :
    #建立三個物件
    Order1 = Fired_Chicken("","","","","")
    Order2 = Fired_Chicken("","","","","")
    Order3 = Fired_Chicken("","","","","")

    Order1.Order("LargeBucket","5","No Spice","No Extra","")
    Order2.Order("SmallBucket","1","More Spice","Extra Soup","6:30pm will need")
    Order3.Order("FamilySet","1","No Spice","Extra French fries","")

    # 列印原訂單
    print("--------------------------------------------------------")
    Order1.ShowOrderInfo()
    Order2.ShowOrderInfo()
    Order3.ShowOrderInfo()

    print("--------------------------------------------------------")
    # 更改訂單細節
    Order1.ChangeOrderInfo("Number","3")                # 更改數量
    Order2.ChangeOrderInfo("Note","")                   # 更改備註
    Order3.ChangeOrderInfo("Spicy","Little Spice")      # 更改辣度
    
    Order1.ShowOrderInfo()
    Order2.ShowOrderInfo()
    Order3.ShowOrderInfo()
    print("--------------------------------------------------------")