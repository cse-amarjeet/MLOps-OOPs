from oops_proj import chatbook

user1 = chatbook()
print("user1",user1.id)

chatbook.set_id(10)
user2 = chatbook()
print("user2",user2.id)
user3 = chatbook()
print("user3",user3.id)
user4 = chatbook()
print("user4",user4.id)