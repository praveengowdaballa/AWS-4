#check proces on port 80
sudo netstat -lnp | grep 80

#add passphrase to ssh key
ssh-keygen -p -f <path to key>
