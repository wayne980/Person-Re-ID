#中文分词处理
#下载地址: https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
#采用结巴分词进行处理，此版本未进行简繁体转换，以及特殊字符处理

# -*- coding: utf-8 -*-
 
from gensim.corpora import WikiCorpus
import jieba
from langconv import *
 
_author__ = 'Lust'
 
# read the wiki.xml.bz2
# transform it to simplified Chinese (use langconv)
# Chinese text segmentation(use jieba)
# save it as txt
 
 
def my_function():
    space = " "
    i = 0
    l = []
    a = '..//data//zhwiki-latest-pages-articles.xml.bz2'
    f = open('..//data//reduce_zhiwiki.txt', 'w')
    wiki = WikiCorpus(a, lemmatize=False, dictionary={})
    # texts = wiki.get_texts()
    for text in wiki.get_texts():
        for temp_sentence in text:
            temp_sentence = Converter('zh-hans').convert(temp_sentence.decode('utf-8'))
            temp_sentence = temp_sentence.encode('utf-8')
            seg_list = list(jieba.cut(temp_sentence))
            # for temp_term in temp_sentence:
            for temp_term in seg_list:
                l.append(temp_term.encode('utf-8'))
        f.write(space.join(l) + "\n")
        l = []
        i = i + 1
        print "Saved " + str(i) + " articles"
        # limit number of wikis
        if (i == 100):
            break
    f.close()
 
if __name__ == '__main__':
    my_function()
