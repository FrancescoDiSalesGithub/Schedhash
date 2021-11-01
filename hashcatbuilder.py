import json
import sys

class hashcat_builder:
    
    __json_data=""

    def __init__(self):
        
            hash_json = open("hash.json","r")
            self.__json_data=json.load(hash_json)
            hash_json.close()
           

    def show_category(self):
        automatic_index=0

        for i in self.__json_data['hash']:
            automatic_index+=1
            print( "{} - {}".format(str(automatic_index),str(i['category'])) )

    def show_actions(self):
        pass
            
        