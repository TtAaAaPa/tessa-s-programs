import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

show = pg.prompt ("Please make all your answers Upper-case")

show = pg.prompt ("what is your favorite show")

if show == "Parks and rec":
    pg.alert ("That is a really godd show!")
    points += 2
    t.sleep (2)
    wb.open("https://www.google.com/search?q=parks+and+rec&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjMn9rrhrHeAhURUt8KHYbcBr8Q_AUIDygC&biw=1011&bih=685#imgrc=s9mU6eo9VMmYxM:")
elif show == "The office":
    pg.alert (" I love Dwight!")
    points += 3
    t.sleep (2)
    wb.open ("https://www.youtube.com/watch?v=M8KmqaJvgpE")
elif show =="Freinds":
    pg.alert ("I love that show")
    points += 6
    t.sleep (2)
    wb.open("https://www.google.com/search?q=ryan+brush&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjE7qf45I3eAhVIT98KHcpZAr4Q_AUIDigB&biw=1500&bih=685#imgrc=RNDXBDtGg-UqdM:")
elif show == "Arrow":
    pg.alert ("I love arrow")
    points += 7
    t.sleep (2)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1500&bih=685&tbm=isch&sa=1&ei=2lXHW6H5G4vp_QbPranIBQ&q=baljeete+phineas+and+ferb&oq=baljeete+phineas+and+ferb&gs_l=img.3...13582.15235..17316...0.0..0.51.329.7......0....1..gws-wiz-img.1EkqOtQZ_WU#imgrc=g4QVnZa3_Pj9VM:")
elif show == "The Flash":
    pg.alert ("I love the flash")
    points += 2
    t.sleep (2)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1517&bih=695&tbm=isch&sa=1&ei=JJfQW9KZJeWN_Qbbw6v4DA&q=the+flash&oq=the+flash&gs_l=img.3..0l10.3604.6056..6331...0.0..0.57.447.9......0....1..gws-wiz-img.......0i67.RufJmOD2b-c#imgrc=zonaxkUNtt7mnM:")
elif show == "Suits":
    pg.alert ("I love suits")
    points += 5
    t.sleep (2)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1500&bih=685&tbm=isch&sa=1&ei=2lXHW6H5G4vp_QbPranIBQ&q=baljeete+phineas+and+ferb&oq=baljeete+phineas+and+ferb&gs_l=img.3...13582.15235..17316...0.0..0.51.329.7......0....1..gws-wiz-img.1EkqOtQZ_WU#imgrc=g4QVnZa3_Pj9VM:")
else:
    pg.alert ("Your Favorite show is " + str(show))
    points += 4
t.sleep (10)
food = pg.prompt ("What is your favorite food? ")
if food == "Pizza":
    pg.alert ("I love pizza!!")
    points += 6
    t.sleep (2)
    wb.open("https://www.google.com/search?q=pizza+hut&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjLmruDh7HeAhXET98KHTMjBjEQ_AUIESgE&biw=1011&bih=685#imgrc=SnVh6F74Tts6vM:")
elif food == "Ice cream":
    pg.alert ("I love ice cream")
    points += 4
    t.sleep (2)
    wb.open("https://www.google.com/search?q=ice+cream&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi7udSY6I3eAhUBTN8KHdKCDN0Q_AUIDygC&biw=1500&bih=685#imgrc=k32GClIWOV5_PM:")
elif food == "Tomatos":
    pg.alert ("tomatos are the best")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?q=pizza&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiK9pav6I3eAhXJhOAKHbm_CBQQ_AUIDygC&biw=1500&bih=685#imgrc=x_7gN_kuIgT94M:")
