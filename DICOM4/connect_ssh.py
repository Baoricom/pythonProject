from paramiko import SSHClient
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('dcmadm@10.10.9.189')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
print(ssh_stdout) #print the output of ls command