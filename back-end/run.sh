#!/bin/bash

run() {
  if [[ $1 = "train" ]]; then
    train;
  elif [[ $1 = "start" ]]; then
    start;
  elif [[ $1 = "dev" ]]; then
    start --reload
  elif [[ $1 = "install" ]]; then
    install;
  elif [[ "$1" = "add" ]]; then
    add $2;
  else
    echo "Unrecognized command \"$1!\"";
    exit 1;
  fi
}

train() {
  python3 src/train_model.py;
}

start() {
  if [[ -z "${PORT}" ]]; then
    PORT=5008;
  fi

  if [[ -z "${HOST}" ]]; then
    HOST="0.0.0.0";
  fi

  uvicorn src.main:app --host $HOST --port $PORT "$@"
}

install() {
  python3 -m pip install -r requirements.txt
}

add() {
  echo "Adding \"$1\" to requirements.txt...";
  echo "$1" >> requirements.txt;
  install;
}

run "$@";
