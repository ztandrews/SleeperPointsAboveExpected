import requests
import matplotlib.pyplot as plt

#See README.md for better instructions on how to run the program.
######################################### Config ######################################################
#You can get this from looking at the URL bar on sleepers website
league_id = "" #Add league ID here
url = requests.get('https://api.sleeper.app/v1/league/'+league_id+'/rosters')
rosters = url.json()
#To get the team you want to see, you need to look at the response from the API above and find what index your team is at.
my_team = rosters[] #Add my_team roster index here
roster = my_team["players"]

week = 10
########################################## Main #######################################################
names_plot = []
points_plot = []

for player_id in roster:
    total_actual_points = 0
    total_projected_points = 0
    total_pts_abv_exp = 0
    for i in range(1, week):
        i = str(i)
        stats_url = requests.get(
            'https://api.sleeper.app/stats/nfl/2021/' + i + '?season_type=regular&position[]=FLEX&position[]=QB&position[]=RB&position[]=TE&position[]=WR&order_by=pts_ppr')
        proj_url = requests.get(
            'https://api.sleeper.app/projections/nfl/2021/' + i + '?season_type=regular&position[]=FLEX&position[]=QB&position[]=RB&position[]=TE&position[]=WR&order_by=pts_ppr')

        stats = stats_url.json()
        projections = proj_url.json()

        actual_points_found = False
        for player in stats:
            ids = player['player_id']
            if ids == player_id:
                fname = player['player'].get('first_name')
                lname = player['player'].get('last_name')
                name = fname + " " + lname
                actual_points = player['stats'].get('pts_ppr')
                if type(actual_points) != float:
                    actual_points = 0
                actual_points_found = True
        if actual_points_found != True:
            actual_points = 0
        for player in projections:
            ids = player['player_id']
            if ids == player_id:
                projected_points = player['stats'].get('pts_ppr')
                if type(projected_points) != float:
                    projected_points = 0


        total_actual_points += actual_points
        total_projected_points += projected_points
        pts_abv_expected = actual_points - projected_points
        total_pts_abv_exp += pts_abv_expected


    print(name)
    print("Total Projected Points: ", total_projected_points)
    print("Total Actual Points", total_actual_points)
    print("Total Points Above Expected:", total_pts_abv_exp)
    names_plot.append(name)
    points_plot.append(total_pts_abv_exp)
    print()

plt.bar(names_plot, points_plot)
plt.xticks(rotation=55)
plt.title("2021 Points Above Slepper Predictions")
plt.ylabel("Points Above Predicted")
plt.xlabel("Player")
plt.show()
