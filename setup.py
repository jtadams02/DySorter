import os

def generateArchives(path):
    """A simple function that generates folders for the download sorter to use

    Args:
        path (str): Parameter containing the path to the downloads section
    """
    os.chdir(path)
    
    if not os.path.exists("Documents"):
    # If the PDF folder does not exist we need to create it
        os.mkdir("PDFs")
    else:
        print("PDF present")
        
    # Now we need to look for executables
    if not os.path.exists("Executables"):
        # If the .exe folder does not exist we need to create it
        os.mkdir("Executables")
    else:
        print("Exe present")


    # Now we're going to make an archive folder
    if not os.path.exists('Archives'):
        # If the archive folder does not exist we need to create it
        os.mkdir("Archives")
    else:
        print("Archives Present")
    
    # And lastly for now, I'll make an image folder
    if not os.path.exists("Images"):
        os.mkdir("Images")
    else:
        print("Images present")
        
    if not os.path.exists("Code"):
        os.mkdir("Code")
    else:
        print("Code present")

    
    