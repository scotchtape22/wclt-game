#!/bin/python
#WORLD CHAMPIONSHIP LAZER TAG
#Single Game Debugger
import random
import time
from operator import itemgetter


def die_roll(chk,player,team):
	the_roll = random.randint(0,99)
	#Debug log roll
	game_log(player['name']+" rolled a "+str(the_roll)+" for "+chk,"l")
	if chk == "int":
		the_result = player["s_int"] - the_roll
		if player["drug"] == "cocaine":
			the_result = the_result*1.25
		elif player["drug"] == "marijuana":
			the_result = the_result*.8		
		if player["per"] == "aggressive":
			the_result = the_result*1.25
		elif player["per"] == "reactive":
			the_result = the_result*.8	
		if player["c_pos"] == "skirmisher":
			the_result = the_result*2
		elif player["c_pos"] == "guard":
			the_result = the_result*.5
	elif chk == "acc":
		the_result = player["s_acc"] - the_roll
		if player["drug"] == "adderall":
			the_result = the_result*1.25
		elif player["drug"] == "cocaine":
			the_result = the_result*.8		
		if player["per"] == "stoic":
			the_result = the_result*1.25
		elif player["per"] == "aggressive":
			the_result = the_result*.8	
		if player["c_pos"] == "battleline":
			the_result = the_result*2
		elif player["c_pos"] == "skirmisher":
			the_result = the_result*.5
	elif chk == "eva":
		the_result = player["s_eva"] - the_roll
		if player["drug"] == "marijuana":
			the_result = the_result*1.25
		elif player["drug"] == "adderall":
			the_result = the_result*.8		
		if player["per"] == "reactive":
			the_result = the_result*1.25
		elif player["per"] == "stoic":
			the_result = the_result*.8	
		if player["c_pos"] == "guard":
			the_result = the_result*2
		elif player["c_pos"] == "battleline":
			the_result = the_result*.5
	elif chk == "pot":
		the_result = player["s_eva"] - the_roll
		if player["per"] == "ambitious":
			the_result = the_result+20
		if the_result < 0 and team["Mentor"] != -1:
			the_result = random.randint(0,99) - team["Mentor"]
	elif chk == "fit":
		the_result = player["s_eva"] - the_roll
		if player["drug"] == "steroid":
			the_result = the_result+20
		if the_result < 0 and team["Medical"] != -1:
			the_result = random.randint(0,99) - team["Medical"]
	# Check for results
	# Round result
	round(the_result)
	if p["inj"] > 0:
		the_result = the_result - 50
	#If 90+, a light was generated
	if the_result > 89 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" made a highlighut play!","l")
		team["Lights"] = team["Lights"] + 1
	#50+ earns exp, -25 earns fatigute
	if the_result > 49 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" learned something!","l")
		player["exp"] = player["exp"] + 1
	elif the_result < -25 and chk != "pot" and chk != "fit":
		game_log(player["name"]+" may have injured himself!","l")
		player["fat"] = player["fat"] + 1
	return the_result


def game_log(msg,tier):
	#Will write to a file eventually
	#Tiers: d - debug,l - log only, t - terminal and log
	#Don't show die rolls to screen?
	if tier == 't':
		print(msg)
		time.sleep(1)
		return
	elif tier == 'l':
		return


#Handles game from loading teams from file
#Up until gaining credits

