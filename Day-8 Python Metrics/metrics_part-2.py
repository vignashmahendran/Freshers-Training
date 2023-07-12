from nltk.metrics import edit_distance
from nltk.translate.bleu_score import sentence_bleu 
predictions=["I","have","thirty","six","years","old"]
references=[["I","am","thirty","six","years","old"],["I","am","thirty","six"]]
print(f" BLEU Score 1-gram : { sentence_bleu(references,predictions,weights=(1,0,0,0))}")
print(f" BLEU Score 2-gram : { sentence_bleu(references,predictions,weights=(0,1,0,0))}")
print(f" BLEU Score 3-gram : { sentence_bleu(references,predictions,weights=(0,0,1,0))}")
print(f" BLEU Score 4-gram : { sentence_bleu(references,predictions,weights=(0,0,0,1))}")
gtvalue='this is a cat'
predvalue='this is a dog'
print(f"Character error : {edit_distance(gtvalue,predvalue)/len(gtvalue)}")
print(f"Word error : {edit_distance(gtvalue.split(),predvalue.split())/len(gtvalue)}")



