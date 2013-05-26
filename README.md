# ProxyTester v 2.0 #

_Python based script, can test one or multiple proxies to determine if they're alive or not._

## How to use ##

### Interactive Shell ###

The script is __extremely__ easy to use. You can use it via command line arguments or with the Interactive Shell.
To launch the program in Interactive Shell, open up the Terminal and navigate to the directory which contains the
file. Use _cd_ command to navigate. For example, if the script is located in the Desktop, type this command in the 
Terminal:

    cd Desktop
    
Or, you can simply type _cd_ and then drag&drop the folder in the Terminal. Once you are in the right dir, type 
this command to start the program in Interactive Shell:

    python ProxyTester-v.VERSION.py
    
Replace the _VERSION_ with the current version. Ex. _2.0_. NOTE: Is extremely important to have Python installed. If 
you're on a Linux/OS X machine, Python is installed by default. If you're on a Windows machine, install Python from 
here: http://www.python.org/download/

OK, now the program should start in Interactive Shell mode. The IS mode is designed to instruct the user step-by-step
so there's no need to make a tutorial. Let's now focus on the Command Line mode.

### Command Line ###

If you want to launch the script in Command Line mode, first open the Terminal and move in the right directory.
See above for instructions. Once you're in the script's dir, type this command, to show help:

    python ProxyTester-v.VERSION.py -h
    
The script can work in two modes, the SSM (Single-Scan Mode) or the MSM (Multiple-Scan Mode). If you've to test one proxy,
the SSM is the preferred mode, since it scan one and only one port. To use this mode, launch the script with this command:

    python ProxyTester-v.VERSION.py -m ssm -a [IP ADDRESS] -p [PORT] [-t] [TIMEOUT]
    
The _-t_ arg is optional, it's used to set the response timeout, default is 10 seconds. So, for example, if we want to test
the proxy __127.0.0.1__ with the port __8080__, here's how the command should look:

    python ProxyTester-v.VERSION.py -m ssm -a 127.0.0.1 -p 8080
    
Simple, huh? Now it comes the best part. The MSM is used when you have to scan __many__ proxies. If you've a file, full of proxy,
and want to scan one-by-one, the MSM is for you. For example, if we have a file, called _list.txt_, and want to scan __ALL__ the proxies,
here's the command:

    python ProxyTester-v.VERSION.py -m msm -f list.txt [-o] [OUT_FILE] [-t] [TIMEOUT]
    
The _-o_ and the _-t_ args are optional. The _-o_ defines the output file name. Basically it's a log-file created by PT, with all the proxies statuses.
_NOTE: The 'list.txt' MUST be in the same directory as the script, and the proxies must be written with this syntax: IP:PORT, Ex. 127.0.0.1:8080_

