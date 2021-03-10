docker run --rm -v $PWD:/local openapitools/openapi-generator-cli generate --skip-validate-spec -i /local/swagger.json  -v -g python  -o /local -p packageName=textrepo_client 
