#!/usr/bin/env bash
aws cloudformation create-stack --template-body file://templates/elb-stack.yml --stack-name prod

# to delete stack:
# aws cloudformation delete-stack --stack-name prod2
