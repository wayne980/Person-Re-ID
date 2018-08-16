#下载wiki百科英语语料库，并采用gensim进行处理
# 下载地址 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
#生成纯净的文本，每一行是一篇wiki百科文章
#python3 环境下运行，24线程全开，处理15G数据，大概一个小时

#使用命令 python3 process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.txt

from __future__ import print_function
import logging
import os.path
import six
import sys
from gensim.corpora import WikiCorpus
 
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
    if len(sys.argv) != 3:
        print("Using: python process_wiki.py enwiki.xxx.xml.bz2 wiki.en.text")
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0
 
    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        if six.PY3:
            output.write(b' '.join(text).decode('utf-8') + '\n')
        else:
            output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")
 
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
