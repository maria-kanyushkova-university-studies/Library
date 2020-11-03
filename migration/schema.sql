create table book
(
    id                serial       not null
        constraint book_pk
            primary key,
    title             varchar(255) not null,
    description       text,
    rate              integer,
    isbn              varchar(50),
    year              integer,
    bbk               varchar(50),
    udc               varchar(50),
    link_in_publisher text,
    created_at        timestamp,
    updated_at        timestamp
);

alter table book
    owner to postgres;

create table author
(
    id         serial not null
        constraint author_pk
            primary key,
    surname    varchar(255),
    name       varchar(255),
    patronymic varchar(255),
    filename   uuid
);

alter table author
    owner to postgres;

create table series
(
    id    serial       not null
        constraint series_pk
            primary key,
    title varchar(255) not null
);

alter table series
    owner to postgres;

create table code
(
    id         serial       not null
        constraint code_pk
            primary key,
    code       varchar(255) not null,
    book_id    integer      not null
        constraint code_book_id_fk
            references book,
    is_deleted boolean default false,
    created_at timestamp    not null,
    updated_at timestamp    not null
);

alter table code
    owner to postgres;

create table asset
(
    filename   uuid        not null
        constraint asset_pk
            primary key,
    extension  varchar(10) not null,
    path       text        not null,
    created_at timestamp   not null,
    updated_at timestamp   not null
);

alter table asset
    owner to postgres;

create table "user"
(
    id            serial not null
        constraint user_pk
            primary key,
    surname       varchar(255),
    name          varchar(255),
    patronymic    varchar(255),
    filename      uuid
        constraint user_asset_filename_fk
            references asset,
    email         varchar(255),
    birthday      date,
    created_at    timestamp,
    updated_at    timestamp,
    access_token  text,
    refresh_token text
);

alter table "user"
    owner to postgres;

create table comment
(
    id         serial  not null
        constraint comment_pk
            primary key,
    title      text    not null,
    book_id    integer not null
        constraint comment_book_id_fk
            references book,
    user_id    integer not null
        constraint comment_user_id_fk
            references "user",
    rate       integer not null,
    created_at timestamp,
    updated_at timestamp
);

alter table comment
    owner to postgres;

create unique index asset_filename_uindex
    on asset (filename);

create table category
(
    id          serial       not null
        constraint category_pk
            primary key,
    title       varchar(255) not null,
    description text
);

alter table category
    owner to postgres;

create table label
(
    id    serial  not null
        constraint label_pk
            primary key,
    title integer not null
);

alter table label
    owner to postgres;

create table wishlist
(
    id         serial               not null
        constraint wishlist_pk
            primary key,
    book_id    integer              not null
        constraint wishlist_book_id_fk
            references book,
    user_id    integer              not null
        constraint wishlist_user_id_fk
            references "user",
    is_actual  boolean default true not null,
    created_at timestamp            not null,
    updated_at timestamp            not null
);

alter table wishlist
    owner to postgres;

create table publisher
(
    id       serial       not null
        constraint publisher_pk
            primary key,
    title    varchar(255) not null,
    filename uuid
        constraint publisher_asset_filename_fk
            references asset
);

alter table publisher
    owner to postgres;

create table reading_book
(
    id           serial    not null
        constraint reading_book_pk
            primary key,
    code_id      integer   not null
        constraint reading_book_code_id_fk
            references code,
    user_id      integer   not null
        constraint reading_book_user_id_fk
            references "user",
    started_day  timestamp not null,
    finished_day timestamp
);

alter table reading_book
    owner to postgres;

create table book_purchase
(
    id         serial               not null
        constraint book_purchase_pk
            primary key,
    title      varchar(255)         not null,
    author     varchar(255)         not null,
    link       text                 not null,
    comment    text                 not null,
    user_id    integer              not null
        constraint book_purchase_user_id_fk
            references "user",
    is_actual  boolean default true not null,
    created_at timestamp            not null,
    updated_at timestamp            not null
);

alter table book_purchase
    owner to postgres;

create table book_author
(
    book_id   integer not null
        constraint book_author_book_id_fk
            references book,
    author_id integer not null
        constraint book_author_author_id_fk
            references author,
    constraint book_author_pk
        unique (book_id, author_id)
);

alter table book_author
    owner to postgres;

create table book_publisher
(
    book_id      integer not null
        constraint book_publisher_book_id_fk
            references book,
    publisher_id integer not null
        constraint book_publisher_publisher_id_fk
            references publisher,
    constraint book_publisher_pk
        unique (book_id, publisher_id)
);

alter table book_publisher
    owner to postgres;

create table book_category
(
    book_id     integer not null
        constraint book_category_book_id_fk
            references book,
    category_id integer not null
        constraint book_category_category_id_fk
            references category,
    constraint book_category_pk
        unique (book_id, category_id)
);

alter table book_category
    owner to postgres;

create table book_label
(
    book_id  integer not null
        constraint book_label_book_id_fk
            references book,
    label_id integer not null
        constraint book_label_label_id_fk
            references label,
    constraint book_label_pk
        unique (book_id, label_id)
);

alter table book_label
    owner to postgres;

create table book_series
(
    book_id   integer not null
        constraint book_series_book_id_fk
            references book,
    series_id integer not null
        constraint book_series_series_id_fk
            references series,
    constraint book_series_pk
        unique (book_id, series_id)
);

alter table book_series
    owner to postgres;

create table book_asset
(
    book_id  integer not null
        constraint book_asset_book_id_fk
            references book,
    filename uuid    not null
        constraint book_asset_asset_filename_fk
            references asset
            on delete cascade,
    constraint book_asset_pk
        unique (book_id, filename)
);

alter table book_asset
    owner to postgres;

create table ebook
(
    filename uuid    not null
        constraint ebook_asset_filename_fk
            references asset
            on delete cascade,
    book_id  integer not null
        constraint ebook_book_id_fk
            references book,
    constraint ebook_pk
        unique (filename, book_id)
);

alter table ebook
    owner to postgres;

