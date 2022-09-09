import streamlit as st
import pandas as pd
import numpy as np


def get_player_details(player_id):

    """
    
    """

    player_df = pd.read_csv('data/fifa 22/players_22.csv', low_memory=False)
    

  
    player_df.set_index('sofifa_id',inplace=True)

    player = player_df.loc[player_id]

    print(player)

    face = player['player_face_url']
    club = player['club_logo_url']
    value = player['value_eur']
    salary = player['wage_eur']

    return {'face':face,'club':club,'value':value,'salary':salary}




def get_players():

    player_df = pd.read_csv('data/player_abilities.csv', low_memory=False)
    player_ids = list(player_df['sofifa_id'])
    player_names = list(player_df['short_name']+','+player_df['overall'].astype('str'))

    
    player_dict = dict(zip(player_names, player_ids))

    return player_dict

    
def get_similiar_players(player,player_count=5):
    """
    find top 5 similiar players
    i/p: player_id
    """

    player_name = player.split(',')[0]
    overall = player.split(',')[1]

    print(player_name,2,overall)
    

    PCA_components = pd.read_csv('models/pca_result.csv', low_memory=False)
    pl_df          = pd.read_csv('models/pca_result.csv', low_memory=False)
    
    print(pl_df.head())

    playerA_id = pl_df[(pl_df['name']==str(player_name)) & (pl_df['overall']==int(overall))]['sofifa_id'].item()

    print(playerA_id,2)

    pl_df.set_index('sofifa_id',inplace=True)
    PCA_components.set_index('sofifa_id',inplace=True)

    n_clusters = list(PCA_components['pred_labels'].unique())

    cluster_dict = {i: pl_df.index[PCA_components['pred_labels']==i].tolist() for i in range(len(n_clusters))}

  
    # find the cluster the player belongs
    cluster = PCA_components.loc[playerA_id]['pred_labels']

    # get the features of playerA
    playerA_data = PCA_components.loc[playerA_id].head()

    
    # get the other players in the same cluster
    cluster_indices = cluster_dict[cluster]


    # get the other players in the same cluster
    cluster_indices = cluster_dict[cluster]

    # initialise a temp dictionary to store player ids and distances
    dist_dict={}

    # iterate through each player in the cluster
    for player_id in cluster_indices:

        if(player_id != playerA_id):

        
            playerB_data = PCA_components.loc[player_id].head()
            dist = np.linalg.norm(playerA_data-playerB_data)
            dist_dict[player_id]=dist.round(4)
        
    
    dist_df = pd.DataFrame(columns=['id','distance'])

    dist_df['id'] = dist_dict.keys()
    dist_df['distance'] = dist_dict.values()
    dist_df.sort_values('distance',inplace=True)

    similiar_players = dist_df.head(player_count)
    
    name_list=[]

    for id in list(similiar_players['id']):
        name_list.append(pl_df.loc[id]['name'])

    similiar_players['name'] =name_list

    print(similiar_players)

    return similiar_players

    





if __name__ == '__main__':

    st.title('Welcome To Player Replacement Application')

    instructions = """
       Enter the name of the player you want to replace and the model will give you a list of similiar players based on their abilities and skill
        """
    st.write(instructions)

    player_dict = get_players()


    data_split_names = list(player_dict.keys())


    gender = st.sidebar.radio("Select gender",('Male', 'Female'))

    player_name = st.sidebar.selectbox(
            "Select Players", data_split_names
            )

    # value = st.selectbox("players", data_split_names, format_func=lambda x: data_split_names[x])

    player_id = player_dict[player_name]

    print(player_name,':',player_id)

    if st.sidebar.button('Find Players'):

        print(player_name)

        similiar_players = get_similiar_players(player=player_name)

        player_info = get_player_details(player_id)

        print(player_info['face'])
        st.title("Here is the player you've selected")
        # resized_image = img.resize((336, 336))
        st.image(player_info['face'])
        st.title("Here are the five most similiar players")

        st.table(similiar_players[['name','distance']])

        instructions = """
                *Lower the score, Greater the similarity
            """
        st.write(instructions)

   
        
