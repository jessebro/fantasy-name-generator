from random import choice

male_names = (
    "Alander",
    "Aldath",
    "Alvyn",
    "Andra",
    "Atyn",
    "Axran",
    "Beralt",
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
    "Hartis",
    "Ikadell",
    "Javic",
    "Jebus",
    "Kayu",
    "Kendor",
    "Khiln",
    "Layal",
    "Leifen",
    "Lenn",
    "Luin",
    "Marlo",
    "Mardon",
    "Mastalay",
    "Mayin",
    "Micha",
    "Perel",
    "Phalray",
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
    "Ulen",
    "Vandimar"
    )

female_names = (
    "Aethila",
    "Amber",
    "Amli",
    "Astira",
    "Atra",
    "Berina",
    "Cassala",
    "Chana",
    "Cilanna",
    "Dandela",
    "Elira",
    "Erakoda",
    "Erlda",
    "Feretta",
    "Gwilafeyir",
    "Hilda",
    "Iris",
    "Isich",
    "Jean",
    "Jia",
    "Karina",
    "Kattifey",
    "Krista",
    "Lihn",
    "Lydia",
    "Mara",
    "Mavella",
    "Medanno",
    "Merlie",
    "Pera",
    "Quin",
    "Raven",
    "Revella",
    "Rivani",
    "Selena",
    "Sifli",
    "Stinella",
    "Tesha",
    "Tora",
    "Velda",
    "Yemir"
)

family_names = (
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
    "Glimmerwood",
    "Helzak",
    "Jadefall",
    "Kadoran",
    "Kindleberry",
    "Kylengard",
    "Laven",
    "Lilyfoot",
    "Mandreiga",
    "Nellamei",
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
        "male": list(male_names),
        "female": list(female_names),
        "family": list(family_names)
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
    - type 'l' to display the name pool
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

    elif gender == "l":
        display = f"""
    
~MALE~        {male_names}  

~FEMALE~      {female_names} 

~FAMILY~      {family_names}
    """
        return display


if __name__ == '__main__':
    main(reset())
