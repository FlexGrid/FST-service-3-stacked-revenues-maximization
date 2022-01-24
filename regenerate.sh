#!/bin/bash
set -euxo pipefail

err() {
  echo "**** FAIKED ****" 1>&2
}
trap err ERR 

java -jar ../swagger-codegen-3.0.32/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -l python-flask -i ./swagger/pricing.yml

if [ "${1:-}" == "checkout" ]
then
  git checkout .gitignore requirements.txt swagger_server/__main__.py swagger_server/controllers/authorization_controller.py swagger_server/util.py
fi
