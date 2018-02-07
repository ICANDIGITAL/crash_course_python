guest_list = ['hugh', 'majorie', 'kenny', 'dawn']
guest_list.insert(2, 'bouchy')
print("I hope you guys are well" + ", "  + guest_list[0].title() + " and your invited to dinner.")
print("I hope you guys are well" + ", "  + guest_list[1].title() + " and your invited to dinner.")
print("I hope you guys are well" + ", "  + guest_list[-1].title() + " and your invited to dinner.")
print("I hope you guys are well" + ", "  + guest_list[2].title() + " and your invited to dinner.")
print("I apologize but I can't invite all of you to dinner. There are only seats for two.")
print("Sorry, there is not enough room. Stay home " + guest_list.pop().title() + " and continue.")
print("Sorry, there is not enough room. Stay home " + guest_list.pop().title() + " and continue.")
print("Sorry, there is not enough room. Stay home " + guest_list.pop().title() + " and continue.")
print(guest_list[-2].title() + " your still invited, I have so may questions.")
print(guest_list[-1].title() + " your still invited, I have so may questions.")
del guest_list[-1]
del guest_list[0]
