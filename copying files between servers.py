'''
Transferring files between remote and local servers.
We use paramiko which is pretty handy for such transfers.
'''
import paramiko
ssh = paramiko.SSHClient()
# syntax to create sshclient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# adding known host to the local server
ssh.connect(hostname='192.168.10.10',username='ec2-user',password='user@123',port=22)
# connecting with your server
sftp_client=ssh.open_sftp()
print(dir(sftp_client))

# sftp_client.get('/home/ec2-user/paramiko_download.txt','paramiko_downloaded_file.txt')

sftp_client.chdir("/home/ec2-user")
# If you don't want to give full path, you can change the current pointing path to your desired location.
print(sftp_client.getcwd())
# To check the current pointing path location
sftp_client.get('demo.txt','C:\\Users\\Azi\\Desktop\\downloaded_file.txt')
# To get the file from remote server to local server. If the transfer is between windows and linux, make sure to use "\\" defining the path.
sftp_client.put("transfer_files.py",'/home/ec2-user/transfer_files.py')
# To put the file from local server to remote server.

sftp_client.close()
# sftp should be closed before ssh because sftp is dependent on ssh
ssh.close()
# The closure is not mandatory as would be closed after sometime, but this is recommended.