#!/bin/bash

# include user messages in prelude
help_msg='Usage: ./deploy.sh <hosted html dir> <hosted images dir>\n\n'
help_msg+='Copies book.html to <hosted html dir> and copies images to\n'
help_msg+='<hosted images dir>. Hosted dirs should be hosted by web server.\n'

no_book_msg='ERROR: No book.html found in this directory. Have you ran make yet?\n'
copy_err1_msg='ERROR: Copying "./book.html" to first argument location failed.\n'
copy_err2_msg='ERROR: Copying "./images/*" to second argument location failed.\n'

success_msg='Book deployed to specified directories!\n'

# print Usage message for either -h or other than two arguments passed
if [ "$#" != 2 ] ; then
	printf "$help_msg"
	exit 1
fi

# abort if book.html doesn't exist
if [ ! -f ./book.html ] ; then
	printf "\n"
	printf "$no_book_msg"
	exit 1
fi

# copy book to specified dir
cp ./book.html $1

#check for errors
if [ "$?" != "0" ] ; then
    printf "\n"
    printf "$copy_err1_msg"
    exit 1
fi

# copy images to specified dir
cp ./images/* $2

#check for errors
if [ "$?" != "0" ] ; then
    printf "\n"
    printf 
    exit 1
fi

printf "\n"
printf "$success_msg"
exit 0
