# Demo for Scalable Graph Processing on Kubernetes Webinar

### Import Data
```/usr/local/opt/arangodb/bin/arangoimport --server.password=test123 --file data/movies.csv --type csv --collection movies --create-collection true --translate "item_id=_key"```

```/usr/local/opt/arangodb/bin/arangoimport --server.password=test123 --file data/users.csv --type csv --collection users --create-collection true --translate "user_id=_key"```

```/usr/local/opt/arangodb/bin/arangoimport --server.password=test123 --file data/ratings.csv --type csv --collection ratings --create-collection true --translate "user_id=_from" --translate "item_id=_to" --create-collection-type=edge --from-collection-prefix=users/  --to-collection-prefix=movies/```
