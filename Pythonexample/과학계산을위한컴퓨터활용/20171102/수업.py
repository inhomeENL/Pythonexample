m = 'hello'
a = 12
x = 123.123456789
y = 987.98765e-10
print("%s %s %s %s" %(m,a,x,y))
print("Message = ", m, ', liter = ', a, ', x = ', x, ' y = ', y)
print("Message = ", m, ', liter = ', a, ', x = ', x, ' y = ', y, sep ='')
print("Message = " + m + ', liter = ' + str(a) + ', x = ' + str(x) + ' y = ' + str(y))
print('x = {2}, y = {3}, Message = {0}, iter = {1}'.format(m,a,x,y))
print("Message = {}, iter = {}, x = {}, y = {}".format(m,a,x,y))
print("Message = {:10s}, iter = {:10d}, x = {:20f}, y = {:20e}".format(m,a,x,y))
print("Message = {:>10s}, iter = {:10d}, x = {:20.3f}, y = {:20.3e}".format(m,a,x,y))
print("Message = {:^10s}, iter = {:10d}, x = {:20.3f}, y = {:20.3e}".format(m,a,x,y))
print("Message = {:<10s}, iter = {:010d}, x = {:20.3g}, y = {:20.3g}".format(m,a,x,y))
print("x = {2:20.3g}, y = {3:20.3g}, Message = {0:^10s}, iter = {1:10d}".format(m,a,x,y))