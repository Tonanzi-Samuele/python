import datetime

def calcolo(anno):
    anno_att = datetime.datetime.now().year
    eta = anno_att - anno
     
    print(f"età = {eta}")
def main():

    annonascita = int(input("inserire anno di nascita: "))
    
    calcolo(annonascita)
main()
    