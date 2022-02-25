CREATE TABLE users(
        user_id                 SERIAL PRIMARY KEY,
        username                TEXT NOT NULL,
        email                   TEXT NOT NULL,
        password                TEXT NOT NULL,      
        number_of_games_played   int NOT NULL,
        number_of_games_won      int NOT NULL,
        win_percentage           Float,
        total_points             int NOT NULL
);

INSERT INTO users(username, email, password, number_of_games_played, number_of_games_won, win_percentage, total_points) VALUES
    ('Borneo', 'bornakevin1@gmail.com', 'Tehran14!', 0, 0, 0.0, 0);