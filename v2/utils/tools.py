import re

def check_if_date(string):
    t1 = re.match(r'(\d+.\d+.\d+ \d+:\d+)',string)
    t2 = re.match(r'(\d+:\d+ \d+.\d+.\d+)',string)
    if t1 or t2:
        return True
    return False

def clean_L1(data):
    return data.strip().split('\n')

def clean(obj):
    replacement = ['Voir la traduction', ' (فيديو)', " J’aime"," Haha", " Grrr", " J’adore", " Wouah",' (صور)', ' commentaires', ' partages']
    for rep in replacement:
              obj = obj.replace(rep,'')

    return obj


