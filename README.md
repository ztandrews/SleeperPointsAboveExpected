# Sleeper Points Above Expected
### V 1.0.0
A data visualization tool to show your Sleeper fantasy football roster's points above projected.
## About
This is a program that will show your Sleeper fantasy football roster's PPR fantasy points above projected via a bar chart. The program loops through your roster for each week of the season and calculates the players actual points - projected points and returns the total difference from each week so far in a season. The point of this program is to see which players are overperforming and which are underperforming. If a player has a high points above projected, they are likely overperforming, and if they have a low/negative points above projected, they are underperforming.

The program uses Python, an "undocumented" Sleeper API, the real Sleeper API, and matplotlib to visualize the data.

In the future, I plan to run some sort of model accuracy test to determine how accurate Sleepers projections are, because in the end, while we can draw conclusions about if a player is over/under performing, it's smart to keep in mind that the reason we make those conclusions could be because Sleepers point projection model isn't good. For the most part, based on an extremely general eye test (and you'll see in the sample provided in this README) the projections seem fairly accurate.
## How To Run
Note - I know this program is kind of tedious to run. I plan on fixing this in the future. For now thoguh, here are the steps:
Wait Another Note - Also, I used PyCharm Community to run this. You could use any IDE but this or Spyder would be the best options as they are great for Data Vis. Ok now the steps:
1. Download code and open in the IDE. You'll notice there are two main sections for code: Config and Main. We'll be working in the Config section only.
2. Add your league ID into the league_id variable. You can find your leagues ID in the Sleeper URL bar like this:

![image](https://user-images.githubusercontent.com/68918006/142707164-b7684c22-5278-43bd-b956-d370ddec09cf.png)

3. This next step is the most tedious. We need to find the index of your team in the response. I reccomend using an app like Postman to get the response of the API to find your team. Go to this URL: https://api.sleeper.app/v1/league/{YourLeagueID}/rosters and search for your team. Now, the most annoying part of this is there really isn't an easy way to find your team. You kind of have to look through every single team in the array and find player nicknames that are on your team. Once you find your team, take the roster_id and subtract 1. This will be what you add to the my_team variable. The reason for this being the API doesn't give us team names, it only gives us a team number (1-the amount of teams in your league) and a user ID, which I haven't found a way to find on the Sleeper website. Since that was just about impossible to follow, here is a step by step tutorial with screenshots on how to find your team:

First, find a player nickname you can search. Here's mine:
![image](https://user-images.githubusercontent.com/68918006/142706285-f6be267b-738f-4f15-80d5-a60b875173cc.png)

Next, go into Postman and paste the API URL into it, with your own league ID where mine is:
![image](https://user-images.githubusercontent.com/68918006/142707259-0bc38fa2-79bb-471c-a2f9-222a1e40204e.png)

After clicking run, you should see a response with every team in your leagues roster. CTL+F and search for the nickname of your player that you want to find like so:
![image](https://user-images.githubusercontent.com/68918006/142745952-4b7c3196-5c8a-4b15-9b2d-cd8c854c93d3.png)

After fidning the nickname, scroll up and find roster_id. Subtract 1 from that, and set that to the my_team variable.
![image](https://user-images.githubusercontent.com/68918006/142706477-089c735a-0d84-4f40-8867-2cb3e68eb1ad.png)



4. Once you have all of the variables in the config section asigned, run the code! It may take a while so be patient with that.


## Sample Output
![sample](https://user-images.githubusercontent.com/68918006/142657452-f41ae6a1-ea78-413e-a0e2-503e75883884.png)
This is the type of output we can expect after running the program. Just drawing some basic conclusions from this, we can see that Brandon Aiyuk is by far my most underperformig player. This checks out, as he has had a very underwheliming year compared to his incredible rookie season. In general, my team is underperforming, which also holds true as this roster is not putting up as many wins or points as much of the league expected. 
## Version Updates
### 1.0.0
- Initial commit.
