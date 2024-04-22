from typing import Union

class Settings:
    path: str
    name: str    

    def __init__(self, path: str, name: str):
        self.path = path
        self.name = name

class SettingsSingleton:    
    __instance: Union[None, Settings] = None

    @classmethod
    def instance(cls) -> Settings:
        if not cls.__instance:
            cls.__instance = Settings('default path', 'default name')

        return cls.__instance
