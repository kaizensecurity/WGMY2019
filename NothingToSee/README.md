After extracting the compressed file that we downloaded,  we got "ntsh.py". 
My experience in python is not good at all! But hey let take a look what inside the python script.

First thing i want to dig into is Base64 string and follow it,  and it is base64 decompress and zlib uncompress. 
So what i did is basically just like that but i did it in my console:
	- * Extract base64 string save as a file *
	- $ base64 -d < ./extracted.dump > out
	- $ zlib-flate -uncompress < out > uncompress
	- $ file ./uncompress
		./uncompress: python 3.7 byte-compile
		
Oh is a python bytecode compiled file, nice! After googling a little bit i found a tool named "Uncompyle6" that allow us to decompile python bytecode.
Then i download the tool via python pip and use it:
	- $ mv ./uncompress ./uncompress.pyc
	- $ uncompyle6 ./uncompress.pyc > gamelogic.py
	- $ file ./gamelogic.py 
		 ./gamelogic.py: Python script, UTF-8 Unicode text executable, with very long lines

Now we have recovered the "gamelogic.py" python script. 
Remembered that "ntsh.py" python script have a DEBUG variable and we need to set that to TRUE to use its own decompiled "gamelogic.py".
Now we can edit gamelogic.py to show us more data.
Edited code:

for i in range(75):
            vp = self.game_map[(pos_y + i)]
            vp = vp[pos_x:pos_x + 145]
            vk = self.d_keys[(pos_y + i)]
            vk = vk[pos_x:pos_x + 145]
	    	    
Save "gamelogic.py" and run "ntsh.py" script again. We can see the whole map and there is our flag ^^
![map](https://github.com/kaizensecurity/WGMY2019/blob/master/NothingToSee/output.png)
