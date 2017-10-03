# DPG 101 [E]
# Years w/ and w/o repeatind digits

runcount = 0
count = 0
runyears = []
years = []
streak = 0
streaklist = []

antiruncount = 0
anticount = 0
antirunyears = []
antiyears = []
antistreak = 0
antistreaklist = []

def deconstruct(x):
    a = x / 1000
    b = (x - a * 1000) / 100
    c = (x - a * 1000 - b * 100) / 10
    d = (x - a * 1000 - b * 100 - c * 10)
    return [a, b, c, d]

first = int(raw_input("\nFirst year >> "))
last = int(raw_input("\nLast year >> "))

for k in range(first, last+1):

    L = deconstruct(k)
    a = deconstruct(k)[0]
    b = deconstruct(k)[1]
    c = deconstruct(k)[2]

    if (L.count(a) == L.count(b) == L.count(c) == 1):
        years += [k]
        count += 1

        runcount += 1
        runyears += [k]
        
        if (antiruncount > antistreak):
            antistreak = antiruncount
            antistreaklist = antirunyears
        antiruncount = 0
        antirunyears = []

    else:
      antiyears += [k]
      anticount += 1

      antiruncount += 1
      antirunyears += [k]
      
      if (runcount > streak):
          streak = runcount
          streaklist = runyears
      runcount = 0
      runyears = []


print "\nTotal w/o repeats", count
# print "\nList", years
print "\nLongest Streak", streak
print "\nStreak List", streaklist, "\n"

print "\nTotal w/ repeats", anticount
# print "\nList", antiyears
print "\nLongest Streak", antistreak
print "\nStreak List", antistreaklist, "\n"



exitprogram = raw_input("anykey to quit >> ")