elif food == "Steak":
    pg.alert ("i love steak")
    points += 8
    pg.alert ("Your favorite food is" + str(food))
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1500&bih=685&tbm=isch&sa=1&ei=dFnHW6C2BuLl_QbS4JewBA&q=vans&oq=vans&gs_l=img.3..0l10.2016.7866..8618...6.0..0.55.507.11......0....1..gws-wiz-img.......0i30j0i5i30j0i24.QhgiHNes9Qs#imgrc=HyRG7O-DhZ4y1M:")
elif food == "Pasta":
    pg.alert ("I love pasta")
    points += 2
    pg.alert ("Your favorite food is" + str(food))
    t.sleep (2)
    wb.open("https://www.google.com/search?q=pasta&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiv2uybuJ_eAhXhYd8KHXpzALkQ_AUIDigB&biw=1517&bih=695#imgrc=tzXRwsLUoZUEtM:")
elif food == "Chicken":
    pg.alert ("I love Chicken")
    points += 3
    pg.alert ("Your favorite food is" + str(food))
    t.sleep (2)
    wb.open("https://www.google.com/search?q=chicken&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjUsIPRuJ_eAhXBneAKHXCsBY0Q_AUIDigB&biw=1517&bih=695#imgrc=V9bV1mZUWzW-YM:")
else:
    pg.alert ("Your favoite food is" + str(food))
t.sleep (10)
name = pg.prompt ("What is your name?")

if name == "Mr. Rill":
    pg.alert("I know you love sleep")
    points += 2
    t.sleep (2)
    wb.open("https://www.google.com/search?q=sleep&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjwre7vgLHeAhXLdN8KHcgmDf4Q_AUIDigB&biw=1011&bih=685#imgrc=PBoRxRgc9XbBtM:")
elif name == "Teddy":
    pg.alert("Thanks teddy")
    points += 9
    t.sleep (2)
    wb.open("https://www.google.com/search?q=pizza&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiK9pav6I3eAhXJhOAKHbm_CBQQ_AUIDygC&biw=1500&bih=685#imgrc=x_7gN_kuIgT94M:")
elif name == "Mr. Kelly":
    pg.alert(" hello mr kelly")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?q=pizza&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiK9pav6I3eAhXJhOAKHbm_CBQQ_AUIDygC&biw=1500&bih=685#imgrc=x_7gN_kuIgT94M:")
elif name == "Mr. Bowes":
    pg.alert(" hello mr bowes")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1500&bih=685&tbm=isch&sa=1&ei=HVnHW9GlM4mk_Qa2rJGgCg&q=catas&oq=catas&gs_l=img.3..0l10.1465.2181..3044...0.0..0.60.254.5......0....1..gws-wiz-img._lidHx7ViXE#imgrc=hVsEVjaBf87JQM:")
elif name == "Mr. Danforth":
    pg.alert(" hello mr Danforth")
    points += 4
    t.sleep (2)
    wb.open("https://www.google.com/search?q=boo&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjju-fi6Y3eAhVymeAKHUaTCQUQ_AUIDigB&biw=1500&bih=685#imgrc=gSs1TrnsbjRivM:")
elif name == "Mr. Hearn":
    pg.alert(" hello mr hearn")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1517&bih=695&tbm=isch&sa=1&ei=G5XQW8WQB8m5ggfw1Y24DQ&q=hi&oq=hi&gs_l=img.3..0l10.3497.4260..4565...0.0..0.58.111.2......0....1..gws-wiz-img.VoIuKivq15Y#imgrc=yGgGgEAgiXMGuM:")
elif name == "Mr. Sandler":
    pg.alert(" hello mr sandler")
    points += 7
    t.sleep (2)
    wb.open("https://www.google.com/search?q=todd+rosenbaum&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi92YGnt5_eAhVETd8KHeCtBHQQ_AUIDygC&biw=1517&bih=695#imgrc=FMHK7VGh5otoBM:")
else:
    pg.alert(" You're name is " + str(name))
 
t.sleep (10)
game = pg.prompt ("what is your favorite game?")
if game == "Fortnite":
    pg.alert("I love fortnite")
    points += 3
    t.sleep (2)
    wb.open("https://www.google.com/search?q=fortnite&rlz=1C1GCEA_enUS752US765&tbm=isch&source=lnms&sa=X&ved=0ahUKEwjpjO3Yr5_eAhUmmuAKHamlDREQ_AUIDCgD&biw=1517&bih=695&dpr=0.9#imgrc=H-2KEph21oPaCM:")
