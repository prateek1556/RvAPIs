import re

    
def clean_text(un_processed):
    #strr = "Global warming is the ongoing rise of the average temperature of the Earth's climate system and has been demonstrated by direct temperature measurements and by measurements of various effects of the warming.[1] It is a major aspect of climate change which, in addition to rising global surface temperatures,[2] also includes its effects, such as changes in precipitation.[3] While there have been prehistoric periods of global warming,[4] observed changes since the mid-20th century have been unprecedented in rate and scale.[5] "
    
    for i in range(len(un_processed)):
        un_processed = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s", " ", un_processed)
        un_processed = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s", " ", un_processed)
        un_processed = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$", " ", un_processed)
        un_processed = un_processed.lower()
        un_processed = re.sub(r"that's","that is",un_processed)
        un_processed = re.sub(r"there's","there is",un_processed)
        un_processed = re.sub(r"what's","what is",un_processed)
        un_processed = re.sub(r"where's","where is",un_processed)
        un_processed = re.sub(r"it's","it is",un_processed)
        un_processed = re.sub(r"who's","who is",un_processed)
        un_processed = re.sub(r"i'm","i am",un_processed)
        un_processed = re.sub(r"she's","she is",un_processed)
        un_processed = re.sub(r"he's","he is",un_processed)
        un_processed = re.sub(r"they're","they are",un_processed)
        un_processed = re.sub(r"who're","who are",un_processed)
        un_processed = re.sub(r"ain't","am not",un_processed)
        un_processed = re.sub(r"wouldn't","would not",un_processed)
        un_processed = re.sub(r"shouldn't","should not",un_processed)
        un_processed = re.sub(r"can't","can not",un_processed)
        un_processed = re.sub(r"couldn't","could not",un_processed)
        un_processed = re.sub(r"won't","will not",un_processed)
        un_processed = re.sub(r"\W"," ",un_processed)
        un_processed = re.sub(r"\d"," ",un_processed)
        un_processed = re.sub(r"\s+[a-z]\s+"," ",un_processed)
        un_processed = re.sub(r"\s+[a-z]$"," ",un_processed)
        un_processed = re.sub(r"^[a-z]\s+"," ",un_processed)
        un_processed = re.sub(r"\s+"," ",un_processed)
        
        
    return un_processed



