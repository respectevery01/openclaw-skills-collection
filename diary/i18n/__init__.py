#!/usr/bin/env python3
"""
Multi-language management module
Supports module-based i18n loading (common, qweather, amap, etc.)
"""

import json
import os

class I18nManager:
    def __init__(self, lang='zh_cn'):
        self.lang = lang
        self.translations = {}
        self._modules = ['common', 'qweather', 'amap', 'mastodon']
        self._load_all_translations()
    
    def _load_all_translations(self):
        """Load all translation files including module-specific ones"""
        i18n_dir = os.path.dirname(os.path.abspath(__file__))
        
        supported_langs = ['zh_cn', 'en_us', 'zh_tw', 'jp']
        
        for lang in supported_langs:
            self.translations[lang] = {}
            
            for module in self._modules:
                module_dir = os.path.join(i18n_dir, module)
                file_path = os.path.join(module_dir, f'{lang}.json')
                
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        module_data = json.load(f)
                        # Deep merge module data into translations
                        self._deep_merge(self.translations[lang], module_data)
    
    def _deep_merge(self, base_dict, new_dict):
        """Deep merge two dictionaries"""
        for key, value in new_dict.items():
            if key in base_dict:
                # If both values are dictionaries, merge them
                if isinstance(value, dict) and isinstance(base_dict[key], dict):
                    self._deep_merge(base_dict[key], value)
                else:
                    # Otherwise, overwrite with new value
                    base_dict[key] = value
            else:
                # Key doesn't exist, add it
                base_dict[key] = value
    
    def set_language(self, lang):
        """Set language"""
        if lang in self.translations:
            self.lang = lang
            return True
        return False
    
    def get(self, key, **kwargs):
        """Get translation"""
        try:
            keys = key.split('.')
            translation = self.translations[self.lang]
            
            for k in keys:
                translation = translation[k]
            
            if kwargs:
                return translation.format(**kwargs)
            
            return translation
        except (KeyError, AttributeError):
            return key
    
    def get_supported_languages(self):
        """Get supported languages list"""
        return list(self.translations.keys())


i18n = I18nManager()


def set_language(lang):
    """Set current language"""
    return i18n.set_language(lang)


def get(key, **kwargs):
    """Get translation by key"""
    return i18n.get(key, **kwargs)


def gettext(key):
    """Alias for get() for backward compatibility"""
    return i18n.get(key)


_ = gettext


def get_module_i18n(module_name: str, lang: str = None):
    """Get i18n data for a specific module"""
    i18n_dir = os.path.dirname(os.path.abspath(__file__))
    target_lang = lang or i18n.lang
    
    file_path = os.path.join(i18n_dir, module_name, f'{target_lang}.json')
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {}


if __name__ == "__main__":
    i18n.set_language('zh_cn')
    print(i18n.get('weather.title'))
    print(i18n.get('common.query_location', name='北京', id='101010100'))
    print(i18n.get('amap.cli_tool'))


SUPPORTED_LANGS = ['zh_cn', 'en_us', 'zh_tw', 'jp']
t = get
