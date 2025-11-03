def fun_infinte_arg(*anylist):
    print("this is parameter from user, ",anylist)
    print(type(anylist))
    for i in anylist:
        print(i)
        print(type(i))

anylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#anylist = "vinod"
#anylist={1,2,3,4}
# anylist = 'a'
# anylist= ("abc","vinod",123,123.987,True)
fun_infinte_arg(*anylist)