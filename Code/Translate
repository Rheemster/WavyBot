TranslateToFullwidth = str.maketrans(
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~',
    '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［］＾＿‘｛｜｝～')

def fullwidth(s):
    return s.translate(TranslateToFullwidth)
    
def brokenTranslate(aestheticMessage):
	finalMessage = ""

	for i in range(len(aestheticMessage)):
		if not(i % 2 == 0):
			aestheticMessage[i] = fullwidth(aestheticMessage[i])
		
	for i in range(len(aestheticMessage)):
		finalMessage = finalMessage = aestheticMessage[i]
	
	return finalMessage
