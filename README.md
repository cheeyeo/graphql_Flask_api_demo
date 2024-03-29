### GraphQL tutorial

[ariadne]: https://ariadnegraphql.org/
[Python graphql tutorial]: https://www.apollographql.com/blog/complete-api-guide
[Resolvers]: https://ariadnegraphql.org/docs/resolvers
[Flask integration]: https://ariadnegraphql.org/docs/flask-integration


A simple GraphQL API application built using **ariadne** and **Flask**. This is based on the original [Python graphql tutorial]

It consists of:

* A Flask API application running graphql
* A postgresql database 


It runs locally via docker compose:
```
docker compose -f compose.yaml up
```

To create some seed data:
```
source .env

python seed_db.py
```

Navigate to browser to **http://localhost:8000/graphql**

![GraphQL query editor](image.png)


#### Docs
- [ariadne]
- [Python graphql tutorial]
- [Resolvers]
- [Flask integration]


#### TODO:

* Use inputs in the schema and update the mutations

* The current queries are made via the graphql query editor.

How to make query via curl??

```
curl http://localhost:8080/ \
-F operations='{ "query":"mutation ($userid: String!, $file: Upload!) { uploadUserAvatar(userid: $userid, file: $file) }","variables": { "file": null, "userid": null } }' \
-F map='{ "0": ["variables.file"], "1": ["variables.userid"] }' \
-F 0=@etiqueta_LG.jpeg \
-F 1=abc1234
```*