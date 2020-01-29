import webbrowser

print("""Welcome to my baseball bot! I am designed to give you
information about your favourite baseball team.

CODES

AL East
TOR = Toronto Blue Jays
NYY = New York Yankees
BOS = Boston Red Sox
BAL = Baltimore Orioles
TB = Tampa Bay Rays

AL West
HOU = Houston Astros
OAK = Oakland Athletics
LAA = Los Angeles Angels
TEX = Texas Rangers
SEA = Seattle Mariners

AL Central
MIN = Minnesota Twins
CLE = Cleveland Indians
CWS = Chicago White Sox
KC = Kansas Royals
DET = Detroit Tigers

""")

TOR = "TOR"
NYY = "NYY"
BOS = "BOS"
BAL = "BAL"
TB = "TB"
HOU = "HOU"
OAK = "OAK"
LAA = "LAA"
TEX = "TEX"
SEA = "SEA"
MIN = "MIN"
CLE = "CLE"
CWS = "CWS"
KC = "KC"
DET = "DET"

baseball_teams = [TOR, NYY, BOS, BAL, TB, HOU, OAK, LAA, TEX, SEA,
                  MIN, CLE, CWS, KC, DET]

team = input("Please enter the CODE for which team you are interested in: ")
if team not in baseball_teams:
    print('Invalid Team!')
else:
    selection = input("Which of the following are you interested in (twitter, roster, tickets): ")

    TWITTER = (selection == 'twitter')
    ROSTER = (selection == 'roster')
    TICKETS = (selection == 'tickets')
    
    if team == TOR:
        if TWITTER:
            webbrowser.open('https://twitter.com/BlueJays')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/tor/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/toronto-blue-jays-tickets/artist/806032')
        else:
            print("Invalid option")
    elif team == NYY:
        if TWITTER:
            webbrowser.open('https://twitter.com/Yankees')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/nyy/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/new-york-yankees-tickets/artist/805992')
        else:
            print("Invalid option")
    elif team == BOS:
        if TWITTER:
            webbrowser.open('https://twitter.com/redsox')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/bos/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.com/boston-red-sox-tickets/artist/805904')
        else:
            print("Invalid option")   
    elif team == BAL:
        if TWITTER:
            webbrowser.open('https://twitter.com/Orioles')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/bal/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.com/baltimore-orioles-tickets/artist/805900')
        else:
            print("Invalid option")
    elif team == TB:
        if TWITTER:
            webbrowser.open('https://twitter.com/RaysBaseball')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/tb/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.com/tampa-bay-rays-tickets/artist/806027')
        else:
            print("Invalid option")
    elif team == HOU:
        if TWITTER:
            webbrowser.open('https://twitter.com/astros')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/hou/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/houston-astros-tickets/artist/805948')
        else:
            print("Invalid option")
    elif team == OAK:
        if TWITTER:
            webbrowser.open('https://twitter.com/Athletics')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/oak/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/oakland-athletics-tickets/artist/805993')
        else:
            print("Invalid option")
    elif team == LAA:
        if TWITTER:
            webbrowser.open('https://twitter.com/Angels')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/laa/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/los-angeles-angels-tickets/artist/805892')
        else:
            print("Invalid option")
    elif team == TEX:
        if TWITTER:
            webbrowser.open('https://twitter.com/Rangers')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/tex/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/texas-rangers-tickets/artist/806031')
        else:
            print("Invalid option")
    elif team == SEA:
        if TWITTER:
            webbrowser.open('https://twitter.com/Mariners')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/sea/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/seattle-mariners-tickets/artist/806019')
        else:
            print("Invalid option")
    elif team == MIN:
        if TWITTER:
            webbrowser.open('https://twitter.com/Twins')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/min/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/minnesota-twins-tickets/artist/805972')
        else:
            print("Invalid option")
    elif team == CLE:
        if TWITTER:
            webbrowser.open('https://twitter.com/Indians')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/cle/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/cleveland-indians-tickets/artist/805922')
        else:
            print("Invalid option")
    elif team == CWS:
        if TWITTER:
            webbrowser.open('https://twitter.com/whitesox')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/cws/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.ca/chicago-white-sox-tickets/artist/805917')
        else:
            print("Invalid option")
    elif team == KC:
        if TWITTER:
            webbrowser.open('https://twitter.com/Royals')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/kc/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.com/kansas-city-royals-tickets/artist/805956')
        else:
            print("Invalid option")
    elif team == DET:
        if TWITTER:
            webbrowser.open('https://twitter.com/tigers')
        elif ROSTER:
            webbrowser.open('http://m.mlb.com/det/roster')
        elif TICKETS:
            webbrowser.open('https://www.ticketmaster.com/detroit-tigers-tickets/artist/805940')
        else:
            print("Invalid option")    

            






