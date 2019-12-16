The program have 3 main functions: cook, discard, serve

I.  cook():
    When we call cook(), the program malloc(0x18)(I call this memory the container) to store:
        1. The address 0x400866, used when we call serve() function.
        2. The address of the name of the dish
        3. The address of the ingredients
        
II. discard():
    1.free(The address of the ingredients)
    2.free(The address of the container)
    Bug here: The program does not make the container's pointer zero so we can use it later.
    
III.serve():
    This function does not call any printf or puts function to show the ingredients. Instead, it call the address 0x400866 it store before to do that stuff.

With the bug in II, we can control the address that the serve() function will call.
First, we overwrite the parameter of the function at 0x400866 to leak the address of puts() in libc.
Then, we calculate the address of one_gadget(), overwrite 0x400866 with it.
Finally, we call serve() function to trigger the one_gadget() to execute, then we get shell and have the flag.
