#NAME:iCan Digital DATE:03/01/2018 DESCRIPTION:In the program below I am utilizing the striping method to remove "whitespace". Then I am concatenating variables, in the form of strings.
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#This is where the concatenation begins and is executed in a flawless manner.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)
