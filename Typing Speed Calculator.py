import time
str1="don't trouble the trouble, if you trouble the trouble, trouble trobles you, i am not the trouble i am the truth"
str2="Nuvvu naa pakkana unnantha varaku nannu champe magadu inka puttaledu mama!"
str3="history tells us, powerful people come from powerful places but history was wrong, powerful people make places powerful "
str4="okkokadini kadhu sher khan, vanda mandini okesari rammanu... lekka ekkuva ayina parvaledhu takkuva kaakunda choosko"
str5="aapesi odipoyina vadu unnadu kani, prayathnisthu odipoyina vadu ledu. Maa nanna praythnisthu chanipoledhu, Chanipothadani thelisi kuda praythnimchadu"
str6="manaki emaina effect aythe, manam pothe, the most effected person okkaruntaru. adhi na life lo ah pilla. ahh pilla ki emanna aythe, i'll be the most effected understand! "
str7="Evadu kodithe dimma thirigi mind block aypothado… aade pandugadu"
str8="Naakoncham tikkundi, kaani daaniko lekkundi. Ah tikkento chupistha, andari lekkalu telusthaa"
str9="After all cigerate packet meedhe nannu thagaddhu potharu ani cheppinappudu. Nalantodu nannu gelakaddhu chastharu ani cheppothe yela…"
str10="Balavanthudu balaheenudini bhayapetti brathakadam aanavaayithi ne, but for a change aa balaheenudi pakkana kuda oka balam undi, JANATHA GARAGE!"
s={str1,str2,str3,str4,str5,str6,str7,str8,str9,str10}
print("---------------------------typing speed test-----------------------------")
print("NOTE:1.Do not use backspace!!\n     2.Do not see the keyboard\n")
int(input(("Enter any key when you are ready:")))
while True:
    string=""
    print("\nenter the below given sentence")
    for e in s:
        string=e
        break
    print("Given sentence:",string)
    wordcount=len(string.split())
    t0=time.time()
    inputtext=str(input("your sentence:"))
    t1=time.time()
    accuracy=len(set(inputtext.split())&set(string.split()))
    accuracy=accuracy/wordcount*100
    timetaken=t1-t0
    wpm=wordcount/timetaken*60
    print("\nwpm={}\naccuracy={}\ntimetaken={}".format(wpm,accuracy,timetaken))
    n=int(input("\nEnter 0 to try again or Enter any other to exit:"))
    if(n!=0):
        print("\nthank you!!")
        break
    s.remove(string)