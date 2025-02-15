import os, json
from json import JSONDecodeError

class ExtMetadata:
    def __init__(self):
        self.match  = None
        self.external_metadata_path = os.path.join(os.getcwd(), "OctaveEngine/Data/external_metadata.json")        
        self.current_metadata = self.load_external_metadata()
        
    def getMetadatafromData(self, data):
        if self.current_metadata['mediaData'] != []:
            for i, element in enumerate(self.current_metadata['mediaData']):
                if element['title'] == data.title and element['fpath'] == data.filePath and element['artist'] == data.artist:
                    self.match = (i, element)
                else:
                    self.match = None
                    self.commit_external_metadata(data)
        else:
            self.commit_external_metadata(data)

        return self.match
        
    def load_external_metadata(self):
        obj = None
        if os.path.exists(self.external_metadata_path):
            try:
                with open(self.external_metadata_path, "r") as f:
                    obj = json.load(f)
                
                return obj
            except JSONDecodeError as e:
                os.remove(self.external_metadata_path)
                self.create_external_metadata()
                self.load_external_metadata()
        else:
            self.create_external_metadata()
            self.load_external_metadata()

    def commit_external_metadata(self, data):
        if self.match == None:
            self.current_metadata['mediaData'].append({'title':data.title, 'fpath':data.filePath, 'artist':data.artist, 'isLiked':data.isLiked})
        else:
            self.current_metadata['mediaData'][self.match[0]]['isLiked'] = data.isLiked

        with open(self.external_metadata_path, "w") as jb:
            json.dump(self.current_metadata, jb, indent=4)

    def change_metadata(self, new):
        if self.current_metadata['mediaData'] != []:
            for i, element in enumerate(self.current_metadata['mediaData']):
                if element['title'] == new.title and element['fpath'] == new.filePath and element['artist'] == new.artist:
                    self.match = (i, element)
                else:
                    self.match = None
        
        self.match['isLiked'] = new.isLiked
        self.commit_external_metadata()
        
    def create_external_metadata(self):
        with open(self.external_metadata_path, "w") as j:
            temp= {"mediaData" : []}
            json.dump(temp, j, indent=4)