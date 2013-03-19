drop database rm;
create database rm DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON rm.* to 'room_101'@'localhost' WITH GRANT OPTION;
use rm;
create table rm_user (
	id                      int 		 not null,
	gender 		 	char(1) 	 not null,
	primary key(id)
);
create table rm_task_type (
	id 			int 			auto_increment, 
	name 		varchar(50)		not null unique,
	description varchar(1000),
	primary key (id)
);
create table rm_task_category (
	id 			int 			auto_increment, 
	name 		varchar(50)		not null unique,
	description varchar(1000),
	primary key (id)
);
create table rm_group_category (
	id 			int 			auto_increment,
	name 		varchar(50) 	not null unique,
	description varchar(1000),
	primary key(id)
);
create table rm_privilege_type (
	id 			int 			auto_increment, 
	name 		varchar(50)		not null unique,
	description varchar(1000),
	primary key (id)
);
create table rm_group (
	id 					int 		auto_increment,
	name 				varchar(50) not null unique,
	founder_id 			int 		not null,
	group_category_id	int 		not null,
	founded 			datetime 	not null,
	decription 			varchar(1000),
	primary key(id),
	foreign key(founder_id) 		references rm_user(id),
	foreign key(group_category_id) 	references rm_group_category(id)
);
create table rm_is_member (
	id 				int 		auto_increment,		
	user_id			int 		not null,
	group_id 		int 		not null,
	privilege_type_id	int 	not null,
	date_joined 	datetime	not null,
	primary key (id),	
	foreign key (user_id) references rm_user(id),
	foreign key (group_id) references rm_group(id),
	foreign key (privilege_type_id) references rm_privilege_type(id)
);
create table rm_task (
	id 					int 		auto_increment,
	name 				varchar(50)	not null,
	is_group_task		boolean 	not null,
	task_type_id		int 		not null,
	task_category_id 	int 	 	not null,
	points_awarded		int 		default 0,
	award				varchar(255)	default '',	
	begin_date 			datetime 		not null,
	end_date 			datetime,
	primary key (id),
	foreign key (task_category_id) references rm_task_category(id),
	foreign key (task_type_id) references rm_task_type(id)
);
create table rm_user_task (
	id 					int 		auto_increment,
	taskee int not null,
	tasker int not null,
	task_id int not null,
	primary key (id),
	foreign key (taskee) references rm_user(id),
	foreign key (tasker) references rm_user(id),
	foreign key (task_id) references rm_task(id)
);
create table rm_group_task (
	id 				int 		auto_increment,
	taskee int not null,
	tasker int not null,
	task_id int not null,
	primary key (id),
	foreign key (taskee) references rm_group(id),
	foreign key (tasker) references rm_group(id),
	foreign key (task_id) references rm_task(id)
);
create table rm_user_monitor(
	id 					int 		auto_increment,
	user_id int not null,
	monitor_id int not null,
	task_id int not null,
	primary key (id),
	foreign key (user_id) references rm_user(id),
	foreign key (task_id) references rm_task(id),
	foreign key (monitor_id) references rm_user(id)
);
create table rm_group_monitor(
	id 					int 		auto_increment,
	user_id int not null,
	monitor_id int not null,
	task_id int not null,
	primary key (id),
	foreign key (user_id)   references rm_group(id),
	foreign key (monitor_id) references rm_group(id),
	foreign key (task_id) references rm_task(id)
);
create table rm_task_history (
	id 					int 		auto_increment,
	task_id int not null,
	date_done datetime not null,
	primary key (id),
	foreign key (task_id) references rm_task(id)
);
create table rm_follow(
	id 					int 		auto_increment,
	user_id int not null,
	friend_id int not null,
	primary key (id),
	foreign key (user_id)   references rm_user(id),
	foreign key (friend_id) references rm_user(id)
);
create table rm_friend(
	id 					int 		auto_increment,
	user_id int not null,
	friend_id int not null,
	privilege_type_id int not null,
	primary key (id),
	foreign key (user_id)   references rm_user(id),
	foreign key (friend_id) references rm_user(id),
	foreign key (privilege_type_id) references rm_privilege_type(id)
);
	
	
	
	

	
	
