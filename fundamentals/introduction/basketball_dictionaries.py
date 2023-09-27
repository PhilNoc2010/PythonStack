class Player:
    all_players = []

    def __init__(self, player):
        for k,v in player.items():
            setattr(self, k, v)
        Player.all_players.append(self)

    @classmethod
    def team_roster(cls):
        for player in cls.all_players:
            print(player.name)


players = [
    {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving",
    	"age":32,
        "position": "Point Guard",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard",
    	"age":33,
        "position": "Point Guard",
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid",
    	"age":32,
        "position": "Power Foward",
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

kevin = {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving",
    	"age":32,
        "position": "Point Guard",
    	"team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???

# player_jason = Player(jason)
# player_kyrie = Player(kyrie)
# player_kevin = Player(kevin)

for i in range(len(players)):
    first_name = players[i]["name"][0:players[i]["name"].find(" ")]
    objname = "player_" + first_name.lower()
    objname = Player(players[i])

Player.team_roster()