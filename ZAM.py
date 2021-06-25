printers = []
for i in range(10):
    def printer():
        print(i)
        print('iiii')
    i = 32
    printers.append(printer)

print(printers[6]())       
