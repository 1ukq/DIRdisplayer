# DIRdisplayer

When I report on my IT projects I like the person to have a global view of the project architecture. With this in mind, the DIRdisplayer describes the architecture of a directory.

## Run
It is easily launched in the following way: `python3 display.py <path_to_dir> [path_to_file]` \
If path_to_file is not given as argument, the output is displayed on `stdout`, otherwise in the file given as argument.

## More
The DIRdisplayer doesn't display the hidden files (those who start with a '.'). But you can change that easily in the code. 
