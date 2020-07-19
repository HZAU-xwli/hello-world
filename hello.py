# 9 * 9 乘法口诀
for i in range(1,10):

    j=1

    while j<=i:

        print('%d * %d = %d' % (j,i,j*i),end = '  ')

        j=j+1

    print('') #用来换行
