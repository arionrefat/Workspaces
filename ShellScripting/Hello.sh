#!/bin/bash

#Display the UID and username of the user executing this script
#Display if the user is the Root user or not.

# Display the UID
echo "Your UID is ${UID}"

#Only display if the UID does not match 1000.
UID_TO_TEST_FOR='1000'
if [[ "${UID}" -ne "${UID_TO_TEST_FOR}" ]]
then
    echo "Your UID does not match ${UID_TO_TEST_FOR}."
    #exit 1   #if we use the exit status 1 here then the script stops right here if the exit status shows 1
fi

#Display the username.
USER_NAME=$(id -un)  # $( command inside ho) is used to capture the output of a command

#Test if the command succeeded
if [[ "${?}" -ne 0  ]]  # Here the ${?} shows the exit status of previous command
then
    echo 'The ID command did not execute succesfully.'
    exit 1
fi
echo "Your username is ${USER_NAME}"
#You can sure a string test condition
USER_NAME_TO_TEST_FOR='refat'
#if [[ "${USER_NAME}" -eq "${USER_NAME_TO_TEST_FOR}" ]]
if [[ "${USER_NAME}" = "${USER_NAME_TO_TEST_FOR}" ]]
then
    echo "Your username matches ${USER_NAME_TO_TEST_FOR}."
fi

# Text for =! (not equal) for the string
if [[ "${USER_NAME}" != "${USER_NAME_TO_TEST_FOR}" ]]
then
    echo "Your username does not match ${USERNAME_NAME_TO_TEST_FOR}"
    exit 1
fi

exit 0
