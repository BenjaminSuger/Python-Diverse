#given by the subject
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#my code starts here to transform each "containers"

ft_list[1] = "World!"

ft_tuple = ft_tuple[:1] + ("France!",)

ft_set.remove("tutu!")
ft_set.remove("Hello")
ft_set.add("Hello")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

#print given by the subject
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
