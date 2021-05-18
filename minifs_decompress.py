# coding:utf-8
import os,sys,re
import struct
from pathlib import Path


target_firmware = sys.argv[1]
if(not target_firmware):
    exit(-1)

def p32(data):
    return struct.pack(">I",data)

def u32(data):
    '''Big endian'''
    return struct.unpack(">I",data)[0]

def read_file_offset_name(path):
    _fd = open(path,"rb")
    if(not _fd):
        print('[-] Open target firmware failed!')
        exit(-1)
    content = _fd.read()
    mini_fs_offset = content.find("MINIFS")
    if(not mini_fs_offset):
        print("[-] The rootfs of target firmware is not MINIFS!")
        exit(-1)
    first_place = content.find("\x5A\x00\x00\x80")
    if(not first_place):
        print('[-] Not found the compression data!')
        exit(-1)
    compress_offset_list =  [hex(i.start()) for i in re.finditer("\x5A\x00\x00\x80",content)]

    filenames_start = mini_fs_offset + 20

    file_list = []
    idx = 0
    while(True):
        obj = []
        filename_start = filenames_start+idx*88
        if(content[filename_start+8] == '/'):
            
            file_size = content[filename_start:filename_start+4]
            file_offset = hex(u32(content[filename_start+4:filename_start+8]))
            file_name = content[filename_start+8:filename_start+88].replace("\x00","")

            obj.append(file_offset)
            obj.append(file_name)
            file_list.append(obj)
        else:
            '''file end'''
            break
        idx += 1

    _fd.close()
    return first_place,content,file_list,compress_offset_list

def create_dictionary(file_list):
    try:
        for obj in file_list:
            path = obj[1]
            if(path[0] == '/'):
                dic = Path(path).parent
                os.system("mkdir -p .%s"%(dic))
        return True
    except:
        print('[-] Create dictionary failed!')
        exit(-1)

def write_file(start_addr,file_content,file_list,compress_offset_list):
    try:
        for obj in file_list:
            offset = obj[0]
            file_path = obj[1]
            for idx in range(len(compress_offset_list)):
                #print(compress_offset_list[idx])
                '''检查压缩数据的偏移和MINIFS中文件项的偏移是否相同'''
                if (start_addr+eval(offset) == eval(compress_offset_list[idx])):
                    
                    compress_size = eval(compress_offset_list[idx+1])-eval(compress_offset_list[idx])

                    dd_command = "dd if=%s of=.%s.bak bs=1 skip=%s count=%s"%(target_firmware,file_path,eval(compress_offset_list[idx]),compress_size)
                    os.system(dd_command)

                    lzma_command = "lzma -kdc .%s.bak> .%s;rm .%s.bak"%(file_path,file_path,file_path)
                    os.system(lzma_command)
                else:
                    #print("[*] Can not found the offset (%s) in firmware, pass."%(start_addr+eval(offset)))
                    pass

        return True
    except:
        print("[-] Write file failed!")
        exit(-1)


first_place,file_content,file_list,compress_offset_list = read_file_offset_name(target_firmware)

if(create_dictionary(file_list)):
    write_file(first_place,file_content,file_list,compress_offset_list)
