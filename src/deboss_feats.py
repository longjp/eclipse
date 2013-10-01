########## 
########## 
########## OUTPUT data/new_debosscher .xml files in tfe format
########## estimate periods for each curve
##########
########## by James Long 
########## date: SEPTEMBER 30, 2013
########## 


import glob
import xml_manip



def read_xml(filename):
    print "hello"


if __name__ == "__main__":
    folder = "../data/new_debosscher/"
    extension = ".xml"
    filepaths = glob.glob(("%s/*" + extension) % (folder))
    print filepaths
    info = xml_manip.get_info(filepaths[0])
    print info
