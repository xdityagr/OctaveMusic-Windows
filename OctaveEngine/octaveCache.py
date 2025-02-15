
import enum
import pickle
import random
import time
import asyncio, aiohttp

from urllib.response import addinfo
import types


import re
import json
from json import JSONDecodeError
from typing import List, Dict
import sys, os
from datetime import datetime

from enum import Enum, auto

from click import DateTime

import pick
from ai_utils import *
import time


# from definitions import StreamMediaObject, OctaveStreamAudioQuality, OctaveStreamSupportedCodec
class KnownCacheSubTypes(Enum):
    INT = int()
    STR = str()
    LIST = list()
    DICT = dict()

class KnownCacheTypes(Enum):
    PERMANENT = 'PERMANENT'
    SESSION = 'SESSION'
    EXPIRY = 'EXPIRY'

class ExpireTime:
    def __init__(self):
        self.time = None

    def auto(self):
        self.time = datetime.now()
        return self.time
    
    def __str__(self):# -> Any:
        return datetime.strftime(self.time)
    
    def expiresIn(self, time):
        time = datetime.strptime(time)
        if time:
            time_left = datetime.now() - self.time 
            return time_left



class Cache:
    def __init__(self, **kwargs):  
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.sub_type = kwargs.get('sub_type', None)
        self.additional_info = {}
        if self.type == KnownCacheTypes.EXPIRY:
            expires_after = kwargs.get('expires_after', None)
            self.additional_info['expires_after'] =  expires_after
        print(self.additional_info)
        
        self.path = f'.{self.name}.json' if self.name else None
            
    def __repr__(self):
        return f"CacheType -> name={self.name}, type={self.type}, sub_type={self.sub_type}, path={self.path}"
        
class CacheTypes(list):
    def __init__(self, *args, callback=None):
        super().__init__(*args)
        self._callback = callback  

    def append(self, **kwargs):
        print(kwargs)
        item = Cache(**kwargs)
        super().append(item)  

        if self._callback:
            self._callback(item)  

    def extend(self, iterable):
        new_iterable = [Cache(**kwargs) for kwargs in iterable]

        super().extend(new_iterable)
        if self._callback:
            for i in new_iterable:
                self._callback(i)  

    def insert(self, **kwargs):
        
        new_item = item = Cache(**kwargs)

        super().insert(kwargs.get('index', -1), new_item)
        if self._callback:
            self._callback(new_item) 



class OctaveCache:
    def __init__(self):
        self.CACHEPATH = 'OctaveEngine/cache/'
        self.CACHEINFOPATH = 'OctaveEngine/cache/cacheinfo'
        self.KNOWN_CACHES = CacheTypes(callback=self._update_cache_types)
        for i in self.KNOWN_CACHES: self._register(i)
        # self.KNOWN_CACHE_TYPES.append('results_cache', d)
    
    def _update_cache_types(self, item):
        print(f'Cache types updated with {item}')
        # print(item.name, item.type, item.sub_type,item.path)
        # self._register(item)
        self._create_cache_file(item)

        
    def _register(self, cacheObject):
        data = None
        if os.path.exists(self.CACHEINFOPATH):
            with open(self.CACHEINFOPATH, 'rb') as f1:
                data = pickle.load(f1)
                data = data['cacheinfo']
        else:
            tmpl = {'cacheinfo':[]}
            with open(self.CACHEINFOPATH, 'wb') as f2:
                pickle.dump(tmpl, f2)
    
            data = tmpl['cacheinfo']
        
        if data is not None:
            
            ids, id, name = [], cacheObject.cache_id, cacheObject.name
            for object in data: ids.append(object[0])
            if id not in ids: 
                data.append((id, name))

                with open(self.CACHEINFOPATH, 'wb') as f3:
                    pickle.dump({'cacheids':data}, f3)
                
                self._create_cache_file(cacheObject)


    def _create_cache_file(self, cache_type):
        name, type, sub_type, fpath, addn_info = cache_type.name, cache_type.type, cache_type.sub_type, cache_type.path, cache_type.additional_info
        # expires_after = addn_info.get('expires_after', None) 
        
        cache_templ = {name:sub_type.value, 'type':(f'{type.value}', addn_info), 'subtype':sub_type.name}
        print(cache_templ)
        fpath = os.path.join(self.CACHEPATH, fpath)
        try:
            if os.path.exists(fpath): os.remove(fpath)

            with open(fpath, 'w') as f: pass
            with open(fpath, 'w') as f2: 
                json.dump(cache_templ, f2, indent=4)
        except JSONDecodeError as e:
            print(f'Octave Cache Error : {e}')

    def add_to_cache(self, cache_name, item):
        self.KNOWN_CACHES 
        pass


             
# USAGE :
c = OctaveCache()
c.KNOWN_CACHES.append(name='results_cache', type=KnownCacheTypes.EXPIRY, expires_after = str(ExpireTime().auto()), sub_type=KnownCacheSubTypes.LIST)          
# print(c.KNOWN_CACHES[0].sub_type)




# print(get_id())
# c.KNOWN_CACHES.extend([{'name':'hih', 'sub_type':KnownCacheSubTypes.LIST, 'type':KnownCacheTypes.PERMANENT},])







