#!/bin/bash
# Pass two varibles in post method
curl -sdX POST 'email=test@gmail.com&subject=I will always be here for PLD' "$1"