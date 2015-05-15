if [ -z "$1" ]
then
  echo "usage: $0 <target>"
else
  nasm -f macho $1.asm
  ld -macosx_version_min 10.7.0 -o $1 $1.o
  ./$1
  rm -rf $1
fi
