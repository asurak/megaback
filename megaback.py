from mega import Mega
import sys

# Configuration
mega_username = ""
mega_password = ""
#

script, action = sys.argv

allowed_actions = ["upload","delete","cleanup"]

if action not in allowed_actions:
  print "Unknown command"
  sys.exit(1)

mega = Mega()

m = mega.login(mega_username,mega_password)

if action == "upload":
  filename = sys.argv[2]
  file = m.upload(filename)
  print m.get_upload_link(file)
  sys.exit(0)

elif action == "delete":
  filename = sys.argv[2]
  if "https" in filename:
    m.destroy_url(filename)
  else:
    m.destroy(filename)
  sys.exit(0)

elif action == "cleanup":
  files = m.get_files()

  for file,atr in files.items():
    if "k" in atr.keys():
      try:
        m.destroy(file)
      except ValueError:
        print "Error deleting file {0}".format(file)

  sys.exit(0)
