# Custom Python Interactive Shell

while 1:
    i = input(">>> ")
    if i == 'exit':
        break
    try:
        a = eval(i)
        if a:
            print(a)
    except:
        try:
            exec(i)
        except Exception as e:
            print("Error:", e)
