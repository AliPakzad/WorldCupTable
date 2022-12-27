"""
input:

2-2
2-1
1-2
2-2
3-1
2-1

Iran - Spain
Iran - Portugal
Iran - Morocco
Spain - Portugal
Spain - Morocco
Portugal - Morocco

output:

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3

"""

Spain ={'name': 'Spain', 'wins':0 , 'loses':0 , 'draws':0 , 'goal_difference':0 , 'points':0}
Iran = {'name': 'Iran', 'wins':0 , 'loses':0 , 'draws':0 , 'goal_difference':0 , 'points':0}
Portugal = {'name': 'Portugal', 'wins':0 , 'loses':0 , 'draws':0 , 'goal_difference':0 , 'points':0}
Morocco = {'name': 'Morocco', 'wins':0 , 'loses':0 , 'draws':0 , 'goal_difference':0 , 'points':0}

Iran_Spain = input().split('-')
goal_difference = int(Iran_Spain[0]) - int(Iran_Spain[1])

if goal_difference > 0:
    Iran['wins'] += 1
    Iran['goal_difference'] += goal_difference
    Iran['points'] += 3
    Spain['loses'] += 1
    Spain['goal_difference'] -= goal_difference
elif goal_difference == 0:
    Iran['draws'] += 1
    Iran['points'] += 1
    Spain['draws'] += 1
    Spain['points'] += 1
else:
    Iran['loses'] += 1
    Iran['goal_difference'] += goal_difference
    Spain['points'] += 3
    Spain['wins'] += 1
    Spain['goal_difference'] -= goal_difference

Iran_Portugal = input().split('-')
goal_difference = int(Iran_Portugal[0]) - int(Iran_Portugal[1])

if goal_difference > 0:
    Iran['wins'] += 1
    Iran['goal_difference'] += goal_difference
    Iran['points'] += 3
    Portugal['loses'] += 1
    Portugal['goal_difference'] -= goal_difference
elif goal_difference == 0:
    Iran['draws'] += 1
    Iran['points'] += 1
    Portugal['draws'] += 1
    Portugal['points'] += 1
else:
    Iran['loses'] += 1
    Iran['goal_difference'] += goal_difference
    Portugal['points'] += 3
    Portugal['wins'] += 1
    Portugal['goal_difference'] -= goal_difference


Iran_Morocco = input().split('-')
goal_difference = int(Iran_Morocco[0]) - int(Iran_Morocco[1])

if goal_difference > 0:
    Iran['wins'] += 1
    Iran['goal_difference'] += goal_difference
    Iran['points'] += 3
    Morocco['loses'] += 1
    Morocco['goal_difference'] -= goal_difference
elif goal_difference == 0:
    Iran['draws'] += 1
    Iran['points'] += 1
    Morocco['draws'] += 1
    Morocco['points'] += 1
else:
    Iran['loses'] += 1
    Iran['goal_difference'] += goal_difference
    Morocco['points'] += 3
    Morocco['wins'] += 1
    Morocco['goal_difference'] -= goal_difference

Spain_Portugal = input().split('-')
goal_difference = int(Spain_Portugal[0]) - int(Spain_Portugal[1])

if goal_difference > 0:
    Spain['wins'] += 1
    Spain['goal_difference'] += goal_difference
    Spain['points'] += 3
    Portugal['loses'] += 1
    Portugal['goal_difference'] -= goal_difference
elif goal_difference == 0:
    Spain['draws'] += 1
    Spain['points'] += 1
    Portugal['draws'] += 1
    Portugal['points'] += 1
else:
    Spain['loses'] += 1
    Spain['goal_difference'] += goal_difference
    Portugal['points'] += 3
    Portugal['wins'] += 1
    Portugal['goal_difference'] -= goal_difference

Spain_Morocco = input().split('-')
goal_difference = int(Spain_Morocco[0]) - int(Spain_Morocco[1])

if goal_difference > 0:
    Spain['wins'] += 1
    Spain['goal_difference'] += goal_difference
    Spain['points'] += 3
    Morocco['loses'] += 1
    Morocco['goal_difference'] -= goal_difference
elif goal_difference == 0:
    Spain['draws'] += 1
    Spain['points'] += 1
    Morocco['draws'] += 1
    Morocco['points'] += 1
else:
    Spain['loses'] += 1
    Spain['goal_difference'] += goal_difference
    Morocco['points'] += 3
    Morocco['wins'] += 1
    Morocco['goal_difference'] -= goal_difference

Portugal_Morocco = input().split('-')
goal_difference = int(Portugal_Morocco[0]) - int(Portugal_Morocco[1])

if goal_difference > 0:
    Portugal['wins'] += 1
    Portugal['goal_difference'] += goal_difference
    Portugal['points'] += 3
    Morocco['loses'] += 1
    Morocco['goal_difference'] -= goal_difference
elif goal_difference == 0:
    Portugal['draws'] += 1
    Portugal['points'] += 1
    Morocco['draws'] += 1
    Morocco['points'] += 1
else:
    Portugal['loses'] += 1
    Portugal['goal_difference'] += goal_difference
    Morocco['points'] += 3
    Morocco['wins'] += 1
    Morocco['goal_difference'] -= goal_difference

groupList =[Spain , Portugal ,Morocco , Iran]
sortedList1 = sorted(groupList, key=lambda i: (i['name']))
sortedList2 = sorted(sortedList1, key=lambda i: (i['wins'], i['points']),reverse=True)

for team in sortedList2:
    print(f"{team['name']}  wins:{team['wins']} , loses:{team['loses']} , draws:{team['draws']} , goal difference:{team['goal_difference']} , points:{team['points']}")
