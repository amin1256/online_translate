sentences = input("type your sentences : ")
sentences = sentences.split()


farsi = dict()
farsi["hello"] = "salam"
farsi["bye"] = "khodafez"
farsi["we"] = "ma"

english_list = list(farsi.keys())
answer_list = list(farsi.values())

farsi1 = farsi.get(sentences[0] , sentences[0])   
farsi2 = farsi.get(sentences[1] , sentences[1])  
farsi3 = farsi.get(sentences[2] , sentences[2])  

finish = farsi1 + " " + farsi2 + " " + farsi3
print(finish)