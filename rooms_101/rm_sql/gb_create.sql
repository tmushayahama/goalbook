drop database goalbook;
create database goalbook DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON goalbook.* to 'rooms_101'@'localhost' WITH GRANT OPTION;