all_players = []
#Load Home Team
h_team={"name":"hometeam","points":0,"Medicial":-1,"Mentor":-1,"Marketeer":-1,"Lights":0,"Fan_Exp":0,"Fan_Cap":0,"Coach_Cost":0}
#Load Players
h_path = input("Home Team File: ")
h_load = open(h_path,"r+")
for x in h_load:
	xi = x.split(':')
	if xi[0] == "medic":
		h_team["Medical"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "mentor":
		h_team["Mentor"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "marketeer":
		h_team["Markteer"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "medic":
		h_team["Medical"] = xi[8]
		h_team["Coach_Cost"] = h_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "stadium":
		h_team["Fan_Exp"] = xi[1]
		h_team["Fan_Cap"] = xi[2]
	elif xi[0] == "roster-player":
		new_player={"name":xi[1],"team":"home",
		"s_int":int(xi[2]),"s_acc":int(xi[3]),"s_eva":int(xi[4]),"s_pot":int(xi[5]),"s_fit":int(xi[6]),"s_ego":int(xi[7]),"s_kno":int(xi[8]),
		"per":xi[9],"drug":xi[10],
		"r_init":0,"r_shts":0,"r_hit":0,
		"c_pos":"","w_pos":xi[11],"sw_pos":xi[12],"l_pos":xi[13],"sl_pos":xi[14],
		"exp":0,"fat":0,
		"inj":int(xi[15]),"g_ht":0,"g_ph":0,"g_fc":0,"g_st":0,"g_rd":0,"g_cost":int(xi[21])}
		all_players.append(new_player)

#Load Away Team
a_team={"name":"hometeam","points":0,"Medicial":-1,"Mentor":-1,"Marketeer":-1,"Lights":0,"Fan_Exp":0,"Fan_Cap":0,"Coach_Cost":0}
#Load Players
a_path = input("Away Team File: ")
a_load = open(a_path,"r+")

for x in a_load:
	xi = x.split(':')
	if xi[0] == "medic":
		a_team["Medical"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "mentor":
		a_team["Mentor"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "marketeer":
		a_team["Markteer"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "medic":
		a_team["Medical"] = xi[8]
		a_team["Coach_Cost"] = a_team["Coach_Cost"] + int(xi[10])
	elif xi[0] == "stadium":
		a_team["Fan_Exp"] = xi[1]
		a_team["Fan_Cap"] = xi[2]
	elif xi[0] == "roster-player":
		new_player={"name":xi[1],"team":"away",
		"s_int":int(xi[2]),"s_acc":int(xi[3]),"s_eva":int(xi[4]),"s_pot":int(xi[5]),"s_fit":int(xi[6]),"s_ego":int(xi[7]),"s_kno":int(xi[8]),
		"per":xi[9],"drug":xi[10],
		"r_init":0,"r_shts":0,"r_hit":0,
		"c_pos":"","w_pos":xi[11],"sw_pos":xi[12],"l_pos":xi[13],"sl_pos":xi[14],
		"exp":0,"fat":0,
		"inj":int(xi[15]),"g_ht":0,"g_ph":0,"g_fc":0,"g_st":0,"g_rd":0,"g_cost":int(xi[21])}
		all_players.append(new_player)
#Be sure to close files at the end
l_path = input("Game File: ")
l_load = open(l_path,"w+")

clock = 1
game_log("Match Begins!","t")

while clock < 41:
	#Figure out the game state and set the actions and reset round info
	if a_team["points"]+10 < h_team["points"]:
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["w_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["l_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
		#Home team winning by wide margin
		#Away team winning by wide margin
	elif a_team["points"] > h_team["points"]+10:
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["l_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["w_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
	elif a_team["points"] < h_team["points"]:
		#Home team winning by small margin
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["sw_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["sl_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
	elif a_team["points"] > h_team["points"]:
		#Away team winning by small margin
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["sl_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["sw_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
	else:
		#If the game is tied, use slightly losing
		for p in all_players:
			if p["team"]=="home":
				p["c_pos"] = p["sl_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000
			elif p["team"]=="away":
				p["c_pos"] = p["sl_pos"]
				p["r_shts"] = 0
				p["r_hit"] = 0
				p["r_init"] = -1000	

	#Roll initative for all players
	for p in all_players:
		#print(p['name']+" will be "+p['c_pos'])
		if p["c_pos"] == "bench":
			continue
		else:
			p["g_rd"] = p["g_rd"] + 1
			if p["team"]=="home":
				p["r_init"]=die_roll("int",p,h_team)
			elif p["team"]=="away":
				p["r_init"]=die_roll("int",p,a_team)
			#Count shots
			if p["c_pos"] != "ambush":
				p["r_shts"] = p["r_shts"] + 1
				if p["c_pos"] == "fteam":
					p["r_shts"] = p["r_shts"] + 1
				if p["per"] == "ambitious":
					p["r_shts"] = p["r_shts"] + 1				


	#Sort all players
	all_players = sorted(all_players, key=itemgetter('r_init'), reverse=True)

	#Shooting
	shots_remaining = 0
	for s in all_players:
		shots_remaining = shots_remaining + s["r_shts"]

	active = 0
	#print(shots_remaining)
	while shots_remaining > 0:
		#print(all_players[active]['name']+" is up to "+all_players[active]['c_pos']+" , shots remaining "+str(all_players[active]['r_shts'])+" , times hit "+str(all_players[active]['r_hit']))
		if all_players[active]["r_shts"] > 0:
			#print("player is acting")
			all_players[active]["r_shts"] = all_players[active]["r_shts"] - 1
			stealing = 1
			#Check action
			if all_players[active]["c_pos"] == "steal":
				#Look for ambush
				for ambu in all_players:
					if ambu["team"] != all_players[active]["team"] and ambu["c_pos"] == "ambush" and ambu["r_hit"] == 0:
						ambu["g_st"] = ambu["g_st"] + 1
						if ambu["team"] == "home":
							ambush = die_roll("acc",ambu,h_team)
							dodge = die_roll("eva",all_players[active],a_team)
							if ambush > dodge:
								game_log(ambu["name"]+" defends their flag from "+all_players[active]["name"]+"!","t")
								h_team["points"] = h_team["points"] + 1
								ambu["g_ph"] = ambu["g_ph"] + 1
								stealing = 0
						elif ambu["team"] == "away":
							ambush = die_roll("acc",ambu,a_team)
							dodge = die_roll("eva",all_players[active],t_team)
							if ambush > dodge:
								game_log(ambu["name"]+" defends their flag from "+all_players[active]["name"]+"!","t")
								a_team["points"] = a_team["points"] + 1
								ambu["g_ph"] = ambu["g_ph"] + 1
								stealing = 0
				#If unhit, steal!
				if stealing == 1:
					game_log(all_players[active]["name"]+" has stolen the enemy flag and ended the round!","t")
					if all_players[active]["team"] == "home":
						h_team["points"] = h_team["points"] + 4
						all_players[active]["g_fc"] = all_players[active]["g_fc"] + 1
					elif all_players[active]["team"] == "away":
						a_team["points"] = a_team["points"] + 4
						all_players[active]["g_fc"] = all_players[active]["g_fc"] + 1
					break
			else:
				#Else, find targets
				#print("Looking for target")
				target = len(all_players) - 1
				while target > 0:
					if all_players[target]["team"] != all_players[active]["team"] and all_players[target]["c_pos"] != "bench" and all_players[target]["r_hit"] == 0:
						#Shoot at the target!
						all_players[target]["g_st"] = all_players[target]["g_st"] + 1
						stealing = 0
						if all_players[active]["team"] == "home":
							attack = die_roll("acc",all_players[active],h_team)
							dodge = die_roll("eva",all_players[target],a_team)
							if attack > dodge:
								game_log(all_players[active]["name"]+" hits "+all_players[target]["name"]+"!","t")
								h_team["points"] = h_team["points"] + 1
								all_players[active]["g_ph"] = all_players[active]["g_ph"] + 1
								all_players[target]["r_hit"] = 1
								break
							else:
								game_log(all_players[active]["name"]+" misses "+all_players[target]["name"]+"!","t")								
								break
						if all_players[active]["team"] == "away":
							attack = die_roll("acc",all_players[active],a_team)
							dodge = die_roll("eva",all_players[target],h_team)
							if attack > dodge:
								game_log(all_players[active]["name"]+" hits "+all_players[target]["name"]+"!","t")
								a_team["points"] = a_team["points"] + 1
								all_players[active]["g_ph"] = all_players[active]["g_ph"] + 1
								all_players[target]["r_hit"] = 1
								break
							else:
								game_log(all_players[active]["name"]+" misses "+all_players[target]["name"]+"!","t")								
								break
					target = target - 1					

				#If you can't find a target, take the flag
				if stealing == 1:
					game_log(all_players[active]["name"]+" has stolen the unprotected enemy flag and ended the round!","t")
					if all_players[active]["team"] == "home":
						game_log("The away team had no players to protect the flag","t")
						h_team["points"] = h_team["points"] + 4
					elif all_players[active]["team"] == "away":
						game_log("The home team had no players to protect the flag","t")
						a_team["points"] = a_team["points"] + 4
					break

		#Count remaining shots
		#print("end of shooting round")
		shots_remaining = 0
		for s in all_players:
			if s["r_hit"] == 1:
				s["r_shts"] = 0
			shots_remaining = shots_remaining + s["r_shts"]

		if shots_remaining == 0:
			game_log("No shots remaining","l")
			break
		#Choose next
		if active == len(all_players) - 1:
			active = 0
		else:
			active = active + 1

		#If not 
	#Clock Advance
	game_log("end of round "+str(clock),"t")
	game_log("Home: "+str(h_team["points"]),"t")
	game_log("Away: "+str(a_team["points"]),"t")
	clock = clock + 1



#################END OF GAME#################

#Final
game_log("FINAL SCORE:","t")
game_log("Home: "+str(h_team["points"]),"t")
game_log("Away: "+str(a_team["points"]),"t")

#Sort players for better stat view
#Stats
game_log("FINAL STATS:","t")
game_log("Player\t\tHits\tShots\tFlags\tShooting %\tPoints Earned\tHits Taken\tHit +/-","t")
for p in all_players:
	try:
		sp = p["g_ph"]/p["g_st"]
	except:
		sp = "NA"
	pp = p["g_ph"]+(p["g_fc"]*4)
	ppm = p["g_ht"]+(p["g_fc"]*4)
	game_log(p["name"]+":\t"+p["g_ph"]+"\t"+p["g_st"]+"\t"+p["g_fc"]+"\t"+sp+"\t"+pp+"\t"+p["g_ht"]+"\t"+ppm,"t")

# Money Earned
# Roll for gaining credits
# Credit maximum is determined by the fanbase size
# Credit minimum is determined by the fan experience
# Earn attempts at cash based on
# 90s rolled (Highlight Reel Plays)
# 10 for winning
# A number of bonus dice based on the marketeers knowledge
# D100 - KNO
# For each, roll a die based on fanbase tier:
# 1-5 for D4-D12
# Sum is the amount of credits earned
# Fan experience denotes a minimum level earned
# Pay players, staff, facilities, and drugs used
if h_team["points"] > a_team["points"]:
	h_cashrolls = 20+h_team["Lights"]

	if h_team["Marketeer"] != -1:
		h_cashrolls = h_cashrolls + (h_team["Marketeer"] - random.randint(0,99))

	if h_team["Fan_Cap"] == 1:
		h_cashtot = h_cashrolls * random.randint(1,4)
	elif h_team["Fan_Cap"] == 2:
		h_cashtot = h_cashrolls * random.randint(1,6)
	elif h_team["Fan_Cap"] == 3:
		h_cashtot = h_cashrolls * random.randint(1,8)
	elif h_team["Fan_Cap"] == 4:
		h_cashtot = h_cashrolls * random.randint(1,10)
	elif h_team["Fan_Cap"] == 5:
		h_cashtot = h_cashrolls * random.randint(1,12)

	a_cashrolls = a_team["Lights"]

	if a_team["Marketeer"] != -1:
		a_cashrolls = a_cashrolls + (a_team["Marketeer"] - random.randint(0,99))

	if a_team["Fan_Cap"] == 1:
		a_cashtot = a_cashrolls * random.randint(1,4)
	elif a_team["Fan_Cap"] == 2:
		a_cashtot = a_cashrolls * random.randint(1,6)
	elif a_team["Fan_Cap"] == 3:
		a_cashtot = a_cashrolls * random.randint(1,8)
	elif a_team["Fan_Cap"] == 4:
		a_cashtot = a_cashrolls * random.randint(1,10)
	elif a_team["Fan_Cap"] == 5:
		a_cashtot = a_cashrolls * random.randint(1,12)

elif h_team["points"] < a_team["points"]:
	h_cashrolls = h_team["Lights"]

	if h_team["Marketeer"] != -1:
		h_cashrolls = h_cashrolls + (h_team["Marketeer"] - random.randint(0,99))

	if h_team["Fan_Cap"] == 1:
		h_cashtot = h_cashrolls * random.randint(1,4)
	elif h_team["Fan_Cap"] == 2:
		h_cashtot = h_cashrolls * random.randint(1,6)
	elif h_team["Fan_Cap"] == 3:
		h_cashtot = h_cashrolls * random.randint(1,8)
	elif h_team["Fan_Cap"] == 4:
		h_cashtot = h_cashrolls * random.randint(1,10)
	elif h_team["Fan_Cap"] == 5:
		h_cashtot = h_cashrolls * random.randint(1,12)

	a_cashrolls = 20+a_team["Lights"]

	if a_team["Marketeer"] != -1:
		a_cashrolls = a_cashrolls + (a_team["Marketeer"] - random.randint(0,99))

	if a_team["Fan_Cap"] == 1:
		a_cashtot = a_cashrolls * random.randint(1,4)
	elif a_team["Fan_Cap"] == 2:
		a_cashtot = a_cashrolls * random.randint(1,6)
	elif a_team["Fan_Cap"] == 3:
		a_cashtot = a_cashrolls * random.randint(1,8)
	elif a_team["Fan_Cap"] == 4:
		a_cashtot = a_cashrolls * random.randint(1,10)
	elif a_team["Fan_Cap"] == 5:
		a_cashtot = a_cashrolls * random.randint(1,12)
# Else tie
else:
	h_cashrolls = h_team["Lights"]

	if h_team["Marketeer"] != -1:
		h_cashrolls = h_cashrolls + (h_team["Marketeer"] - random.randint(0,99))

	if h_team["Fan_Cap"] == 1:
		h_cashtot = h_cashrolls * random.randint(1,4)
	elif h_team["Fan_Cap"] == 2:
		h_cashtot = h_cashrolls * random.randint(1,6)
	elif h_team["Fan_Cap"] == 3:
		h_cashtot = h_cashrolls * random.randint(1,8)
	elif h_team["Fan_Cap"] == 4:
		h_cashtot = h_cashrolls * random.randint(1,10)
	elif h_team["Fan_Cap"] == 5:
		h_cashtot = h_cashrolls * random.randint(1,12)

	a_cashrolls = a_team["Lights"]

	if a_team["Marketeer"] != -1:
		a_cashrolls = a_cashrolls + (a_team["Marketeer"] - random.randint(0,99))

	if a_team["Fan_Cap"] == 1:
		a_cashtot = a_cashrolls * random.randint(1,4)
	elif a_team["Fan_Cap"] == 2:
		a_cashtot = a_cashrolls * random.randint(1,6)
	elif a_team["Fan_Cap"] == 3:
		a_cashtot = a_cashrolls * random.randint(1,8)
	elif a_team["Fan_Cap"] == 4:
		a_cashtot = a_cashrolls * random.randint(1,10)
	elif a_team["Fan_Cap"] == 5:
		a_cashtot = a_cashrolls * random.randint(1,12)

#See how fan experience saves them
#Calculate game cost:
	a_gamecost = a_team["Coach_Cost"]
	h_gamecost = h_team["Coach_Cost"]
	for p in all_players:
		if p["team"] == "home":
			h_gamecost = h_gamecost + p["g_cost"]
			if p["drug"] != "none":
				h_gamecost = h_gamecost + 1000
		if p["team"] == "away":
			a_gamecost = a_gamecost + p["g_cost"]
			if p["drug"] != "none":
				a_gamecost = a_gamecost + 1000

#Net totals
a_net = a_cashtot - a_gamecost
h_net = h_cashtot - h_gamecost

game_log("The away team earned "+a_net,"l")
game_log("The home team earned "+h_net,"l")


# Level Ups
for p in players:
	lurs = 0
	if p["team"] == "home":
		luas = p["exp"]
		while luas > 0:
			lu_att = die_roll("pot",p,h_team)
			if lu_att > 0:
				lurs = lurs + 1
			luas = luas - 1
	if p["team"] == "away":
		luas = p["exp"]
		while luas > 0:
			lu_att = die_roll("pot",p,a_team)
			if lu_att > 0:
				lurs = lurs + 1
			luas = luas - 1
	if lurs == 0:
		break
	#Set levelup set
	if p["per"] == "aggressive":
		lu_set = ["int","int","int","acc","acc","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "stoic":
		lu_set = ["int","acc","acc","acc","acc","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "reactive":
		lu_set = ["int","int","acc","eva","eva","eva","fit","fit","ego","ego","kno","kno"]
	elif p["per"] == "ambitious":
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","ego","ego","kno"]
	elif p["per"] == "eager":
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","kno","kno","kno"]
	else:
		lu_set = ["int","int","acc","acc","eva","eva","fit","fit","ego","ego","kno","kno"]
	while lurs > 0:
		this_lvl = random.choice(lu_set)
		if this_lvl == "int":
			p["s_int"] = p["s_int"] + 1
			game_log(p["name"]+" leveled up initiative!","l")
		elif this_lvl == "acc":
			p["s_acc"] = p["s_acc"] + 1
			game_log(p["name"]+" leveled up accuracy!","l")
		elif this_lvl == "eva":
			p["s_eva"] = p["s_eva"] + 1
			game_log(p["name"]+" leveled up evasion!","l")
		elif this_lvl == "fit":
			p["s_fit"] = p["s_fit"] + 1
			game_log(p["name"]+" leveled up fitness!","l")
		elif this_lvl == "ego":
			p["s_ego"] = p["s_ego"] + 1
			game_log(p["name"]+" leveled up ego!","l")
		elif this_lvl == "kno":
			p["s_kno"] = p["s_kno"] + 1
			game_log(p["name"]+" leveled up knowledge!","l")
		lurs = lurs - 1

#Injuries
for p in players:
	inrc = 0
	if p["team"] == "home":
		inrk = p["fat"]
		while inrk > 0:
			lu_att = die_roll("fit",p,h_team)
			if lu_att > 0:
				inrc = inrc + 1
			inrk = inrk - 1
	if p["team"] == "away":
		inrk = p["fat"]
		while inrk > 0:
			lu_att = die_roll("fit",p,a_team)
			if lu_att > 0:
				inrc = inrc + 1
			inrk = inrk - 1
	if inrc == 0:
		break
	total_in = 0
	while inrc > 0:
		#Roll assuming D10 for now
		total_in = total_in + random.randint(1,10)
		inrc = inrc - 1
	game_log(p["name"] + " is injured for "+total_in+" games","l")
	p["inj"] = p["inj"] + total_in

#Save
#Add to all time stats?
a_load.close()
h_load.close()
l_load.close()