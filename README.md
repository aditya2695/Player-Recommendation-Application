

<h1> Player Recommendation Application :soccer: </h1>



### :seedling: Introduction 

<p>
The Player Recommendation Application is a project that aims to find the right footballer to replace another player. Football clubs often struggle to replace key players when they depart, and this can lead to excessive spending on new acquisitions that fail to make an impact. For example, FC Barcelona spent over 400 million pounds on just three player acquisitions in 2018 and 2019 to replace Neymar and Iniesta, but all three failed to create the desired impact. Similarly, Manchester United has spent over £1 billion and has struggled over the past decade.

The project aims to find solutions to the following problems:

</p>

<ol>
    <li>	Let's say player X departs a team, and the team needs a player who is similar to the player who is departing.</li>
    <li>	Clubs occasionally fail to sign their top transfer targets for a variety of reasons. Then they would have to choose the best alternate signing.</li>
    <li>	Coaches occasionally have to select a versatile player to replace one who is currently playing in a different position owing to an injury or another circumstance. </li>
</ol>

<img src="https://cdn.mos.cms.futurecdn.net/y8Z3cKCQ6cZgTZNh5TeKgX.jpg">

## 💻 Technologies Used

    Python
    Pandas
    NumPy
    Scikit-learn
    t-SNE
    KMeans
    Streamlit

### 📚 Dataset

The project uses the FIFA 21 dataset, which includes detailed player attributes such as skill moves, passing, shooting, and dribbling. The dataset also includes physical attributes such as height, weight, and age.

### Feature Engineering
<ul>
<li>Positional Versatility was considered, and a separate column was added to include no of positions</li>
<li>Work rate column was divided into 2 new columns</li>
<li>Label encoded columns 'preferred_foot', 'work_rate1', 'work_rate2', 'first_position','body_type'</li>
<li>27 player positions were identified </li>
<li>Filled the player abilities stats will null values with 0</li>
<li>Finally Shortlisted 50 player columns</li>
</ul>

### Modelling
<ul>
<li>For modelling purposes, unsupervised clustering approaches were used.</li>
<li>KMeans, KMeans(with PCA), KMeans(with t-SNE), Hierarchical Clustering and DBSCAN were used to cluster the players.</li>
<li>Separate modelling was done for male and female players</li>
</ul>

### :book: Instructions

1. Datasets stored in data directory
2. First run EDA notebooks and then run modelling notebooks for male and female players
3. After EDA two files are saved as 'data/player_abilities.csv' and 'data/female_player_abilities.csv'. These two files are used for modelling
4. After modelling the results are saved as 'models/male_pca_result.csv' and 'models/female_pca_result.csv' respectively.
5. The app_home.py and tests.py of  the streamlit app file in the root directory uses the data and models directories.

### :runner: Running the Application

<a href="https://aditya2695-player-recommendation-application-app-home-eu6qy9.streamlitapp.com/">Player Recommendation Application</a>

1. Go to Root directory and activate streamlit environment
2. streamlit app_home.py

<img src="images/app_screen.png" width="600">
<br>
<br>
<table>
<tr>
    <th>3D cluster plot of dribbling,passing and overall</th>
    <th>Silhoutte score for different k values</th>
</tr>
<tr>
    <td><img src="images/male_pca_cluster1.png"></td>
    <td><img src="images/metrics.png"></td>
</tr>

<tr>
    <th>Heirarchical Cluster Dendrogram</th>
    <th></th>
</tr>
<tr>
    <td><img src="images/dendrogram.png" width="600"></td>
    <td></td>
</tr>

</table>


### :microscope: Testing the Application

1. Go to Root directory and activate streamlit environment
2. python tests.py

### Credits
<a href="https://www.flaticon.com/free-icons/soccer-player" title="soccer player icons">Soccer player icons created by Freepik - Flaticon</a>

