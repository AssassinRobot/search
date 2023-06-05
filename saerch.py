def Searchs(genre,search):
    if genre=='action':
        genre=saction
        print(genre)
    elif genre=='scary':
        genre=sscary
        print(genre)  
    elif genre=='dram':
        genre=sdram 
        print(genre)
    elif genre=='romantic':
        genre=sdram   
        print(genre)         
    if search in genre :
      index = genre.index(search)
      Movie=genre[index]
      print(f"Search resulte:{Movie}")
    else :
        print('Name not found')
def Searchm(genre,search):
    if genre=='action':
        genre=maction
        print(genre)
    elif genre=='scary':
        genre=mscary
        print(genre)  
    elif genre=='dram':
        genre=mdram 
        print(genre)
    elif genre=='romantic':
        genre=mromantic  
        print(genre)         
    if search in genre :
      index = genre.index(search)
      Movie=genre[index]
      print(f"Search resulte:{Movie}")
    else :
        print('Name not found')        
series =["a teacher ",'lupin','Channel Zero','masters of horror','loki','ozark','the o.c',"war and peace"] 
saction=series[0:2]
sscary=series[2:4]
sdram=series[4:6]
sromantic=series[6:8]
Movies = ['musel','snaiper','anabel','it','city of gods','parasite',"jj+e","life in a year"]
maction=Movies[0:2]
mscary=Movies[2:4]
mdram =Movies[4:6]
mromantic=Movies[6:8]
Question = input('Series or Movies :')
if Question == "Movies":
    resulte_genrem= input('Enter your desired genre :')
    resulte_searchm= input('Enter your desired movie :')
    Searchm(resulte_genrem,resulte_searchm)
elif Question == 'Series':
    resulte_genres= input('Enter your desired genre :')
    resulte_searchs= input('Enter your desired movie :')
    Searchs(resulte_genres,resulte_searchs)







    

