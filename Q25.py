
def make_ing_form(verb):

    vowels = 'aeiou'  
    
    if verb.endswith('ie'):
        return verb[:-2]+'ying'
    elif verb.endswith('e'):
        return verb[:-1]+'ing'
    elif verb[-3] not in vowels:
        if verb[-2] in vowels:
          if verb[-1] not in vowels:
            return verb+verb[-1]+'ing'
    else:
        return verb+'ing' 
    
if __name__ == '__main__':

   print (make_ing_form('lie'))
   print (make_ing_form('move'))
   print (make_ing_form('hug'))
   print (make_ing_form('touch'))