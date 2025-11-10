def fun_multiple_return(a,b):
    return a+b, a-b, a*b, a/b

print(fun_multiple_return(6,2))
result_sum,result_sub,result_mul,result_div = fun_multiple_return(6,2)
print({result_sum,result_sub})
total = fun_multiple_return(6,2)
print(total)