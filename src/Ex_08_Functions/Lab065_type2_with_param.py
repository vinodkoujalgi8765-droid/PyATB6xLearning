def fun_with_parameter(firstname, lastname, age):
    #print("Hi I am fun with parameter and with print")
    print("firstname:--",firstname,"\nlastname:--",lastname,"\nage:--",age)

fun_with_parameter("koujalgi","vinod",36)
#Positions are interchanged and python provide oytpu according to arguments positions
print()
fun_with_parameter(36,"vinod","koujalgi")
# To avoid such confussion required to use kwarguments, as bellow
print()
fun_with_parameter(age=36,firstname="vinod",lastname="koujalgi")


