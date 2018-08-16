#繁体转简体：使用的是开源简繁转换工具OpenCC
#字符编码转换：使用iconv命令将文件转换成utf-8编码

iconv -c -t UTF-8 < input_file > output_file
#iconv -c -t UTF-8 input_file -o output_file

#分词处理：使用jieba分词工具包，命令行分词

python -m jieba input_file > cut_file

# Traditional Chinese to Simplified Chinese
echo "opencc: Traditional Chinese to Simplified Chinese..."
#time opencc -i wiki.zh.txt -o wiki.zh.chs.txt -c zht2zhs.ini
time opencc -i wiki.zh.txt -o wiki.zh.chs.txt -c t2s.json

# Cut words
echo "jieba: Cut words..."
time python -m jieba -d ' ' wiki.zh.chs.txt > wiki.zh.seg.txt

# Change encode
echo "iconv: ascii to utf-8..."
time iconv -c -t UTF-8 < wiki.zh.seg.txt > wiki.zh.seg.utf.txt

process_wiki_2.sh
