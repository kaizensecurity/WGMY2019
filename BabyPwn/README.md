The program leak address of _IO_2_1_stdout_ so we have address of libc.
After that, it receive an address from user, then call it with parameter "DEADBEEF".

![leak](https://github.com/kaizensecurity/WGMY2019/blob/master/BabyPwn/screenshot.png)

What function will we call? system()? NO. We can't control parameter so we can't get shell with system().
Therefore, I  try to call all one_gadget() and hope that it will be successfull. 
Finally it is! We have the shell and get flag.

![flag](https://github.com/kaizensecurity/WGMY2019/blob/master/BabyPwn/flag.png)
