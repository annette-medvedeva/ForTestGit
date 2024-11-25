#!/bin/bash
if type -t wevtutil &> /dev/null
then 
OS=MSWin
elif type -t scutil &> /dev/nullthen
OS=macOS
else
OS=Linux
fi
echo $OS