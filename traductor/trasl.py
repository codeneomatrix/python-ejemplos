from urllib import urlencode
from urllib2 import urlopen, Request
import re
import json
import codecs
import os
import sys

	#programa creado por josue acevedo maldonado (Neomatrix)  11:ago:2014

def get_google_translate (text, translate_lang, source_lang=None):
    if source_lang == None:
        source_lang= 'auto'
    params = urlencode({'client':'t', 'tl':translate_lang, 'q':text.encode('utf-8'),
                       'sl':source_lang})
    http_headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}
    request_object = Request('http://translate.google.com/translate_a/t?'+params,
                     None, http_headers)
    try:
        response = urlopen(request_object)
        string = re.sub(',,,|,,',',"0",', response.read())
        n = json.loads(string)
        translate_text = n[0][0][0]
        res_source_lang = n[2]
        return True, res_source_lang, translate_text.encode('utf-8'),
    except Exception, e:
        return False, '', text


def main():

    ar = raw_input("URL:")
    
    sal = ""
    con = 0
    print(os.name)


    f = open(ar, "r")



    nombre=f.name[0:-4:]
    nn=''
    nn=nombre+'-tras.srt'


    fin = codecs.open(nn, "w")


    for line in f:

        if line == "\r\n":
            fin.write("\n")

        if '-->' in line:
            print line
            fin.write(line)

        if len(line) <= 5:
            print line
            fin.write(line)

        if (len(line) > 5):
            if (line.find('-->') == -1):
                result, code, text = get_google_translate(line, 'es')
                print text
                fin.write(text+"\n")



    print(sal)

    fin.close()
    f.close()
    

if __name__ == "__main__":main()