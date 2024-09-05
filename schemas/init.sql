create table if not exists ticket_statuses(
    id   serial primary key,
    name varchar(100) not null
);

create table if not exists ticket_types(
    id   serial primary key,
    name varchar(100) not null
);

create table if not exists users(
    id   serial primary key,
    name varchar(100) not null
);

create table if not exists tickets(
    id          serial primary key,
    title       varchar(100) not null,
    description text not null,
    type_id     int not null,
    status_id   int not null,
    author_id   int not null,
    assignee_id int,
    constraint tickets__ticket_statuses_id_fk
        foreign key (status_id) references ticket_statuses (id),
    constraint tickets__ticket_types_id_fk
        foreign key (type_id) references ticket_types (id),
    constraint tickets__users_id_fk
        foreign key (author_id) references users (id),
    constraint tickets__users_id_fk2
        foreign key (assignee_id) references users (id)
);
