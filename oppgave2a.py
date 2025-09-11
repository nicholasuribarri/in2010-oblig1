
#liste = [0,1,2,3,4,5,6,7,8,9,10]
#sorted_to_balanced(liste)


def sorted(sorted_arr, start, end):
    if start > end:
        return
    
    middle = (start + end) // 2
    print(sorted_arr[middle])

    sorted(sorted_arr, start, middle -1)
    sorted(sorted_arr, middle + 1, end)


#skriv: 
#python3 oppgave2a.py < sortert_input
# sortert_input er en fil med sorterte heltall nedover

read = sys.stdin.read().splitlines() # en liste med 1 element for hver linje
input = []
for i in read:
    input.append(i)


#sorted(liste, 0, len(liste)-1)
sorted(input, 0, len(input)-1)