elif game == "call of duty":
    pg.alert("I love call of duty")
    points += 7
    t.sleep (2)
    wb.open("https://www.google.com/search?q=call+of+duty&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiSxMnwsJ_eAhVuTd8KHdgVCewQ_AUIESgE&biw=1517&bih=695#imgrc=WeL7r0v-tQZdtM:")
elif game == "Crossy Road":
    pg.alert(" I love crossy road")
    points += 2
    t.sleep (2)
    wb.open("https://www.google.com/search?q=crossy+road&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwib7oD_sZ_eAhWQUt8KHWPxAVYQ_AUIECgD&biw=1517&bih=695#imgrc=PUMrvyt4Y9FfVM::")
elif game == ("Call of duty and the office"):
    pg.alert("I love call of duty and the office")
    points += 1
    t.sleep (2)
    wb.open("https://www.youtube.com/watch?v=SLqoJwJ-KX0")
elif game == "Overwatch":
    pg.alert("I love Overwatch")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?q=overwatch&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiEop3Xsp_eAhVGnOAKHaFbDQoQ_AUIESgE&biw=1517&bih=695#imgrc=lzmaMjCLII0cDM:")
elif game == "Wii sports":
    pg.alert("I love Wii sports")
    points += 6
    t.sleep (2)
    wb.open("https://www.google.com/search?q=wii+sports&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiUsauDs5_eAhUFT98KHYhfCIsQ_AUIECgD&biw=1517&bih=695#imgrc=TIVOVbSrZWrSEM:")
else:
    pg.alert(" You're favorite game is " + str(game))
sport = pg.alert
if sport == "Hockey ":
    pg.alert("I love hcokey")
    points += 1
    t.sleep (2)
    wb.open("https://www.google.com/search?q=hockey&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi15_PVs5_eAhVGnOAKHaFbDQoQ_AUIECgD&biw=1517&bih=695#imgrc=s3TSpoXFbeSI8M:")
elif sport == ("Hockey"):
    pg.alert("U are the best")
    t.sleep (2)
    points += 4
    wb.open("https://www.google.com/search?q=the+office&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi4pcKNtJ_eAhWphOAKHVQ5BEIQ_AUIECgD&biw=1517&bih=695#imgrc=9DZrDAa4UC_IrM:")
elif sport == "Lacrosse":
    pg.alert("I love lacrosse")
    points += 8
    t.sleep (2)
    wb.open("https://www.google.com/search?q=lacrosse&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjT1NettJ_eAhWvmeAKHcQEBPcQ_AUIDigB&biw=1517&bih=695#imgrc=PHLcEZN_N-hF9M:")
elif sport == "Coding":
    pg.alert("I love to code")
    points += 2
    t.sleep (2)
    wb.open("https://www.google.com/search?q=gcds+coding&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjqyebGtJ_eAhUohuAKHdv-AWwQ_AUIDygC&biw=1517&bih=695#imgrc=bjMfMwT7kBHk6M:")
elif sport == "Football":
    pg.alert("I love football")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?q=football&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiZnqz1tJ_eAhXHY98KHbdkCWkQ_AUIDigB&biw=1517&bih=695#imgrc=8S82xA3w4zYoLM:")
elif sport == "Soccer":
    pg.alert("I love soccer")
    points += 3
    t.sleep (2)
    wb.open("https://www.google.com/search?q=soccer&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjn6__ItZ_eAhXoQd8KHWsECwsQ_AUIDygC&biw=1517&bih=695#imgrc=gwUr-6lwAisCpM:")
elif game == "Soccer":
    pg.alert("Fortnite soccer")
    points += 5
    t.sleep (2)
    wb.open("https://www.google.com/search?q=soccer&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjn6__ItZ_eAhXoQd8KHWsECwsQ_AUIDygC&biw=1517&bih=695#imgrc=gwUr-6lwAisCpM:")
else:
    pg.alert(" You're favorite sport is " + sport)
pg.alert("You have " + str(points) + " points.")

