#!/bin/bash

#read -p "database name: " database_name
#read -p "admin name: " admin_name
#read -p "admin password: " admin_pass

sudo -u postgres psql << END_OF_SCRIPT
drop database mochale;
drop role mochale_admin;
create database mochale;
create user mochale_admin with password 'admin';
alter role mochale_admin set client_encoding to 'utf8';
alter role mochale_admin set default_transaction_isolation to 'read committed';
alter role mochale_admin set timezone to 'UTC';
grant all privileges on database mochale to mochale_admin;
\q

END_OF_SCRIPT
