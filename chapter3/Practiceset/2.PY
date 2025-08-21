Letter ='''
         Dear <|Name|>
         You are selected
         <|Date|>
         '''

print(Letter.replace("<|Name|>","NIKHIL").replace("<|Date|>","1 JUNE 2007"))