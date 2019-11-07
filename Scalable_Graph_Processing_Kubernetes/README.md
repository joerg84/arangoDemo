# Demo for Scalable Graph Processing on Kubernetes Webinar

### Import Data
```/usr/local/opt/arangodb/bin/arangoimport --server.password=test123 --file data/movies.csv --type csv --collection movies --create-collection true --translate "movie_id=_key"```

```/usr/local/opt/arangodb/bin/arangoimport --server.password=test123 --file data/users.csv --type csv --collection users --create-collection true --translate "user_id=_key"```

```/usr/local/opt/arangodb/bin/arangoimport --server.password=test123 --file data/ratings.csv --type csv --collection ratings --create-collection true --translate "user_id=_from" --translate "item_id=_to" --create-collection-type=edge --from-collection-prefix=users/  --to-collection-prefix=movies/```


### Queries
```
// Get all movies rated by User 1
FOR movie, edge IN ANY 'users/1' ratings  
    //FILTER edge.Rating == 5
    RETURN {
        "movie" : movie.` movie title `,
        "rating" : edge.Rating
    }
```

```
// Get all users who have also 5 star rating for 5 star rated movies by user 1
FOR movie, edge IN ANY 'users/1' ratings
    FILTER edge.Rating == 5
    FOR user, edge2 IN ANY movie ratings
        FILTER edge2.Rating == 5
        RETURN {
            "user" : user._key,
            "age" : user.Age
        }
```

  ```  
// Get all movie rated 5 star  users who have also 5 star rating for 5 star rated movies by user 1
FOR movie, edge IN ANY 'users/1' ratings
    FILTER edge.Rating == 5
    // All 5 star rated movies by user 1
    FOR user, edge2 IN ANY movie ratings
        FILTER edge2.Rating == 5
        // All users who have also rated that movie with 5 stars
        FOR movie2, edge3 IN ANY user ratings
            FILTER edge3.Rating == 5
            COLLECT title = movie2.` movie title `, url = movie2.` IMDb URL `
            RETURN {
                title,
                url
            }
```
