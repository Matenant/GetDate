DROP TABLE IF EXISTS users;

-- CREATE TABLE users (
--     users_id int auto_increment,
--     primary key(users_id),
--     name varchar(255) not null,
--     password varchar(255) not null
-- );
DROP TABLE IF EXISTS reponse;
DROP TABLE IF EXISTS proposition;
DROP TABLE IF EXISTS activite;

CREATE TABLE activite (
    activite_id int auto_increment,
    primary key(activite_id),
    nom varchar(255) not null
);

CREATE TABLE proposition (
    proposition_id int auto_increment,
    primary key(proposition_id),
    nom varchar(255) not null,
    activite_nom varchar(255) not null,
    activite_id int,
    date datetime not null,
    proposition_uuid UUID not null,
    CONSTRAINT fk_activite_id FOREIGN KEY (activite_id) REFERENCES activite(activite_id)
);

CREATE TABLE reponse (
    reponse_id int auto_increment,
    primary key(reponse_id),
    activite_rep_nom varchar(255) not null,
    activite_rep_id int,
    proposition_id int,
    date_rep datetime not null,
    CONSTRAINT fk_proposition_id FOREIGN KEY (proposition_id) REFERENCES proposition(proposition_id),
    CONSTRAINT fk_activite_rep_id FOREIGN KEY (activite_rep_id) REFERENCES activite(activite_id)
);