DROP TABLE Distributors CASCADE CONSTRAINTS;
DROP TABLE Movies CASCADE CONSTRAINTS;
DROP TABLE Actors;
DROP TABLE DomesticMovie CASCADE CONSTRAINTS;
DROP TABLE ForeignMovie;
DROP TABLE Genres;
DROP TABLE Critics CASCADE CONSTRAINTS;
DROP TABLE Reviews;
DROP TABLE Awards CASCADE CONSTRAINTS;
DROP TABLE Nominations;
CREATE TABLE Distributors (
    DNum int PRIMARY KEY,
    DName varchar(255),
    DState varchar(255),
    DCity varchar(255),
    DAddress varchar(255),
    DZip int
);
CREATE TABLE Movies (
    Movie_id int PRIMARY KEY,
    Movie_name varchar(255),
    Director varchar(255),
    Run_time int,
    Release_date varchar(255),
    Rating varchar(255),
    DNum int,
    FOREIGN KEY (DNum)
    REFERENCES Distributors(DNum)
);
CREATE TABLE Actors (
    Movie_id int,
    Actor_name varchar(255),
    PRIMARY KEY (Movie_id, Actor_name),
    FOREIGN KEY (Movie_id)
    REFERENCES Movies(Movie_id)
);
CREATE TABLE DomesticMovie (
    Movie_id int PRIMARY KEY,
    Funniness int,
    Movie_description varchar(255),
    FOREIGN KEY (Movie_id)
    REFERENCES Movies(Movie_id)
);
CREATE TABLE ForeignMovie (
    Movie_id int PRIMARY KEY,
    English_subtitles int,
    Movie_language varchar(255),
    FOREIGN KEY (Movie_id)
    REFERENCES Movies(Movie_id)
);
CREATE TABLE Genres (
    Movie_id int,
    Genre varchar(255),
    FOREIGN KEY (Movie_id)
    REFERENCES DomesticMovie(Movie_id)
);
CREATE TABLE Critics (
    CNumber int PRIMARY KEY,
    CName varchar(255)
);
CREATE TABLE Reviews (
    CNumber int,
    Movie_id int,
    CEval int,
    FOREIGN KEY (CNumber)
    REFERENCES Critics(CNumber),
    FOREIGN KEY (Movie_id)
    REFERENCES Movies(Movie_id)
);
CREATE TABLE Awards (
    AName varchar(255) PRIMARY KEY,
    AYear int,
    AWin varchar(255)
);
CREATE TABLE Nominations (
    AName varchar(255),
    Movie_id int,
    AWon int,
    FOREIGN KEY (AName)
    REFERENCES Awards(AName),
    FOREIGN KEY (Movie_id)
    REFERENCES Movies(Movie_id)
);
INSERT INTO Distributors
VALUES (7033723275, 'Chris Tato Ltd.', 'VA', 'Clifton', '12040 Rose Hall Drive', 20124);
INSERT INTO Distributors
VALUES (5712172670, 'Chris Tato Inc.', 'CA', 'Los Angeles', 'Somewhere in LA', 50082);
INSERT INTO Distributors
VALUES (8005882600, 'Chris T. Monsters Inc.', 'WI', 'Cheeseville', 'Another Random Location', 80009);
INSERT INTO Distributors
VALUES (1112223333, 'CAT Corp.', 'CA', 'Los Angeles', 'Somewhere Different in LA', 44444);
INSERT INTO Distributors
VALUES (5556667777, 'A24', 'MI', 'Beloxi', 'The Hospital Where Chris Was Born', 88888);


INSERT INTO Awards
VALUES ('Oscars Award', 2018, 'Moonlight');
INSERT INTO Awards
VALUES ('Big Movie Award', 2014, 'Transformers 2: Darkside of the Moon');
INSERT INTO Awards
VALUES ('Moon Award', 2014, 'Lion King');
INSERT INTO Awards
VALUES ('Foreign Award', 2018, 'The Big Frenchowski');
INSERT INTO Awards
VALUES ('Best Bowling Movie', 2048, 'The Big Frenchowski');
INSERT INTO Awards
VALUES ('Coolest Robots Award', 2025, 'Transformers 2: Darkside of the Moon');

INSERT INTO Critics
VALUES (7033077703, 'Roger Ebert');
INSERT INTO Critics
VALUES (4444444444, 'Chris Tato');
INSERT INTO Critics
VALUES (0987654321, 'Garfield');

INSERT INTO Movies
VALUES (001, 'Moonlight', 'Jacque Cousteau', 120, 'March 23rd 2007', 'PG-13', 7033723275);
INSERT INTO ForeignMovie
VALUES (001, 1, 'French');
INSERT INTO Actors
VALUES (001, 'Steve Irwin');
INSERT INTO Actors
VALUES (001, 'Green Power Ranger');

