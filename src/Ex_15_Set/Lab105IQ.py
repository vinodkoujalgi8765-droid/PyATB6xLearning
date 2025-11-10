a ="swiss"

def first_non_repeating():
    emp_str = ''
    for i in a:
        if i not in emp_str:
            emp_str = emp_str + i
    return emp_str
print(first_non_repeating())


