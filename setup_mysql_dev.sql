-- Creates database instakush_dev_db
CREATE DATABASE IF NOT EXISTS instakush_dev_db;
USE instakush_dev_db;
CREATE USER IF NOT EXISTS 'instakush_dev'@'localhost';
SET PASSWORD FOR 'instakush_dev'@'localhost' = 'instakush_dev_pwd';
GRANT ALL PRIVILEGES ON instakush_dev_db.* TO 'instakush_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'instakush_dev'@'localhost';
