docker run --rm -v $PWD:/local openapitools/openapi-generator-cli generate --skip-validate-spec -i /local/textrepo-api.json  -v -g python  -o /local -p packageName=textrepo_client