INSERT INTO Movies
VALUES (002, 'Transformers 2: Darkside of the Moon', 'Michael Bay', 160, 'May 18th 2015', 'PG-13', 5712172670);
INSERT INTO DomesticMovie
VALUES (002, 2, 'Romance');
INSERT INTO Genres
VALUES (002, 'Drama');
INSERT INTO Genres
VALUES (002, 'Action');
INSERT INTO Genres
VALUES (002, 'Horror');
INSERT INTO Genres
VALUES (002, 'Comedy');
INSERT INTO Actors
VALUES (002, 'Shia Labouef');
INSERT INTO Actors
VALUES (002, 'Megan Fox');

INSERT INTO Movies
VALUES (003, 'Lion King', 'John Woo', 160, 'August 25th 1998', 'PG', 5712172670);
INSERT INTO DomesticMovie
VALUES (003, 1, NULL);
INSERT INTO Genres
VALUES (003, 'Comedy');
INSERT INTO Genres
VALUES (003, 'Action');
INSERT INTO Actors
VALUES (003, 'Pauly Shore');
INSERT INTO Actors
VALUES (003, 'John Oliver');

INSERT INTO Movies
VALUES (004, 'The Big Frenchowski', 'The Dude', 130, 'January 11th 2221', 'PG', 1112223333);
INSERT INTO ForeignMovie
VALUES (004, 1, 'French');
INSERT INTO Actors
VALUES (004, 'The Dude');
INSERT INTO Actors
VALUES (004, 'Joe Mama');
INSERT INTO Actors
VALUES (004, 'Paul Beach');
INSERT INTO Actors
VALUES (004, 'Ru Paul');
INSERT INTO Actors
VALUES (004, 'French-Man McGee');



INSERT INTO Movies
VALUES (005, 'You, Me, and Duprea', 'Duprea', 200, 'May 1st 2001', 'R', 8005882600);
INSERT INTO ForeignMovie
VALUES (005, 1, 'German');
INSERT INTO Actors
VALUES (005, 'You');
INSERT INTO Actors
VALUES (005, 'Me');
INSERT INTO Actors
VALUES (005, 'Duprea');


INSERT INTO Movies
VALUES (006, 'Scary Movie', 'The Scream', 120, 'November 15th 1998', 'PG-13', 5556667777);
INSERT INTO DomesticMovie
VALUES (006, 2, NULL);
INSERT INTO Genres
VALUES (006, 'Comedy');
INSERT INTO Genres
VALUES (006, 'Horror');
INSERT INTO Actors
VALUES (006, 'Bob Sagat');
INSERT INTO Actors
VALUES (006, 'A Guy in a Scream Mask');

INSERT INTO Movies
VALUES (007, 'Scary Movie 2: Only Scares', 'Scream Jr.', 90, 'June 6th 2005', 'R', 5556667777);
INSERT INTO DomesticMovie
VALUES (007, NULL, NULL);
INSERT INTO Genres
VALUES (007, 'Horror');
INSERT INTO Actors
VALUES (007, 'Shaq');
INSERT INTO Actors
VALUES (007, 'Tony the Tiger');

INSERT INTO Movies
VALUES (008, 'Pauly Shore and the Fun-Time Extravaganza', 'Pauly Shore', 15, 'July 4th 2020', 'X', 5712172670);
INSERT INTO DomesticMovie
VALUES (008, 1, NULL);
INSERT INTO Genres
VALUES (008, 'Comedy');
INSERT INTO Actors
VALUES (008, 'Snooki');
INSERT INTO Actors
VALUES (008, 'Joe Mama');
INSERT INTO Actors
VALUES (008, 'Pauly Shore');

INSERT INTO Movies
VALUES (009, 'Lion King 1 and 1/2', 'John Woo', 90, 'September 12th 1999', 'PG-13', 5556667777);
INSERT INTO DomesticMovie
VALUES (009, 5, NULL);
INSERT INTO Genres
VALUES (009, 'Comedy');
INSERT INTO Genres
VALUES (009, 'Action');
INSERT INTO Actors
VALUES (009, 'Timon');
INSERT INTO Actors
VALUES (009, 'Pumba');

INSERT INTO Movies
VALUES (010, 'Your Name.', 'John Woo', 160, 'December 7th 2017', 'PG-13', 1112223333);
INSERT INTO ForeignMovie
VALUES (010, 1, 'Japanese');
INSERT INTO Actors
VALUES (010, 'Taki Tachibana');
INSERT INTO Actors
VALUES (010, 'Mitsuha Miyamizu');



