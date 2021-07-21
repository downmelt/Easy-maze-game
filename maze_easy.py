from abc import get_cache_token
import random

player_coordinates = [random.randrange(0,5),random.randrange(0,5)]      #プレイヤーの初期座標生成
goal_coordinates = [random.randrange(0,5),random.randrange(0,5)]        #ゴールの初期座標生成
distance = 0                                                            #プレイヤーからゴールまでの最短距離
direction = ""                                                          #進む方向
select_direction = ""                                                   #選択できる方向

while player_coordinates == goal_coordinates :
    goal_coordinates = [random.randrange(0,5),random.randrange(0,5)]    #プレイヤーとゴールの座標被り対策

while player_coordinates != goal_coordinates :
    select_direction = "どの方位に進みますか？("
    distance = abs(player_coordinates[0] - goal_coordinates[0]) + abs(player_coordinates[1] - goal_coordinates[1])  #プレイヤーからゴールまでの最短距離                                  
    print("ゴールまでの最短距離は",distance,"マス、現在地は",player_coordinates,"です")

    if player_coordinates[0] < 5 :                                      #進める方向を表示する処理
        select_direction += "1:東"
    if player_coordinates[0] > 0 :
        if player_coordinates[0] < 5 :
            select_direction += ","
        select_direction += "2:西"
    if player_coordinates[1] < 5 :
        select_direction += ",3:南"
    if player_coordinates[1] > 0 :
        select_direction += ",4:北"
    select_direction += ")"

    direction = int(input(select_direction))   

    if direction == 1 and player_coordinates[0] < 5 :                   #プレイヤーの移動処理
        player_coordinates[0] += 1
    elif direction == 2 and player_coordinates[0] > 0 :
        player_coordinates[0] -= 1
    elif direction == 3 and player_coordinates[1] < 5 :
        player_coordinates[1] += 1
    elif direction == 4 and player_coordinates[1] > 0:
        player_coordinates[1] -= 1
    elif direction < 1 or direction > 4 :
        print("1～4を入力してください")
    else :
        print("その方向にはいけません")

print("ゴールしました。")