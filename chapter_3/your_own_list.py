#NAME:CHRISTOPHER LEADER DATE:04/01/18 DESCRIPTION: Below I am storing a list of bike brand and then using concatenation to combine elements from the list inside of variables.
bicycles = ['trek', 'cannodale', 'redline', 'specialized', 'aventon']
number = 1
message_1 = "I could have bought a " + bicycles[-2].title() + " " + "but instead I brought a " + bicycles[-1].title() + "."
print(message_1)

#In the variable directly below I am utilizing the string function "str()" in order to input the fictional number of bikes that I brought.
message_2 = "I could have bought a " + bicycles[0].title() + " " + "but instead I brought " + str(number) + " " + bicycles[2].title() + "."
print(message_2)

message_3 = "I could have bought a " + bicycles[1].title() + " " + "but instead I brought a " + bicycles[-3].title() + "."
print(message_3)
