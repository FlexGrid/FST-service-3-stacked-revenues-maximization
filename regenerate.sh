#!/bin/bash
java -jar ../swagger-codegen-3.0.32/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -l python-flask -i ./pricing.yml
git checkout .gitignore requirements.txt swagger_server/__main__.py swagger_server/controllers/authorization_controller.py
