DROP TABLE IF EXISTS locations;

CREATE TABLE locations (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	    name TEXT NOT NULL,
	    region TEXT NOT NULL,
	    coordinates TEXT NOT NULL
);
