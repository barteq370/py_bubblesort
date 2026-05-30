#1. Rozwiązanie książkowe (z użyciem funkcji)

def bubble_sort(lista):                                         #definicja funkcji która potem jest wywoływana w linijce 16
    n = len(lista)                                              #n = długość listy (len - length)
    for i in range(n-1):                                        #pętla która przechodzi przez wszystkie elementy listy (w nawiasie można napisać "0, n-1" żeby było bardziej czytelne)
        for j in range(0, n-i-1):                               #pętla która przechodzi przez wszystkie elementy listy oprócz tych które już są posortowane
            if lista[j] > lista[j+1]:                           #jeśli pierwszy element jest większy to \/
                lista[j], lista[j+1] = lista[j+1], lista[j]     #zamiana miejscami sąsiednich elementów
    return lista                                                #funkcja zwraca posortowaną listę


print("Ile elementów ma mieć lista?)")                           
n = int(input())                                                #pobieranie od użytkownika liczby (int) elementów
lista = []                                                      #tworzenie pustej listy do której będą dodawane elementy
for i in range(n):                                              #pętla która przechodzi przez wszystkie elementy listy (w nawiasie można napisać "0, n" żeby było bardziej czytelne)
    print(f"Podaj {i+1} element:")
    lista.append(int(input()))                                  #dodawanie elementów do listy (append - dodaj na koniec listy)                    
posortowana_lista = bubble_sort(lista)                          #wywołanie funkcji bubble_sort i przypisanie jej wyniku do zmiennej posortowana_lista
print("Posortowana lista:", posortowana_lista)



#2. Dokładnie to samo rozwiązanie ale bez użycia funkcji (wszystko w jednym "bloku" kodu)

print("Ile elementów ma mieć lista?")
n = int(input())
lista = []
for i in range(n):                                              
    print(f"Podaj {i+1} element:")
    lista.append(int(input()))     

n = len(lista)
for i in range(n-1):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Posortowana lista:", lista)


#3. Zablokowanie możliwości wpisanie liczb innych niz 1-10

print("Ile elementów ma mieć lista? (1-10)")
n = int(input())
while n < 1 or n > 10:                                                          # while - dopóki n jest mniejsze niż 1 lub większe niż 10 to wykonuj kod poniżej
    print("Nieprawidłowa liczba elementów. Podaj liczbę z zakresu 1-10:")       ##
    n = int(input())                                                            ##

lista = []
for i in range(n):                                              
    print(f"Podaj {i+1} element:")
    lista.append(int(input()))     

n = len(lista)
for i in range(n-1):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Posortowana lista:", lista)
