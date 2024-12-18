docker run --rm --env=ADMIN_PASSWORD=admin --volume=/Users/nick/work/kurrawong/prez.dev/manifest/fuseki/configuration:/fuseki-base/configuration --volume=/Users/nick/work/kurrawong/prez.dev/manifest/fuseki/databases:/fuseki-base/databases -p 3030:3030 --name manifest-loader secoresearch/fuseki:5.1.0

