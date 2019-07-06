def RecurFolderTree(path):
    try:
        listOfFile = os.listdir(path)
    except PermissionError:
        return []
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            allFiles.extend(FolderTree(fullPath))
        else:
            try:
                allFiles.append([fullPath, open(fullPath, 'rb').read()])
                print("Successful:", allFiles[-1][0])
            except PermissionError:
                print("Permission denied")
def FolderTree(path):
    try:
        listOfFile = os.listdir(path)
    except PermissionError:
        return []
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            allFiles.extend(RecurFolderTree(fullPath))
        else:
            try:
                allFiles.append([fullPath, open(fullPath, 'rb').read()])
                print("Successful:", allFiles[-1][0])
            except PermissionError:
                print("Permission denied")
    return allFiles
