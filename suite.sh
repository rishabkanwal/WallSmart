if [ "$1" = "-b" ] 
then
	FLAG="-b"
elif [ "$1" = "-s" ]
then
	FLAG="-s"
elif [ "$1" = "-f" ]
then
	FLAG="-f"
elif [ "$1" = "-fs" ]
then
	FLAG="-fs"
fi

bash train.sh $FLAG
bash test.sh $FLAG