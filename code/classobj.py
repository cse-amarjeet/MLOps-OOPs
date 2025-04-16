# initiate a class
class employee:
    #special/magic/dunder methon constructor
    def __init__(self):
        self.employee_id = 123
        self.salary = 50000
        self.des = "sde"
    
    
    def travel(self):
        print("employee is now travelling to the destination")
sam = employee()
print(sam.salary)
sam.travel()