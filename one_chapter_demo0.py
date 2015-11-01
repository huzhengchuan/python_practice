#-*- coding: UTF-8 -*-
'''
Created on 2015-11-1

@author: wxt
'''
import sys

if __name__ == '__main__':
    print "Hello World, The first python code!"
    
    ##格式话变量以及变量的定义
    mystring = "Hello world"
    print mystring
    print "%s is number %d!" % ("python", int(1.01))
    
    ##raw input
    #user = raw_input('Enter login name:')
    #password = raw_input('Enter password')
    #print 'user name is %s, password is %d' % (user, int(password))
    
    ##操作符 + - *　/　//　%　　**　　<　<=　>　>=　==　!=　　<>　　and　or　not
    print -2 * 4 + 3 ** 2
    print 4/2
    print 4//2
    print 2 < 4
    print 2 == 4
    print 2 < 4 and 3 < 4
    print 2 < 4 or 3 > 4
    print not 2 < 4
    
    ##字符串操作
    mystring = 'python is cool!'
    myname = 'The'
    print mystring[0]
    print mystring[1:]
    print mystring[-1]
    print mystring[2:-1]
    print myname + ' ' + mystring 
    
    ##列表和元组
    alist = [1, 2, 'test', 3]
    print alist[0]
    print alist[2:]
     
    ##字典
    adict = {'host': 'earth'}
    print adict['host']
    
    ##if 
    input = 7 ##int(raw_input('Input the number:'));
    if input < 5:
        print str(input) + ' is smaller than 5.'
    elif input  < 8:
        print str(input) + ' is smaller than 8 and bigger than 5.'
    else:
        print str(input) + ' is bigger than 8.'
    
    ##while for
    counter = 3;
    while counter < 0:
        print 'loop %d.' % (counter)
        counter = counter - 1
        
    tsrange = ['one', 'two', 'three']
    for item in tsrange:
        print item
    
    for eachNum in range(3):
        print eachNum
    
    fp = open('text.info', 'rw')
    fwrite(fp)
    