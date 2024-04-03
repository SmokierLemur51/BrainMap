create table if not exists creator (
	id integer primary key autoincrement,
	created_at datetime default current_timestamp,
	updated_at datetime,
	deleted_at datetime,
	name varchar(100)
);

create table if not exists journal (
	id integer primary key autoincrement,
	created_at datetime default current_timestamp,
	updated_at datetime,
	deleted_at datetime,
	creator_id integer, 
	title varchar(100), -- name of the journal
	description varchat(500),
	foreign key(creator_id) references creator(id)
);

create trigger update_timestamp
after update on journal for each row;