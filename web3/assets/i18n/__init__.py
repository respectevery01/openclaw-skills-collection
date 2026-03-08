import json
import os
from pathlib import Path

I18N_DIR = Path(__file__).parent

DEFAULT_LANG = 'en_us'
SUPPORTED_LANGS = ['en_us', 'zh_cn', 'jp', 'zh_tw']

def get_translation(lang=None):
    """
    Get translation dictionary for specified language
    Args:
        lang: Language code (en_us, zh_cn, jp, zh_tw). If None, uses DEFAULT_LANG
    Returns:
        Translation dictionary
    """
    if lang is None:
        lang = os.getenv('LANG', DEFAULT_LANG)
    
    if lang not in SUPPORTED_LANGS:
        lang = DEFAULT_LANG
    
    translation_file = I18N_DIR / f'{lang}.json'
    
    if not translation_file.exists():
        lang = DEFAULT_LANG
        translation_file = I18N_DIR / f'{lang}.json'
    
    try:
        with open(translation_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def t(key_path, lang=None):
    """
    Get translation value by key path (e.g., 'token_query.title')
    Args:
        key_path: Dot-separated key path
        lang: Language code (optional)
    Returns:
        Translation value or key_path if not found
    """
    translations = get_translation(lang)
    
    keys = key_path.split('.')
    value = translations
    
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return key_path
    
    return value

def get_chain_name(chain_key, lang=None):
    """
    Get localized chain name
    Args:
        chain_key: Chain key (e.g., 'ethereum', 'bsc')
        lang: Language code (optional)
    Returns:
        Localized chain name
    """
    return t(f'chains.{chain_key}', lang)
