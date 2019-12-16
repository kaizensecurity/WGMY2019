The program have 3 main functions: cook, discard, serve

I.  cook():
    When we call cook(), the program malloc(0x18)(I call this memory the container) to store:</br>
            1. The address 0x400866, used when we call serve() function.</br>
            2. The address of the name of the dish</br>
            3. The address of the ingredients</br>
        
   ![cook](https://github.com/kaizensecurity/WGMY2019/blob/master/masakan/cook.png)
        
II. discard():</br>
            1.free(The address of the ingredients)</br>
            2.free(The address of the container)</br>
            Bug here: The program does not make the container's pointer zero so we can use it later.
    
   ![discard](https://github.com/kaizensecurity/WGMY2019/blob/master/masakan/discard.png)
    
III.serve():</br>
    This function does not call any printf or puts function to show the ingredients.</br>
    Instead, it call the address 0x400866 it store before to do that stuff.</br>
    
  ![serve](https://github.com/kaizensecurity/WGMY2019/blob/master/masakan/serve.png)

With the bug in II, we can control the address that the serve() function will call.</br>
First, we overwrite the parameter of the function at 0x400866 to leak the address of puts() in libc.</br>

   ![004](https://github.com/kaizensecurity/WGMY2019/blob/master/masakan/0x400866.png)
    
Then, we calculate the address of one_gadget(), overwrite 0x400866 with it.</br>
Finally, we call serve() function to trigger the one_gadget() to execute, then we get shell and have the flag.</br>

   ![flag](https://github.com/kaizensecurity/WGMY2019/blob/master/masakan/flag.png)
