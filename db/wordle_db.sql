CREATE TABLE users(
        user_id                 SERIAL PRIMARY KEY,
        username                TEXT NOT NULL,
        password                TEXT NOT NULL,
        email                   TEXT NOT NULL      
);

CREATE TABLE wordle_stats(
        id                       SERIAL PRIMARY KEY,
        user_id                  int NOT NULL,
        number_of_games_played   int NOT NULL,
        number_of_games_won      int NOT NULL,
        win_percentage           Float,
        total_points             int NOT NULL,
        CONSTRAINT user_Id FOREIGN KEY (user_id) REFERENCES users(user_id)
);