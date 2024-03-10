#!/bin/bash
app="lotto.generator"
docker build -t ${app} .
docker run -d -p 55555:80 --name=${app} -v $PWD:/app ${app}