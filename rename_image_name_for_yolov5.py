import glob, os
 
allfiles = glob.glob('*.jpg')
for afile in allfiles:
  os.rename(afile, 't_'+ afile)
 
allfiles = glob.glob('*.jpg')
count=1
for afile in allfiles:
  new_filename = str(count) + '.jpg'
  print (new_filename)
  os.rename(afile, new_filename)
  count += 1
print("Done")