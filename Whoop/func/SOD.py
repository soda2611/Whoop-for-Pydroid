try:
    from necessary_function import spelling_checker_for_SOD, check_connection, data as word_data
except:
    from func.necessary_function import spelling_checker_for_SOD, check_connection, data as word_data
from googletrans import Translator
import re

translator=Translator()

def SOD_word_list(path="data/tu_dien_nguon.txt", sub_path="func/data/tu_dien_nguon.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        with open(sub_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

    tu_dien = {}
    for line in lines:
        word, wordtype, definition, translation, synonyms, level = line.strip().split(" % ")
        temp={"word": word, "type": wordtype, "definition": definition, "translation": translation, "level": level}
        if synonyms!="none":
            temp["synonyms"]=synonyms.split(", ")
        else:
            temp["synonyms"]=synonyms
        tu_dien[word] = temp
    
    return tu_dien

source={}
for i in SOD_word_list():
    source[i.lower()]=i

def SOD(inp, internet_required=True, boost_performance=False, tu_dien=SOD_word_list(), word=word_data()):
    inp = inp.lower()
    result=[]
    if not boost_performance and (internet_required and check_connection()):
        if translator.detect(inp).lang == "vi": inp = translator.translate(text=inp, src='vi').text.lower()
        else: inp = spelling_checker_for_SOD(" ".join(inp.split()), word=word)
    elif boost_performance or not internet_required: inp = spelling_checker_for_SOD(" ".join(inp.split()))
    inp=word_detector(inp)
    for i in inp:
        try:
            if tu_dien[source[i]] not in result:
                result.append(tu_dien[source[i]])
        except:
            pass
    if result!=[]:
        return result
    return "Không tìm thấy từ"

def grammar_structure_detector(inp,file_path):
    patterns=build_patterns(file_path)
    result=[]
    for i in patterns:
        if len(re.findall(patterns[i], inp))!=0:
            result.append(i.replace("\n",""))
    return result

def build_patterns(file_path):
    patterns = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts,structure = line.split(": ")
            parts=parts.split('...')
            pattern = '\s*.*?'.join(f'({part.strip()})' for part in parts)
            patterns[structure] = pattern
    return patterns

def word_detector(inp):
    inp = inp.split()
    list_ = []
    i = 0
    while i < len(inp):
        max_len_phrase = inp[i]
        for j in range(i, len(inp)):
            phrase = " ".join(inp[i:j+1])
            if phrase in source:
                if len(phrase) > len(max_len_phrase):
                    max_len_phrase = phrase
        if max_len_phrase not in list_:
            list_.append(max_len_phrase)
        i += len(max_len_phrase.split())
    return list_

if __name__=="__main__":
    print(SOD("art art art art art art art", boost_performance=True))

    