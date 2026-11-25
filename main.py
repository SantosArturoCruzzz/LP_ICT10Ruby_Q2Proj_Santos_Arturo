from pyscript import display, document

shardbearers = [
    "godrickthegrafted",
    "rennalaqueenofthefullmoon",
    "starscourgeradahn",
    "morgotttheomenking",
    "rykardlordofblasphemy",
    "mohglordofblood",
    "maleniabladeofmiquella"
]

print("AsherComingout")


elden_ring_classes = {
    "Vagabond": {"lvl": 9, "vig": 15, "mnd": 10, "end": 11, "str": 14, "dex": 13, "int": 9, "fai": 9, "arc": 7},
    "Warrior": {"lvl": 8, "vig": 11, "mnd": 12, "end": 11, "str": 10, "dex": 16, "int": 10, "fai": 8, "arc": 9},
    "Hero": {"lvl": 7, "vig": 14, "mnd": 9, "end": 12, "str": 16, "dex": 9, "int": 7, "fai": 8, "arc": 11},
    "Bandit": {"lvl": 5, "vig": 10, "mnd": 11, "end": 10, "str": 9, "dex": 13, "int": 9, "fai": 8, "arc": 14},
    "Astrologer": {"lvl": 6, "vig": 9, "mnd": 15, "end": 9, "str": 8, "dex": 12, "int": 16, "fai": 7, "arc": 9},
    "Prophet": {"lvl": 7, "vig": 10, "mnd": 14, "end": 8, "str": 11, "dex": 10, "int": 7, "fai": 16, "arc": 10},
    "Samurai": {"lvl": 9, "vig": 12, "mnd": 11, "end": 13, "str": 12, "dex": 15, "int": 9, "fai": 8, "arc": 8},
    "Prisoner": {"lvl": 9, "vig": 11, "mnd": 12, "end": 11, "str": 11, "dex": 14, "int": 14, "fai": 6, "arc": 9},
    "Confessor": {"lvl": 10, "vig": 10, "mnd": 13, "end": 10, "str": 12, "dex": 12, "int": 9, "fai": 14, "arc": 9},
    "Wretch": {"lvl": 1, "vig": 10, "mnd": 10, "end": 10, "str": 10, "dex": 10, "int": 10, "fai": 10, "arc": 10},
    "Heavy Knight": {"lvl": 10, "vig": 14, "mnd": 8, "end": 17, "str": 15, "dex": 11, "int": 7, "fai": 8, "arc": 9},
    "Idus Knight": {"lvl": 7, "vig": 10, "mnd": 12, "end": 11, "str": 13, "dex": 15, "int": 8, "fai": 11, "arc": 6},
}



def find(e):
    document.getElementById("output").innerHTML = " "
    userInput = document.getElementById('input').value.strip().title()



    data = elden_ring_classes.get(
        userInput,
            {
            "lvl": "Please type in a class",
            "mnd": "0",
            "end": "0",  
            "str": "0",
            "dex": "0",
            "int": "0",
            "fai": "0",
            "arc":  "0",
        }
    )


    document.getElementById('output').innerHTML = f"""
    <b>lvl:</b> {data["lvl"]} <br>
    <b>mnd:</b> {data["mnd"]} <br>
    <b>end:</b> {data["end"]} <br>
    <b>str:</b> {data["str"]} <br>
    <b>dex:</b> {data["dex"]}   <br>
    <b>int:</b> {data["int"]}   <br>
    <b>fai:</b> {data["fai"]}   <br>
    <b>arc:</b> {data["arc"]}   <br>
"""


def Shardbearer(e):
    document.getElementById("output").innerHTML = ""
    first = document.getElementById("Shardbearer").value.strip().lower()
    second = document.getElementById("Title").value.strip().lower() 
    fullname = first + second 


    output = document.getElementById("output")
    
    if fullname.replace(" ", "") in shardbearers: 
        output.innerHTML = "Collect all the Great Runes!"
    else: 
        output.innerHTML = "That is not a shardbearer, tarnished.." 

    