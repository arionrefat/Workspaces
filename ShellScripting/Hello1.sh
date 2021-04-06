#!/bin/sh

# This script creats an account on the local system.
# You will be promted for the account name and password.

#Ask for the user name.
read -p 'Enter your username to create: ' USER_NAME

#Ask for  the real name.
read -p 'Enter the real name of the person who this account is for: ' COMMENT

#Ask for the password
read -p 'Enter the password to use for the account: ' PASSWORD

#Create the user.
useradd -c "${COMMENT}" -m ${USER_NAME}

#useradd "${COMMENT}"

#Set the password for the user.
echo ${PASSWORD} | passwd ${USER_NAME}

#Force password change on first login.
passwd -e ${USER_NAME}

