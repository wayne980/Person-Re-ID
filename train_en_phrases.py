#对短语进行训练词编码


from __future__ import print_function

import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.phrases import Phrases
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print("Useing: python train_word2vec_model.py input_text "
              "output_gensim_model output_word_vector")
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]
    sentence=LineSentence(inp)
    bigram_transformer= Phrases(sentence,min_count=1)
    
    model = Word2Vec(bigram_transformer[sentence], size=300, window=5, min_count=1,workers=multiprocessing.cpu_count()-1)
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)
