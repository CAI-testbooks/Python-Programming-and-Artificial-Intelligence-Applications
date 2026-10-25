def my_function():
    local_var = "I am local"
    print(local_var)

my_function()        # 输出: I am local
print(local_var)    # NameError: name 'local_var' is not defined
