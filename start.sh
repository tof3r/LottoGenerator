#!/bin/bash
app="lotto.generator"
docker build -t ${app} .
docker run -d -p 5000:80 --name=${app} -v $PWD:/lotto ${app}
