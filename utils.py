from re import sub
from sre_parse import SubPattern
from colorama import Fore
from OctaveEngine.definitions import OctaveStreamAudioQuality
from main import app_options

import os, json
from json import JSONDecodeError
import difflib

def warn(context, title=None, message=None):
    print(Fore.YELLOW + f"{context} [{title}] : " + Fore.WHITE + f"{message}" + Fore.RESET)

def error(title, traceback=None, message=None):
    print(Fore.RED + f"Error : {title}, from {traceback if traceback else ''} : " + Fore.WHITE + f"{message}" + Fore.RESET)





class OctaveSettings:
    """
    Octave/ConfigX Setttings : Keypath resolved settings manager, easy to use, easy to code with. 
    How does it work? : 
        Well, It works on a keypath based approach.
        Keypath? -> It is a path, separated by '.' of a key in a dictionary. 
            for example;
              data = {'user':{'age':{'value':19, 'isAdult':True}, 'name':'Aditya'}}
              # then the keypath of 'isAdult' will be : 'user.age.isAdult'

        Simply use the resolve method, and you can access info, update it, by just he keypath. 
        -> *this is helpful in a huge settings file, or key:value based data in json, etc.
         
    Usage: 
        Ocs = OctaveSettings()
        Ocs.resolve('app.data.theme') -> will give the value of 'theme'
        >>> 'amoled'
        Ocs.resolve('app.data.theme=Light') -> will change the value of 'theme'
        >>> 'Light'

    Future Additions : 
        1. Datatype management via Schema
        2. Backup/restore settings, or keypaths like: backup('app.playback*')
        3. fetch all from a keypath, like:  resolve('app.playback*') -> gives all the associated subparents, keys, values
        4. Version control for keypaths, like : revert('playback.volume') -> 100 | history('playback.volume') -> 99, 100, 50, 60, 90
        5. Add observers to keypaths & callbacks on value change, like : 
            def on_theme_change(new_value):
                print(f"Theme changed to: {new_value}")
        
            Ocs.add_observer('appearance.theme', on_theme_change)
            Ocs.resolve('appearance.theme=dark')  # Automatically triggers on_theme_change
        
        6. Keypath autocompletion when using CLI
        7. Auto Encryption/Decryption when accessing sensitive setting
        8. Import/Export/Merge settings 
        9. Lazy loading for huge files
        10. Become a mini-dbms. 


    """
    def __init__(self):
        self.DEFAULTS = {'appearance':
                         {'theme':'amoled', 'background':None, 'accent_color':'#fff'}, 
                         'playback':
                         {'quality':OctaveStreamAudioQuality.STANDARD.value, 
                          'crossfade':True, 
                          'crossfade.duration':5, 
                          'queue.remember':True,
                          'queue.repeat_mode':'off', 
                          'queue.shuffle':True, 
                          'queue.resume_on_startup':False,
                          'lyrics.enabled':True,
                          'lyrics.look_online':True, 
                          'lyrics.sync_enabled':False,
                          'speed':1.0,
                          'volume':100,
                          'sleep_timer.enabled':False,
                          'sleep_timer.time':30,
                          'notifications.enabled':False
                          },

                        'notifications':{'enabled':True},
                        'library':
                        {
                        'scan_directories':[],
                        'blacklisted_directories':[],
                        'fetch_metadata':True
                        }
                         }
        self.debug = app_options.get('debug', False)
        self.SETTINGS_PATH = self.__get_settings_path()
        
        
        self.settings =self.load_settings()
        self.known_key_paths = self._get_keypaths(self.DEFAULTS)
        print(self.known_key_paths)
        
        

    def _get_keypaths(self, dct, parent_key=""):
        keypaths = set()
        for key, value in dct.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keypaths.add(full_key)
            if isinstance(value, dict):
                keypaths.update(self._get_keypaths(value, full_key))

        return keypaths

    def load_settings(self):
        self.__verify_settings_file()
        try:
            with open(self.SETTINGS_PATH, 'r') as st:
                settings = json.load(st)
            if self.debug:
                warn('Load Settings', 'OctaveSetings','Settings loaded into memory successfully.')
            return settings
        except JSONDecodeError as e:
            self.settings = None
            error(title='OctaveSettings', traceback=f'JSONDecodeError when loading settings.', message=f"{e}")

    def update_settings(self):
        try:
            with open(self.SETTINGS_PATH, 'w') as updated: 
                json.dump(self.settings, updated, indent=4)

            with open(self.SETTINGS_PATH, 'r') as new:
                self.settings = json.load(new)

            if self.debug:
                warn('Load Settings', 'OctaveSetings','Settings updated & loaded into memory successfully.')

        except Exception as e:
            self.settings = None
            error(title='OctaveSettings', traceback=f'Error when updating settings.', message=f"{e}")


    
    def resolve(self, setting:str):
        c, operation,parent, sub_parent, key, value = self.__parse_setting_from_string(setting)


        if c != -1:
            key_path = '.'.join(filter(None, [parent, sub_parent, key]))
            
            if key_path not in self.known_key_paths:
                if self.debug:
                    similar = []
                    max_results = 5
                    if len(similar) < max_results:
                        remaining_keypaths = [k for k in self.known_key_paths if k not in similar]
                        closest_matches = difflib.get_close_matches(setting, remaining_keypaths, n=max_results - len(similar))
                        similar.extend(closest_matches)

                    error(title='OctaveSettings', traceback=f'parse({setting})', message=f"Parsable Setting '{setting}' contains invalid keypath. {chr(10)}Did you mean? : {chr(10)}"+ Fore.YELLOW + f"{chr(10).join(similar)}" + Fore.RESET)
                return -1
        
            else:
                if sub_parent:
                    try:

                        fetched = self.settings[parent][f'{sub_parent}.{key}']
                    except KeyError:
                        error(title='OctaveSettings', traceback=f'parse({setting}): Key Error', message=f"Parsable Setting '{setting}' contains invalid keypath.")                    
                        return -1
                else:
                    try:
                        fetched = self.settings[parent][key]
                    except KeyError:
                        error(title='OctaveSettings', traceback=f'parse({setting}): Key Error', message=f"Parsable Setting '{setting}' contains invalid keypath.")                    
                        return -1
                
                if operation==1:
                    if sub_parent:
                        self.settings[parent][f'{sub_parent}.{key}'] = value
                    else:
                        self.settings[parent][key] = value
                
                    if self.debug:
                        warn(title='OctaveSettings', context=f'parse({setting})', message=f"Parsable Setting '{setting}' has been updated with key={key}, value={value}")

                    self.update_settings()
                else:
                    return fetched
            

    def __verify_settings_file(self):
        if not os.path.exists(self.SETTINGS_PATH):
            try: 
                with open(self.SETTINGS_PATH, 'w') as fl: pass

                with open(self.SETTINGS_PATH, 'w') as fl2: 
                    json.dump(self.DEFAULTS, fl2, indent=4)

                if self.debug:
                    warn('Verification', 'OctaveSettings', 'Settings file did not exist, Created new with defaults.')
            except Exception as e:
                error('Verify Settings File', 'Settings file did not exist, error encountered at creating the file again ',f'{e}')

    def __purge(self):
        os.remove(self.SETTINGS_PATH)


    def __get_settings_path(self):
        if os.name == 'nt':  # Windows
            base_dir = os.getenv('APPDATA')
        elif os.name == 'posix':  # macOS/Linux
            base_dir = os.path.expanduser('~/.config')
        else:
            raise Exception("Unsupported OS")

        settings_dir = os.path.join(base_dir, 'OctaveMusic')

        os.makedirs(settings_dir, exist_ok=True)
        
        return os.path.join(settings_dir, 'settings.json')
    
    
    def __parse_setting_from_string(self, settingString):
        key = settingString.lower()
        
        if '.' not in key and '=' not in key: 
            return -1, None, None, None, None
        
        key = key.split('.')

        parameter_parent = key[0]
        parameter_sub_parent = key[1] if len(key)>2 else None
        parameter = None
        parameter_value = None
        operation = None

        for subkey in key:
            if '=' in subkey: 
                operation = 1
                split = subkey.split('=')
                parameter =split[0]
                parameter_value = split[1] if split[1] !='' else None
            else:
                operation =0
                parameter = key[-1]
        
        parameter_value = str(parameter_value)

        if parameter_value.isdigit(): 
            parameter_value = int(parameter_value)
        try :
            parameter_value = float(parameter_value)
        except ValueError:
            if parameter_value.lower() in ['true', 'false']:
                parameter_value = parameter_value.lower() == 'true'
            elif parameter_value.lower() == 'none':
                parameter_value = None

        # if parameter_parent in self.known_parents and parameter_sub_parent in self.known_sub_parents and 
        # print(parameter_parent, parameter_sub_parent, parameter, parameter_value)
        return 0, operation, parameter_parent, parameter_sub_parent, parameter, parameter_value





ocs = OctaveSettings()
ocs.resolve("playback.q.sh")