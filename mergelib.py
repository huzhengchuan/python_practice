#! /usr/bin/env python
#-*- coding: UTF-8 -*-
#@Created on 2015-11-1
#@author: wxt
#@verson 2015-12-30
#description: 递归拷贝目录下的jar文件到目的目录下

import sys
import os
import shutil

def file_process(sourceFile, targetDir):
    if not os.path.exists(sourceFile):
        return
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)

    filename = os.path.basename(sourceFile)
    targetFile = os.path.join(targetDir, filename)
    if not os.path.exists(targetFile) :
        open(targetFile, "wb").write(open(sourceFile).read())
        print "%s copy to %s success!" % (sourceFile, targetFile)
    else:
        print targetFile ," is exist!"


def list_file_dir(level, rootPath, targetPath):
    for path in os.listdir(rootPath):
        absolutely_path = os.path.join(rootPath, path)
        if os.path.isdir(absolutely_path):
            list_file_dir(level + 1, absolutely_path, targetPath)
        else:
            if path.endswith(".jar"):
                file_process(absolutely_path, targetPath)



if __name__ == '__main__':
    print "The toolkit of merger java lib"
    libPath = raw_input("Enter the java lib directory:")
    regLibPath = raw_input("Enter the registratory lib directory:")

    libPath = libPath.replace('\\', '/');
    regLibPath = regLibPath.replace('\\', '/');

    if libPath.endswith('/'):
        libPath = libPath[:-1]

    if regLibPath.endswith('/'):
        regLibPath = regLibPath[:-1]

    if not os.path.exists(libPath):
        print libPath, "is not exist"
        exit

    if os.path.exists(regLibPath):
        shutil.rmtree(regLibPath)

    os.mkdir(regLibPath)

    list_file_dir(0, libPath, regLibPath)
