import pandas as pd
import pickle

def predict_runs_scored(OBP,SLG):
    with open('lcm/models/linear_classification_rs.pickle','rb') as f:
        linear_cls_RS = pickle.load(f)
    
    return linear_cls_RS.predict([[OBP,SLG]])

def predict_runs_allowed(OOBP,OSLG):
    
    with open('lcm/models/linear_classification_ra.pickle','rb') as f:
        linear_cls_RA = pickle.load(f)
    print("++++++++++++++++++++++++++++")
    print(linear_cls_RA.predict([[OOBP,OSLG]]))
    
    return linear_cls_RA.predict([[OOBP,OSLG]])  #, coeff_df


def predict_matches_win(rs,ra):
    with open('lcm/models/linear_classification_diff.pickle','rb') as f:
        linear_cls_diff = pickle.load(f)
        
    runs = rs-ra
    
    total_wins_season = linear_cls_diff.predict([[runs]])
         
    if total_wins_season >= 100:   
        percentage_season_qualify = 100   # 95 game-94.73% , 85 games-77.27%, 80 game - 6.6%, 0-80 games 0%
    elif total_wins_season >= 95 and total_wins_season < 100:
        percentage_season_qualify = 94.73
    elif total_wins_season >= 85 and total_wins_season < 95:
        percentage_season_qualify = 77.27
    elif total_wins_season >= 80 and total_wins_season < 85:
        percentage_season_qualify = 6.66
    else:
        percentage_season_qualify = 0
    
    return total_wins_season, percentage_season_qualify
    
    
    