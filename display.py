import sys, os

# Init variables
path_to_folder = None
path_to_file = 0
tab = "| "

# Display function display the organisation of the folder <path_to_folder> in the file <path_to_file> with <tab> as symbols
def display(path_to_dir, path_to_file):
    if(path_to_folder[-1] != "/"):
        path_to_folder += "/"

    f = open(path_to_file, "a")

    def aux(path_to_folder, signs):
        dir = os.listdir(path_to_dir)
        dir.sort()
        for file in dir:
            if(file[0] != "."):
                f.write(signs + file + "\n")
                if(os.path.isdir(path_to_dir + file)):
                    aux(path_to_dir + file + "/", signs + tab)

    aux(path_to_folder, "")
    f.close()

# Handle arguments
nb_arguments = len(sys.argv)
if(nb_arguments < 2):
    sys.exit("Usage: " + sys.argv[0] + " <path_to_folder> [path_to_file]")
    exit(0)
else:
    path_to_folder = sys.argv[1]
    if(nb_arguments > 2):
        path_to_file = sys.argv[2]

# Execute display
display(path_to_dir, path_to_file)
