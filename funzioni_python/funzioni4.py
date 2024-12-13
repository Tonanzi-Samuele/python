def ordine(e1,e2,e3):
    if e1 > e2 and e1 > e3:
        if e2 > e3:
            print(f"""
              - {e3}
              - {e2}
              - {e1} """)
        elif e3 > e2:
            print(f"""/
              - {e2}
              - {e3}
              - {e1} """)
    elif e2 > e1 and e2 > e3:
        if e1 > e3: 
             print(f"""/
              - {e3}
              - {e1}
              - {e2} """)
        if e3 > e1:
             print(f"""/
              - {e1}
              - {e3}
              - {e2} """)
    elif e3 > e1 and e3 > e2:
        if e1 > e2:
             print(f"""/
              - {e2}
              - {e1}
              - {e3} """)
        elif e2 > e1:
             print(f"""/
              - {e1}
              - {e2}
              - {e3} """)

def main():
    et1 = int(input("inserire età 1: "))
    et2 = int(input("inserire età 2: "))
    et3 = int(input("inserire età 3: "))

    ordine(et1, et2, et3)
main()