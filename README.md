# Installation

* install python 3.10
* pip install requirements.txt

# Database setup

using your favorite database create the following table:

```
CREATE TABLE products (
    id INT AUTOINCREMENT,
    name VARCHAR(45),
    value INT
);
```

# .env setup

.env example:

```
HOST=example
USER=example
PASSWORD=example
DATABASE=example
```