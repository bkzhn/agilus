create database if not exists agilus;

create or replace table ticket_statuses
(
    id   int auto_increment
        primary key,
    name varchar(100) not null
);

create or replace table ticket_types
(
    id   int auto_increment
        primary key,
    name varchar(100) not null
);

create or replace table users
(
    id   int auto_increment
        primary key,
    name varchar(100) not null
);

create or replace table tickets
(
    id          int auto_increment
        primary key,
    title       varchar(100) not null,
    description text         not null,
    type_id     int          not null,
    status_id   int          not null,
    author_id   int          not null,
    assignee_id int          null,
    constraint tickets__ticket_statuses_id_fk
        foreign key (status_id) references ticket_statuses (id),
    constraint tickets__ticket_types_id_fk
        foreign key (type_id) references ticket_types (id),
    constraint tickets__users_id_fk
        foreign key (author_id) references users (id),
    constraint tickets__users_id_fk2
        foreign key (assignee_id) references users (id)
);

