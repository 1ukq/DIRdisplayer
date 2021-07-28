import sys, os

def display(path_to_folder, path_to_file, sign):
    if(path_to_folder[-1] != "/"):
        path_to_folder += "/"

    f = open(path_to_file, "a")

    def aux(path_to_folder, signs):
        dir = os.listdir(path_to_folder)
        dir.sort()
        for file in dir:
            f.write(signs + file + "\n")
            if(os.path.isdir(path_to_folder + file)):
                aux(path_to_folder + file + "/", signs + "| ")

    aux(path_to_folder, "")
    f.close()

# Handle arguments
path_to_folder = None
path_to_file = 0
sign = "| "

nb_arguments = len(sys.argv)
if(nb_arguments < 2):
    sys.exit("Usage " + sys.argv[0] + " <path_to_folder> [path_to_file]")
    exit(0)
else:
    path_to_folder = sys.argv[1]
    if(nb_arguments > 2):
        path_to_file = sys.argv[2]
        if(nb_arguments > 3):
            sign = sys.argv[3]

# Execute display
display(path_to_folder, path_to_file, sign)
