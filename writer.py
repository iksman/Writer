import os, json
class Writer:
  def __init__(self,filename):
    if os.path.isfile(filename):
      self.jsonfile = open(filename, 'r+')
      self.filecontent = self.jsonfile.read()
      if json.loads(self.filecontent):
        self.content = json.loads(self.filecontent)
        self.works = [True,0,"File opened succesfully"]
      else:
        self.works = [False,1,"File not in (correct) JSON format"]
        self.content = {}
    else:
      #self.works = [False,2,"Filename not found"]
      open(filename, 'a').close()

      file = open(filename, 'r+')
      file.write('{}')
      file.close()

      self.jsonfile = open(filename, 'r+')
      self.filecontent = self.jsonfile.read()
      self.content = json.loads(self.filecontent)
      self.works = [True,3,"File created and opened succesfully"]


  def writeValue(self,key,value):
    self.content[key] = value
    self.write(self.content)
    
  def alterContent(self,content):
    self.content = content

  def write(self,content):
    #Write
    #Saves changes to file
    
    #self.content <DICT>: content to be saved
    
      
    self.jsonfile.seek(0)
    self.jsonfile.write(json.dumps(content))
    self.jsonfile.truncate()
    
  def writeAppend(self,key,value,count):
    #WriteAppend
    #Adds to an existing list or creates a new list for a specific key
    #Allows counting keys instead of appending whole items
    
    #Key <STRING>: name of database key
    #Value <STRING>: value to add to key
    #Count <BOOLEAN>: false for appending value to list, true for appending a number for existing value in key
    
    
    if count == False:
      if key in self.content and type(self.content[key]) is list:
        self.content[key] += [value]
      else:
        self.content[key] = [value]
    elif count == True:

      
      if key in self.content and type(self.content[key]) is list:
        hasIP = False
        for item in self.content[key]:
          if value in item:               #Key exists
            if type(item[value]) is int:  #check if key has int value
              item[value] += 1
              hasIP = True
        if hasIP == False: 
                     #Generate key
          self.content[key] += [{value:1}]
      else:
        self.content[key] = [{value:1}]
    else:
      if key in self.content:
        self.content[key] += [value]
      else:
        self.content[key] = [value]
    self.write(self.content)
      
      
