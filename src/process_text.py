import re

    
def clean_text(un_processed):
    #strr = "Global warming is the ongoing rise of the average temperature of the Earth's climate system and has been demonstrated by direct temperature measurements and by measurements of various effects of the warming.[1] It is a major aspect of climate change which, in addition to rising global surface temperatures,[2] also includes its effects, such as changes in precipitation.[3] While there have been prehistoric periods of global warming,[4] observed changes since the mid-20th century have been unprecedented in rate and scale.[5] "
    
    for i in range(len(un_processed)):
        un_processed = re.sub(r"\W"," ",un_processed)
        un_processed = re.sub(r"\d"," ",un_processed)
        un_processed = re.sub(r"\s+[a-z]\s+"," ",un_processed,flags=re.I)
        un_processed = re.sub(r"\s+"," ",un_processed)
        un_processed = re.sub(r"^\s","",un_processed)
        un_processed = re.sub(r"\s$","",un_processed)
        
        
    return un_processed



