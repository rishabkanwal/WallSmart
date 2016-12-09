# Read in the file
filedata = None
with open('./data/features.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('\r', '\n')

# Write the file out again
with open('./data/features.csv', 'w') as file:
  file.write(filedata)