class TW:
    def __init__(self):
        self.tweetID = 0
        self.message = ""
        self.date = datetime.datetime.now()
        self.originalMessage=""
        self.category = 0
        self.score = 0
        self.backupMessage=""
        self.sScore=0
        self.sState="Nötr"
    def splitID(self,text):
        self.tweetID = int(text[4:23])
        self.message = text.split("->")[1]
        
       
    def splitDate(self,text):
        
        splited = text.split(" ")
        day = int(splited[2])
        timeString = splited[3].split(":")
        hour = int(timeString[0])
        minute = int(timeString[1])
        second  = int(timeString[2])
        self.date = datetime.datetime(year=2020,month=1,day=day,hour=hour,minute=minute,second=second)
    def remove_emoji(self,text):
        return emoji.get_emoji_regexp().sub(u'', text)    
    def cleanUp(self):         
        self.originalMessage = self.message
        rawS = self.message.split(" ")
        last = ""
        for i in rawS:
            if i.startswith("@") or "http://" in i or  "https://" in i or i.startswith("\n") or "#" in i:
                continue
            else:
                
                last+=stemmer.stem(i)+" "
               
                
        self.message = self.remove_emoji(sonHali.replace("\n", " "))
        self.message = self.message.replace("#", " ")
        self.cleanMore()
    def cleanMore(self):
        charList = " ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQXabcçdefgğhıijklmnoöprsştuüvyzqx0123456789"
        temp=""
        
        for i in self.message:
            if i in charList:
                temp+=i
            else:
                temp+=" "
        self.message = re.sub(' +', ' ', temp.lower().strip())
        #self.message=temp
        print("----")
        print("Edited : "+self.message)
        print("Original : "+self.originalMessage)
        print("---")
