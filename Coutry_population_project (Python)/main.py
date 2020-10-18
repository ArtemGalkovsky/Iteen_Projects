from tkinter import *
from tkinter import ttk
import json as j
from random import randrange

root = Tk()
root.minsize(600, 300)

canv = Canvas(root, width=400, height=400)
canv.grid(row=1, column=1, rowspan=2)  # pack(side=LEFT)

root.update()
w = canv.winfo_width()  # - canv.winfo_width() / 3#canv.winfo_width()
h = canv.winfo_height()

print(w, h)

# X = canv.winfo_width() // 2
# Y = canv.winfo_height() // 2

with open("country.json", "r+") as fl:
    # print(fl.read())
    # json = j.load(fl.read())
    # file = fl.read()
    json = j.load(fl)

# print(json["country"])

diagram = {

}

# ALL_DENSITY = {}

for country in json["country"]:
    print(json["country"][country])
    json["country"][country]["density"] = json["country"][country]["population"] / json["country"][country]["area"]
    diagram[country] = {"density": json["country"][country]["density"], "%": 0,
                        "color": "#%02x%02x%02x" % (randrange(50, 256, 1), randrange(50, 256, 1), randrange(50, 256, 1))}

ALL_DENSITY = 360 / sum(
    json["country"][country]["density"] for country in json["country"]
)
# print(diagram)

# {country: [diagram[country]["density"] for country in diagram]}
# MAX_DENSITY = max(ALL_DENSITY.values)#max([diagram[country]["density"] for country in diagram])

# print(ALL_DENSITY)

# print(ALL_DENSITY)

canv.create_oval(w / 6, h / 6, w - w / 6, h - h / 6, outline="black")

start_deg = 0
# textY = h / 8

for country in diagram:
    diagram[country]["%"] = ALL_DENSITY * diagram[country][
        "density"]  # (ALL_DENSITY - diagram[country]["density"]) / diagram[country]["density"]
    # pass
    # print(MAX_DENSITY)
    canv.create_arc(w / 6, h / 6, w - w / 6, h - h / 6, start=start_deg, extent=diagram[country]["%"],
                    fill=diagram[country][
                        "color"])  # "#%02x%02x%02x" % (randrange(0, 256, 1), randrange(0, 256, 1), randrange(0, 256, 1)))  #$f"#{randrange(0, 256, 1)}02x{randrange(0, 256, 1)}02x{randrange(0, 256, 1)}02x")
    # canv.create_text(w - w / 3 - start_deg, h / 8 + start_deg, text=country, justify="center", font="Arial 20") #h / 4 + start_de
    # canv.create_text(w / 6 + , h + )
    # print(country, start_deg, start_deg + diagram[country]["%"], diagram[country]["%"])
    start_deg += diagram[country]["%"]
    # textY += 30
    # canv.create_text(w + textX)
    # print(country, start_deg, start_deg + diagram[country]["%"], diagram[country]["%"])
    # print("#%02x%02x%02x" % (randrange(0, 256, 1), randrange(0, 256, 1), randrange(0, 256, 1)))
# canv.create_oval(w / 6, h / 6, w - w/6, h - h/6, outline="black")#outline=f"#{randrange(0, 256, 1)}02x{randrange(0, 256, 1)}02x{randrange(0, 256, 1)}02x")

countryList = [country.upper() for country in diagram]

countryCombo = ttk.Combobox(root, value=countryList, width=26)
countryCombo.current(0)


def combo_select(event):
    print("f")
    #colorBox.configure(bg=diagram[countryList[countryList.index(countryCombo.get())].lower()]["color"])#countryCombo.get())#.#bg = diagram[countryList[countryList.index(countryCombo.get())].lower()]["color"]#countryCombo.get()
    #colorBox.grid(row=2, column=2)
    BoxLabel.configure(bg=diagram[countryList[countryList.index(countryCombo.get())].lower()]["color"], text=f"""{countryCombo.get()}
{round(100 / (360 / diagram[countryCombo.get().lower()]['%']))}%
Area: {json["country"][countryCombo.get().lower()]['area']} km2
Population: {json["country"][countryCombo.get().lower()]['population']} people""",) #text=f"{countryCombo.get()} \n {round(diagram[countryCombo.get().lower()]['%'])}") #text=f"{countryCombo.get()} \n {int(360 / diagram[countryCombo.get().lower()]['%'])}%")#text=f"{countryCombo.get()} \n {1 / diagram[countryCombo.get().lower()]['%'] * 360}%")
    # colorBox.update()
    #pass
    # print(event)
    # pass


countryCombo.bind("<<ComboboxSelected>>", combo_select)

countryCombo.grid(row=1, column=2)

print(diagram[countryList[countryList.index(countryCombo.get())].lower()]["color"])
colorBox = Frame(root)#, width=180, height=200)
colorBox.grid(row=2, column=2)

BoxLabel = Label(colorBox, text=f"""{countryCombo.get()}
{round(100 / (360 / diagram[countryCombo.get().lower()]['%']))}%
Area: {json["country"][countryCombo.get().lower()]['area']} km2
Population: {json["country"][countryCombo.get().lower()]['population']} people""",
                            bg=diagram[countryList[countryList.index(countryCombo.get())].lower()]["color"], height=10, font="Arial 20")
BoxLabel.pack()

#print(1 / diagram[countryCombo.get().lower()]['%'])

#print(360 / diagram[countryCombo.get().lower()]['%'])

# print(diagram)

# print(json)

# diagram = {
#
# }

root.mainloop()
