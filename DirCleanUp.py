import shutil, os
import pprint
import csv

class DirCleanUp:
    config = {}
    dir_path =""
    all_files=[]
    wif = False
    action = ""

    def __init__(self,config_path): 
        self.all_file_ext = {}
        self.destination = ""
        self.config = {}
        self.read_config(config_path)

        

    # This method is for showing all the different file 
    # Extention available in the directory. 
    def show_file_ext(self):
        pprint.pprint(self.all_file_ext)
        pprint.pprint(self.config)
    
    def read_config(self, config_file):
        with open(config_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print("Setting source dir path to {}".format(row[1]))
                    self.dir_path = row[1]
                    self.all_files = os.listdir(self.dir_path)
                    self.wif = row[2]
                    self.action = row[3]
                    
                else:
                    print(f'\t{self.action} {row[0]} files in the {row[1]} directory.')
                    if(os.path.isdir(row[1])==False):
                        print("creating as directory {} does not exists".format(row[1]))
                        os.makedirs(row[1])
                        self.config[row[0]]=row[1]

                line_count += 1
                self.config[row[0]]=row[1]
            print(f'Processed {line_count} lines.')

    # This function will populate and increase the count of 
    # file extention in dictionary. 
    def populate_all_file_ext(self,file_type):
        if file_type in self.all_file_ext :
            self.all_file_ext[file_type] += 1
        else:
            self.all_file_ext[file_type] = 1

    
    def move_files(self,source,destination):
        # Code for moving file from one folder to another
        try:
            if self.wif == 'True' :
                
                print("Wif: Moving file from {} to {} ".format(source, destination))
            else:

                print("Real: Moving file from {} to {} ".format(source, destination))
                if(self.action == "Copy"):
                    shutil.copy(source, destination)
                else:
                    shutil.move(source, destination)
                
        except Exception as e:
            print("Printing Exception Message : {}".format(e))

    def dir_clean_up(self):

        # Loop through all files and their filetype. 
        for f in self.all_files:
            abs_path = os.path.join(self.dir_path, f)
            if (os.path.isfile(abs_path)):
               
                try:
                    self.populate_all_file_ext(f.split(".")[-1])
                    if f.split(".")[-1] in self.config:
                        self.move_files(abs_path,self.config[f.split(".")[-1]])
                    else:
                        print("file {} and/or type {} has no instruction in config file, skipping...".format(f,f.split(".")[-1]))
                                       
                except Exception as e:
                    print(e)
            else:
                print("Directory Name: {}  {}".format(abs_path, os.path.isfile(abs_path)))
                print("Directory {} has no instruction in config file, skipping...".format(f))
    # End def move_files. 



x = DirCleanUp("config.txt")
x.show_file_ext()
x.dir_clean_up()