INSERT INTO Nominations
VALUES ('Oscars Award', 001, 1);
INSERT INTO Nominations
VALUES ('Big Movie Award', 002, 1);
INSERT INTO Nominations
VALUES ('Moon Award', 003, 1);
INSERT INTO Nominations
VALUES ('Foreign Award', 004, 1);
INSERT INTO Nominations
VALUES ('Foreign Award', 005, 0);
INSERT INTO Nominations
VALUES ('Foreign Award', 010, 0);
INSERT INTO Nominations
VALUES ('Coolest Robots Award', 002, 1);


INSERT INTO Reviews
VALUES (7033077703, 001, 3);
INSERT INTO Reviews
VALUES (7033077703, 007, 3);
INSERT INTO Reviews
VALUES (7033077703, 003, 5);
INSERT INTO Reviews
VALUES (7033077703, 009, 3);
INSERT INTO Reviews
VALUES (7033077703, 004, 2);
INSERT INTO Reviews
VALUES (7033077703, 005, 5);
INSERT INTO Reviews
VALUES (7033077703, 010, 5);
INSERT INTO Reviews
VALUES (4444444444, 002, 3);
INSERT INTO Reviews
VALUES (4444444444, 003, 5);
INSERT INTO Reviews
VALUES (4444444444, 008, 3);
INSERT INTO Reviews
VALUES (4444444444, 004, 2);
INSERT INTO Reviews
VALUES (4444444444, 005, 5);
INSERT INTO Reviews
VALUES (4444444444, 010, 5);
INSERT INTO Reviews
VALUES (0987654321, 005, 5);
INSERT INTO Reviews
VALUES (0987654321, 006, 5);
INSERT INTO Reviews
VALUES (0987654321, 010, 5);


SELECT DName
FROM Distributors
WHERE DCity = 'Los Angeles';

SELECT Movie_name, Movie_language
FROM Movies, ForeignMovie, Nominations, Awards
WHERE Movies.Movie_id = ForeignMovie.Movie_id
AND Movies.Movie_id = Nominations.Movie_id
AND Nominations.AName = Awards.AName
AND Awards.AYear = 2018;

SELECT DISTINCT Director
FROM Distributors, Movies, DomesticMovie, Genres
WHERE Distributors.DNum = Movies.DNum
AND Distributors.DName = 'A24'
AND Movies.Movie_id = DomesticMovie.Movie_id
AND 'Horror' = ANY(SELECT Genre FROM Genres WHERE DomesticMovie.Movie_id = Genres.Movie_id);

SELECT DISTINCT Movie_name, run_time, release_date
FROM Movies, DomesticMovie, Actors
WHERE Movies.Movie_id = DomesticMovie.Movie_id
AND DomesticMovie.funniness = 1
AND 'Pauly Shore' = ANY(SELECT Actor_name FROM ACTORS WHERE Movies.Movie_id = Actors.Movie_id);

SELECT DISTINCT Movie_Name
FROM Movies, Reviews, Critics, DomesticMovie, Genres
WHERE Movies.Movie_id = Reviews.Movie_id
AND Movies.Director = 'John Woo'
AND Reviews.CNumber = Critics.CNumber
AND Critics.CName = 'Roger Ebert'
AND Movies.Movie_id = DomesticMovie.Movie_id
AND 'Action' = ANY(SELECT Genre FROM Genres WHERE DomesticMovie.Movie_id = Genres.Movie_id);

SELECT DISTINCT Actor_name
FROM Movies, Nominations, Awards, Actors
WHERE Movies.Movie_id = Actors.Movie_id
AND Movies.Movie_id = Nominations.Movie_id
AND Nominations.AName = Awards.AName
AND (SELECT COUNT (AWin) FROM Awards GROUP BY AWin HAVING AWIn = Movies.Movie_name) >= 2;

SELECT COUNT (DISTINCT Movies.Movie_id)
FROM Movies, Reviews
WHERE 5 = (SELECT AVG (CEval) FROM Reviews WHERE Movies.Movie_id = Reviews.Movie_id);

SELECT DISTINCT Movie_name
FROM Movies m
WHERE NOT EXISTS (SELECT Movie_name FROM Nominations WHERE m.Movie_id = Nominations.Movie_id);

SELECT DISTINCT Movie_name
FROM Movies m
WHERE NOT EXISTS (SELECT CNumber FROM Critics c 
WHERE NOT EXISTS (SELECT * FROM Reviews r WHERE m.Movie_id = r.Movie_id AND r.CNumber = c.CNumber));