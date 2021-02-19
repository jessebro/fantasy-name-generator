from random import choice

wimblebean = (
    "Alander",
    "Aldath",
    "Alvyn",
    "Andra",
    "Atyn",
    "Axran",
    "Bertholt",
    "Caylen",
    "Dowrin",
    "Eladris",
    "Elis",
    "Erane",
    "Erdan",
    "Erwin",
    "Fagor",
    "Garurt",
    "Gejin",
    "Gildebran",
    "Javic",
    "Jebus",
    "Kayu",
    "Kendor",
    "Khiln",
    "Layal",
    "Leifen",
    "Lenn",
    "Luin",
    "Lumeus",
    "Marlo",
    "Mardon",
    "Mastalay",
    "Mayin",
    "Micha",
    "Perel",
    "Reiner",
    "Renan",
    "Rindel",
    "Rynne",
    "Sacura",
    "Sharley",
    "Shemor",
    "Silik",
    "Talet",
    "Tayle",
    "Thorin",
    "Tielek",
    "Tilamir",
    "Tilo",
    "Tirindek",
    "Vandimar"
    )

pepper = (
    "Aethila",
    "Amber",
    "Amli",
    "Astira",
    "Atra",
    "Cassala",
    "Chana",
    "Dandela",
    "Elira",
    "Erakoda",
    "Erlda",
    "Feretta",
    "Hilda",
    "Iris",
    "Isich",
    "Jia",
    "Jean",
    "Karina",
    "Kattifey",
    "Krista",
    "Lihn",
    "Lydia",
    "Mara",
    "Mavella",
    "Merlie",
    "Pera",
    "Quin",
    "Raven",
    "Rivani",
    "Sifli",
    "Tesha",
    "Tora",
    "Velda",
    "Yemir"
)

peggy = (
    "Alahin",
    "Alyton",
    "Ashroot",
    "Avary",
    "Beifanger",
    "Caldamire",
    "Cinderfell",
    "Darastrix",
    "Eringard",
    "Firemoon",
    "Helzak",
    "Jadefall",
    "Kadoran",
    "Kindleberry",
    "Kylengard",
    "Laven",
    "Lilyfoot",
    "Mandreiga",
    "Omar",
    "Polbar",
    "Rener",
    "Stellagard",
    "Silvermere",
    "Swallowtail",
    "Tenah",
    "Tyberan",
    "Ymbise",
    "Zekerane"
)


def reset():
    names = {
        "male": list(wimblebean),
        "female": list(pepper),
        "family": list(peggy)
    }
    return names


def main(names):
    gender = ""
    while gender != "x":
        if len(names['male']) == 0 or len(names['female']) == 0 or len(names['family']) == 0:
            names = reset()
        # print(f"There are {len(names['male'])} male names left and {len(names['female'])} female names left.")
        gender = input("""What gender is the character? 
    - type 'm' for male
    - type 'f' for female
    - type 'r' to reset the lists
    - type 'x' to exit
> """)
        generate(names, gender)


def generate(names, gender):

    if gender == "m":
        malechoice = choice(names['male'])
        familychoice = choice(names['family'])
        finalname = f"""

                ~{malechoice + " " + familychoice}~

                """
        print(finalname)
        names['male'].remove(malechoice)
        names['family'].remove(familychoice)
        return finalname

    elif gender == "f":
        femalechoice = choice(names['female'])
        familychoice = choice(names['family'])
        finalname = f"""

                ~{femalechoice + " " + familychoice}~

                """
        print(finalname)
        names['female'].remove(femalechoice)
        names['family'].remove(familychoice)
        return finalname
    elif gender == "r":
        names = reset()


if __name__ == '__main__':
    main(reset())
