-- create a database name meme_dev_db
CREATE DATABASE IF NOT EXISTS meme_dev_db;
-- drops user if database exists
-- DROP USER IF EXISTS 'meme_dev'@'localhost';
-- creates a user with user:meme_dev@localhost with pass meme_dev_pwd
CREATE USER 'meme_dev'@'localhost' IDENTIFIED BY 'meme_dev_pwd';
-- if user root@localhost unable to grant priv
-- http://stackoverflow.com/questions/21714869/error-1044-42000-access-denied-for-root-with-all-privileges
GRANT SELECT ON performance_schema.* TO 'meme_dev'@'localhost';
-- grant user hbnb_dev all privileges to database meme_dev_db
GRANT ALL PRIVILEGES ON meme_dev_db.* TO 'meme_dev'@'localhost';
